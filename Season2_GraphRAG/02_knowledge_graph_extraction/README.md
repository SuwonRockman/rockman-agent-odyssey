# Step 02. Neo4j Knowledge Graph Extraction 🕸️

이 레포지토리는 GraphRAG의 심장부인 **지식망 추출(Knowledge Extraction)** 파이프라인의 엔터프라이즈 표준(Standard) 구현체를 다룹니다.

## 📝 1. 프로젝트 목적
문서(텍스트) 속에서 Entity(주체/객체)와 Relation(관계)를 찾아냅니다. LangChain의 Graph 툴킷과 프롬프트를 활용하여 텍스트를 구조화된 노드와 엣지로 변환하고, 이를 실제 엔터프라이즈 그래프 데이터베이스인 **Neo4j**에 적재(Insert)합니다. 

## 📂 2. 폴더 구조
*   `data/`: Step 01에서 파싱된 `parsed_chunks.json`을 읽어옵니다.
*   `notebook/01_theory.md`: 기존 관계형 데이터베이스(RDBMS)와 그래프 DB의 근본적인 구조적 차이점, 그리고 Neo4j의 쿼리 언어인 **Cypher**의 기초 문법을 다룹니다.
*   `notebook/02_algorithm_from_scratch.ipynb`: LangChain `LLMGraphTransformer`를 이용해 파이썬 메모리에서 지식망을 추출하고, Neo4j DB 인스턴스에 밀어넣는 핵심 파이프라인 코드입니다.

## 🚀 3. 실행 방법 (환경 설정)
이 모듈을 실행하려면 `.env` 파일에 다음 환경 변수가 필요합니다:
*   `OPENAI_API_KEY` (지식 추출용)
*   `NEO4J_URI`, `NEO4J_USERNAME`, `NEO4J_PASSWORD` (로컬 Desktop 또는 클라우드 AuraDB)

1. `notebook` 폴더로 이동합니다.
2. `02_algorithm_from_scratch.ipynb`를 실행하여 텍스트 데이터가 Neo4j 데이터베이스 노드로 변환되는 과정을 확인합니다.
