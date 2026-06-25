import os
import sys
import glob
import json
import re
from dotenv import load_dotenv
from neo4j import GraphDatabase
from openai import OpenAI
from langchain_core.documents import Document
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. 환경 설정 및 클라이언트 초기화
import os
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))
sys.path.append(os.path.dirname(env_path))
load_dotenv(env_path)

# 경로 설정: 이제 raw 폴더 전체를 재귀적으로 타겟팅합니다.
VAULT_PATH = r"C:\Users\정세윤\OneDrive\Desktop\DataCollectionVault\Stock_US\raw"
TRACKER_FILE = "processed_files.json"

URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
AUTH = (os.getenv("NEO4J_USERNAME", "neo4j"), os.getenv("NEO4J_PASSWORD", "graphrag2026"))

driver = GraphDatabase.driver(URI, auth=AUTH)
openai_client = OpenAI()
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
llm_transformer = LLMGraphTransformer(llm=llm)

# 일반 텍스트용 분쇄기 (Fallback)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

# 2. 파일 트래커 로직
def load_processed_files():
    if os.path.exists(TRACKER_FILE):
        with open(TRACKER_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def mark_as_processed(file_path):
    files = load_processed_files()
    if file_path not in files:
        files.append(file_path)
        with open(TRACKER_FILE, 'w', encoding='utf-8') as f:
            json.dump(files, f, ensure_ascii=False, indent=2)

# 3. 듀얼 모드 파싱 (Phase 1)
def parse_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    filename = os.path.basename(file_path)
    documents = []

    # Mode A: '## 숫자️⃣' 포맷이 있는지 확인
    if re.search(r'\n## \d+️⃣ ', content):
        # YAML Frontmatter 제거 (--- ... ---)
        content_stripped = re.sub(r'^---.*?---\n', '', content, flags=re.DOTALL)
        blocks = re.split(r'\n## \d+️⃣ ', content_stripped)
        
        for block in blocks:
            block = block.strip()
            if not block or block.startswith('#'): continue
            
            lines = block.split('\n')
            title = lines[0].strip()
            body = '\n'.join(lines[1:]).strip()
            body = re.sub(r'---', '', body).strip()
            
            if body:
                doc = Document(page_content=body, metadata={"source": file_path, "title": title, "mode": "strict"})
                documents.append(doc)
    
    # Mode B: 일반 텍스트 파일 (.txt) 또는 비구조화 마크다운
    else:
        # YAML 제거 시도
        content_stripped = re.sub(r'^---.*?---\n', '', content, flags=re.DOTALL).strip()
        if content_stripped:
            # 1000자 단위로 자르기
            chunks = text_splitter.split_text(content_stripped)
            for i, chunk in enumerate(chunks):
                doc = Document(page_content=chunk, metadata={"source": file_path, "chunk_id": i, "mode": "fallback"})
                documents.append(doc)
            
    return documents

# 4. Neo4j 삽입 (Phase 2)
def ingest_graph_documents(tx, graph_documents):
    for doc in graph_documents:
        # 노드 생성
        for node in doc.nodes:
            tx.run("MERGE (n:Entity {id: $id})", id=node.id)
            
        # 엣지 생성
        for rel in doc.relationships:
            # 관계 이름 정제 (공백 및 특수문자를 언더스코어로)
            rel_type = rel.type.replace(' ', '_').replace('-', '_').replace('/', '_').upper()
            query = f"""
            MATCH (source:Entity {{id: $source_id}})
            MATCH (target:Entity {{id: $target_id}})
            MERGE (source)-[r:{rel_type}]->(target)
            """
            tx.run(query, source_id=rel.source.id, target_id=rel.target.id)

# 5. 벡터 임베딩 (Phase 3)
def setup_vector_embeddings(tx):
    # 아직 임베딩이 없는 노드들만 선택
    result = tx.run("MATCH (n:Entity) WHERE n.embedding IS NULL RETURN elementId(n) AS internal_id, n.id AS text")
    nodes = [record for record in result]
    
    if nodes:
        print(f"[{len(nodes)}개의 새로운 노드에 임베딩을 생성합니다...]")
        texts = [n['text'] for n in nodes]
        
        # 한 번에 최대 1000개씩 나눠서 API 호출 (안전성)
        batch_size = 1000
        for i in range(0, len(texts), batch_size):
            batch_texts = texts[i:i+batch_size]
            batch_nodes = nodes[i:i+batch_size]
            
            response = openai_client.embeddings.create(input=batch_texts, model="text-embedding-3-small")
            
            for j, node in enumerate(batch_nodes):
                embedding = response.data[j].embedding
                tx.run("MATCH (n) WHERE elementId(n) = $int_id SET n.embedding = $emb", 
                       int_id=node['internal_id'], emb=embedding)
        print("[임베딩 업데이트 완료!]")

def create_vector_index(tx):
    query_index = """
    CREATE VECTOR INDEX entity_index IF NOT EXISTS
    FOR (n:Entity) ON (n.embedding)
    OPTIONS {indexConfig: {
      `vector.dimensions`: 1536,
      `vector.similarity_function`: 'cosine'
    }}
    """
    tx.run(query_index)

# 6. 메인 파이프라인
def run_pipeline():
    print("=== Universal Auto-Ingestion Pipeline Started ===")
    processed = load_processed_files()
    
    # 하위 폴더까지 모든 .md와 .txt 검색
    all_files = []
    for ext in ["*.md", "*.txt"]:
        all_files.extend(glob.glob(os.path.join(VAULT_PATH, "**", ext), recursive=True))
    
    # 윈도우 경로 정규화 후 중복 체크
    all_files = [os.path.normpath(f) for f in all_files]
    new_files = [f for f in all_files if f not in processed]
    
    if not new_files:
        print("새로 처리할 파일이 없습니다.")
        return
        
    print(f"총 {len(new_files)}개의 새로운 파일을 발견했습니다.")
    
    new_data_inserted = False
    
    for file_path in new_files:
        print(f"\n>> 처리 중: {os.path.basename(file_path)}")
        docs = parse_file(file_path)
        print(f"  - {len(docs)}개의 텍스트 청크 파싱 완료")
        
        if docs:
            print("  - LLM으로 지식망(Graph) 추출 중... (시간이 다소 소요됩니다)")
            try:
                graph_docs = llm_transformer.convert_to_graph_documents(docs)
                print(f"  - 추출 완료: {sum(len(d.nodes) for d in graph_docs)}개 노드, {sum(len(d.relationships) for d in graph_docs)}개 엣지")
                
                print("  - Neo4j에 데이터 적재 중...")
                with driver.session() as session:
                    session.execute_write(ingest_graph_documents, graph_docs)
                
                new_data_inserted = True
            except Exception as e:
                print(f"  - [오류 발생] 지식 추출 실패: {e}")
            
        mark_as_processed(file_path)
        print("  - 처리 완료 및 기록 장부 업데이트")
        
    if new_data_inserted:
        print("\n>> 새로운 지식망에 대한 임베딩(Vector) 주입 작업 시작...")
        with driver.session() as session:
            session.execute_write(setup_vector_embeddings)
            session.execute_write(create_vector_index)
            
    print("\n=== Pipeline Finished Successfully ===")

if __name__ == "__main__":
    run_pipeline()
