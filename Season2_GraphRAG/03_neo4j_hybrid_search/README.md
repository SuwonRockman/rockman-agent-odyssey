# Step 03. Hybrid GraphRAG Search Engine 🧠

이 레포지토리는 저장된 지식망을 기반으로 사용자의 질문에 답하는 **Hybrid Search Engine (하이브리드 검색 엔진)** 파이프라인을 구현합니다.

## 📝 1. 프로젝트 목적
일반적인 RAG 시스템은 단순히 의미가 비슷한 문서 조각(Vector)을 찾아옵니다. 하지만 GraphRAG는 '테슬라'라는 단어를 찾아낸 뒤, 그 단어와 연결된 선(Edge)을 타고 넘어가 '일론 머스크', '스페이스X', '트위터 인수 리스크' 등의 **보이지 않는 문맥(Context)**까지 통째로 가져옵니다. 

이 레포지토리에서는 Neo4j의 내장 Vector Index를 활용해 텍스트 임베딩과 그래프 탐색을 파이썬으로 결합합니다.

## 📂 2. 폴더 구조
*   `notebook/01_theory.md`: 왜 Vector DB 단독으로는 한계가 명확한지, 그리고 Graph 탐색을 섞었을 때(Hybrid) 왜 환각 현상(Hallucination)이 극적으로 줄어드는지 증명합니다.
*   `notebook/02_algorithm_from_scratch.ipynb`: 블랙박스 프레임워크(LangChain)의 고수준 함수에 의존하지 않고, 직접 노드에 임베딩 벡터를 주입하고 Cypher 쿼리로 하이브리드 검색을 구현하는 핵심 파이썬 코드입니다.

## 🚀 3. 실행 방법
1. `neo4j-hybrid-search/notebook` 폴더로 이동합니다.
2. `.env` 파일에 `OPENAI_API_KEY`와 Neo4j 접속 정보가 정상적으로 세팅되어 있는지 확인합니다.
3. `02_algorithm_from_scratch.ipynb`를 열고 순서대로 실행합니다.
