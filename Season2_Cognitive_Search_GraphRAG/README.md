# 🕸️ Season 2: Cognitive Search & GraphRAG (인지형 검색 & GraphRAG)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](#)
[![Framework: Neo4j & LangChain](https://img.shields.io/badge/Framework-Neo4j%20%7C%20LangChain-0A84C6.svg)](#)

본 과정은 비정형 텍스트로 구성된 산업용 매뉴얼과 정비 지침서를 지식 그래프(Knowledge Graph)로 정제하여, Neo4j 기반의 인지형 검색(Cognitive Search) 포털을 완수하는 프로젝트 과정입니다.

---

## 🗺️ 5단계 커리큘럼 로드맵 (Curriculum Roadmap)

### 🧱 Phase 1: Structural Ingest & Parsing
*   산업용 설비 장애 조치 지침서 등 원본 문서를 청크 단위로 나누고, 메타데이터 태그와 출처(Citation)를 남기기 위한 전처리 파이프라인.

### 🕸️ Phase 2: Industrial Knowledge Triplet Extraction
*   LLM 프롬프팅 설계를 통하여 원본 데이터에서 Entity(설비, 고장 현상)와 Relation(원인, 조치 방법) 트리플렛을 고신뢰도로 자동 추출하는 기술.

### 🧠 Phase 3: Neo4j Graph DB Integration
*   Cypher 쿼리 구조화 및 Neo4j 데이터베이스 연동. 추출된 노드와 엣지를 그래프 데이터베이스에 자동 적재하는 스키마 모델링.

### 🏢 Phase 4: Cognitive Hybrid Retrieval
*   단순 Vector Embedding 검색의 한계를 극복하기 위해, 의미적 유사도 검색(Vector Search)과 지식의 위상학적 구조 검색(Graph Search)을 통합한 하이브리드 검색 알고리즘 구현.

### ⚙️ Phase 5: Web Command Portal
*   Streamlit 및 NetworkX 시각화 라이브러리를 연동하여, 현장 정비사가 키워드로 검색했을 때 관련 지식 토폴로지와 최적 조치 방안을 실시간으로 확인하는 웹 UI 통합 구축.

---

## 🛠️ 실습 환경 준비
시즌 2를 시작하게 될 경우 필요한 핵심 패키지들은 추후 업데이트될 예정입니다.
*   **대표 사용 패키지**: `neo4j`, `openai`, `langchain`, `streamlit`, `pyvis`
