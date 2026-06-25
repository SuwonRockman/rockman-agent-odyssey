import os
import sys
from neo4j import GraphDatabase
from openai import OpenAI
from dotenv import load_dotenv

# 상위 폴더의 .env 파일 로드
import os
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))
sys.path.append(os.path.dirname(env_path))
load_dotenv(env_path)

URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
AUTH = (os.getenv("NEO4J_USERNAME", "neo4j"), os.getenv("NEO4J_PASSWORD", "graphrag2026"))

driver = GraphDatabase.driver(URI, auth=AUTH)
client = OpenAI()

def get_hybrid_context(question, top_k=3):
    """
    질문을 임베딩하고 Neo4j에서 Vector+Graph 하이브리드 검색을 수행하여 
    문맥 텍스트와 시각화용 레코드 리스트를 반환합니다.
    """
    question_embedding = client.embeddings.create(
        input=question, model="text-embedding-3-small"
    ).data[0].embedding
    
    query = """
    CALL db.index.vector.queryNodes('entity_index', $k, $embedding)
    YIELD node, score
    MATCH (node)-[r]-(neighbor)
    RETURN node.id AS source, type(r) AS relationship, neighbor.id AS target, score
    ORDER BY score DESC
    """
    
    with driver.session() as session:
        results = session.run(query, k=top_k, embedding=question_embedding)
        records = [record.data() for record in results]
        
    context_list = []
    for r in records:
        fact = f"{r['source']} -[{r['relationship']}]-> {r['target']}"
        if fact not in context_list:
            context_list.append(fact)
            
    context_str = "\n".join(context_list)
    return context_str, records

def generate_answer(question, context_str):
    """
    추출된 문맥을 바탕으로 LLM 답변을 Streaming으로 생성합니다.
    """
    system_prompt = f"""
    You are an expert financial graph analyst. 
    Answer the user's question using ONLY the provided knowledge graph context.
    If the context doesn't contain the answer, say 'I do not have enough information'.
    Respond in Korean.
    
    [GRAPH CONTEXT]
    {context_str}
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        temperature=0,
        stream=True
    )
    return response
