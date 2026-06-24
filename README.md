# 🚀 Industrial MLOps & Cognitive DS Masterclass

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](#)
[![Frameworks: PyTorch & Neo4j](https://img.shields.io/badge/Framework-PyTorch%20%7C%20Neo4j-0A84C6.svg)](#)

> **"What I cannot create, I do not understand."** - Richard Feynman
> (내가 직접 만들 수 없는 것은, 내가 온전히 이해한 것이 아니다.)

단순히 오픈소스 라이브러리를 조립하는 것을 넘어, **자연어 처리 기초부터 최상위 엔터프라이즈 자율 에이전트, Cognitive RAG 검색망, 그리고 산업용 MLOps 모니터링 시스템까지** 밑바닥부터 수학적으로 증명하며 구축해 나가는 대규모 마스터클래스 포트폴리오입니다.

전체 커리큘럼은 **3개의 거대한 시즌(Season 1, 2, 3)**으로 구성되어 있으며, 각 시즌은 유기적으로 연결된 **5개의 Phase**로 세분화되어 제공됩니다.

---

## 🎯 주요 아키텍처 및 하이라이트

1. **밑바닥부터 짜는 트랜스포머 (PyTorch)**: BPE 토크나이저, Attention 매트릭스, LoRA 파라미터 튜닝, RLHF(DPO)를 직접 수학적으로 구현.
2. **사내 데이터 분석 에이전트 (Code Interpreter)**: Text-to-SQL 및 자가 디버깅 루프(ReAct)가 내장된 BI 자율 분석기.
3. **거대 지식망 구축 (Enterprise GraphRAG)**: 비정형 데이터에서 개체/관계(Entity/Relation)를 추출하여 **Neo4j DB**에 적재하고 Vector와 하이브리드 검색을 수행하는 최첨단 RAG 엔진.
4. **스마트팩토리 멀티 에이전트 군집 (Swarm)**: 센서 감시, GraphRAG 복구 지시, SQLite 재고 공급사 발주 등의 전문 에이전트들이 **LangGraph** 상에서 자율 협업하는 시스템.
5. **엔터프라이즈 운영 (MLOps & LLMOps)**: FastAPI 마이크로서비스, Docker 컨테이너, MLflow 및 Evidently AI를 활용한 실시간 데이터 드리프트 탐지 및 파이프라인.

---

## 🗺️ 커리큘럼 로드맵 (Curriculum Roadmap)

각 폴더로 이동하여 상세한 구현 코드와 주피터 노트북을 확인하세요.

### 🧠 [Season 1: LLM Foundation & Agents](./Season1_LLM_Masterclass/)
언어 모델의 수학적 기초부터 트랜스포머 아키텍처, 그리고 자율 행동 에이전트(Autonomous Agents)까지 진화하는 5단계 커리큘럼입니다. (기존 13개 퀘스트 포함)

*   **Phase 1: NLP Foundation** (BPE 토크나이저, 임베딩 수학적 구현)
*   **Phase 2: Deep Learning & Attention** (RNN/Seq2Seq, Attention, Transformer, Pretrained LM)
*   **Phase 3: Parameter-Efficient Tuning & Alignment** (LoRA 최적화, RLHF & DPO 정렬)
*   **Phase 4: Advanced Retrieval & Agents** (HNSW 계층형 인덱싱 RAG, ReAct 자율 에이전트)
*   **Phase 5: Domain Solutions & Production** (BI 데이터 분석 SQL 에이전트, 예외 대응 에이전트, LLMOps)

👉 **[Season 1 상세 커리큘럼 보기](./Season1_LLM_Masterclass/README.md)**

---

### 🕸️ [Season 2: Enterprise GraphRAG Masterclass](./Season2_GraphRAG_Masterclass/)
기업의 방대한 비정형 데이터를 논리적 지식망(Knowledge Graph)으로 정제하여 연결하는 Cognitive Search 아키텍처 구축기입니다.

*   **Phase 1: Structural Data Parsing** (구조적 청킹, Regex, 메타데이터 태깅)
*   **Phase 2: LLM-based Knowledge Extraction** (LLM 프롬프팅 기반 Entity & Relation 자동 추출)
*   **Phase 3: Neo4j Hybrid Search Engine** (Neo4j 그래프 검색 + Vector 유사도 하이브리드 엔진)
*   **Phase 4: Command UI Portal** (Streamlit & NetworkX 기반 사내 지식 검색 UI)
*   **Phase 5: Automated Ingestion Pipeline** (신규 업로드 데이터 파싱 및 Neo4j 자동 적재 파이프라인)

👉 **[Season 2 상세 커리큘럼 보기](./Season2_GraphRAG_Masterclass/README.md)**

---

### ⚙️ [Season 3: Autonomous AX Command Center (Multi-Agent Swarm)](./Season3_MultiAgent_Swarm/)
센서 데이터, SQL 재고 DB, Neo4j GraphRAG가 복합적으로 연계되어 실시간 장애를 대응하는 자율 협업 공장 관제 시스템과 MLOps 모니터링입니다.

*   **Phase 1: Edge Sensor Data & Environment Setup** (SQLite DB 설계, 센서 데이터 수집 환경)
*   **Phase 2: Individual Specialist Agent Nodes** (이상 탐지 에이전트, GraphRAG 정비 에이전트, SQL 재고 에이전트)
*   **Phase 3: LangGraph Supervisor Choreography** (LangGraph State Machine을 활용한 자율 협업 및 라우팅 루프)
*   **Phase 4: Real-time Web Dashboard Portal** (Streamlit 기반 관제 센터 웹 대시보드 시각화)
*   **Phase 5: MLOps Monitoring & Drift Analysis** (MLflow 및 Evidently AI를 사용한 실시간 센서/모델 모니터링)

👉 **[Season 3 상세 커리큘럼 보기](./Season3_MultiAgent_Swarm/README.md)**

---

## 🛠️ 기술 스택 (Tech Stack)

### Core AI & Data Science
* **ML & DL Frameworks:** PyTorch, HuggingFace Transformers, XGBoost, Scikit-learn
* **Agentic Frameworks:** LangGraph, LangChain, OpenAI API
* **Vector & Graph DB:** FAISS, Sentence-Transformers, Neo4j, Cypher, SQLite

### Infrastructure, Ops & Monitoring
* **MLOps / LLMOps:** MLflow, Evidently AI, FastAPI, Docker
* **Frontend & Dashboards:** Streamlit, NetworkX, PyVis
* **CI/CD & Testing:** GitHub Actions, Pytest

---

<br>
<div align="center">
  <i>Created with ❤️ by Jung Seyoon (SuwonRockman)</i>
</div>
