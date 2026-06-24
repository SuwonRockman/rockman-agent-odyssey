# 🚀 Season 2: Enterprise GraphRAG Masterclass

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](#)
[![Framework: Neo4j & LangChain](https://img.shields.io/badge/Framework-Neo4j%20%7C%20LangChain-0A84C6.svg)](#)

> **"Data is the new oil, but knowledge graphs are the refineries."**
> (데이터는 새로운 원유이지만, 지식 그래프는 그 원유를 정제하는 정유소다.)

이 마스터클래스(Season 2)는 파편화된 기업의 비정형 데이터(문서, 위키, 리포트)를 단순한 벡터 검색(Vector RAG)으로 찾는 한계를 넘어, 데이터 간의 '논리적 관계(Relationship)'를 추출하여 거대한 사내 지식망을 구축하고 하이브리드 검색을 수행하는 **엔터프라이즈 GraphRAG 풀스택 퀘스트**입니다.

---

## 🗺️ 커리큘럼 로드맵 (Curriculum Roadmap)

각 폴더의 링크를 클릭하여 해당 단계의 상세 파이프라인 구현 코드를 확인해 보세요!

### 🧱 Phase 1: Data Preparation (비정형 데이터 정제)
GraphRAG의 성공을 좌우하는 기초 공사. 원본 텍스트의 불순물을 제거하고 구조화합니다.
*   **Step 01. [Advanced Data Parsing](./graphrag-data-parsing/)**
    *   GIGO(Garbage In, Garbage Out) 방지 이론, 정규표현식(Regex) 기반의 Structural Chunking, 그리고 추론 근거(Citation)를 위한 Metadata Tagging 파이프라인 구현.

### 🕸️ Phase 2: Knowledge Extraction (지식망 추출)
*   **Step 02. [Knowledge Graph Extraction](./knowledge-graph-extraction/)**
    *   LLM 프롬프팅을 통한 Entity(개체)와 Relation(관계) 트리플렛(Triplet) 자동 추출 및 구조화.

### 🧠 Phase 3: Hybrid Retrieval (하이브리드 엔진)
*   **Step 03. [Neo4j Hybrid Search](./neo4j-hybrid-search/)**
    *   Neo4j 그래프 DB 적재(Cypher 쿼리) 및 Vector 유사도 검색을 결합한 하이브리드(Hybrid) 통합 알고리즘 검색 엔진 구축.

### 🏢 Phase 4: Enterprise Web UI (엔터프라이즈 검색 포털)
*   **Step 04. [GraphRAG Web UI](./graphrag-web-ui/)**
    *   Streamlit 웹 어플리케이션 개발 및 NetworkX/PyVis를 활용한 사내 지식 검색(Cognitive Search) 시각화 인터페이스 통합.

### 🤖 Phase 5: Auto-Ingestion Pipeline (완전 자동화 데이터 수집기)
*   **Step 05. [Auto Ingestion Pipeline](./auto-ingestion-pipeline/)**
    *   사용자의 로컬 마크다운 폴더(`DataCollectionVault/raw`)를 모니터링하여, 매일 쏟아지는 원본 데이터를 자동으로 파싱하고 LLM을 통해 지식망으로 변환한 뒤 Neo4j DB에 실시간 적재하는 백그라운드 자동화 봇.

---

## 🛠️ 기술 스택 (Tech Stack)
*   **Language:** Python 3.10+
*   **Graph DB:** Neo4j, Cypher
*   **Vector DB & LLM:** FAISS, OpenAI API, LangChain
*   **Environment:** Jupyter Notebook, Streamlit

<br>
<div align="center">
  <i>Created with ❤️ by Jung Seyoon (SuwonRockman)</i>
</div>
