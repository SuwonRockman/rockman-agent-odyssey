# 🚀 Industrial MLOps & Cognitive DS Masterclass

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](#)
[![Frameworks: PyTorch & Neo4j](https://img.shields.io/badge/Framework-PyTorch%20%7C%20Neo4j-0A84C6.svg)](#)

> **"What I cannot create, I do not understand."** - Richard Feynman
> (내가 직접 만들 수 없는 것은, 내가 온전히 이해한 것이 아니다.)

이 마스터클래스는 산업용 데이터 과학(Industrial Data Science), 인지 검색(Cognitive Search), 그리고 프로덕션 MLOps(Machine Learning Operations)를 다루는 전문가 과정 포트폴리오입니다. 실제 제조 및 산업 도메인의 대규모 센서 데이터, 텍스트 매뉴얼, 분산 데이터베이스 환경을 기반으로 모델을 학습하고 지속 가능하게 운영하는 엔지니어링 체계를 구축합니다.

---

## 🎯 주요 아키텍처 및 하이라이트

1. **산업용 시계열 모델링 & 최적화**: 공장 설비 센서 데이터를 전처리하고 XGBoost 기반의 예지 보전(Predictive Maintenance) 장애 분류 및 잔여 수명(RUL) 회귀 분석 구현.
2. **설명 가능한 AI (XAI)**: SHAP, LIME 등을 활용하여 복잡한 머신러닝 예측 모델의 내부 의사결정을 시각화하고 설비 고장의 근본 원인(Root Cause Analysis) 분석.
3. **인지형 지식 검색 (Cognitive GraphRAG)**: 비정형 설비 매뉴얼에서 Entity/Relation을 정밀 파싱하고 **Neo4j 그래프 데이터베이스**와 결합한 하이브리드 검색망 설계.
4. **실시간 MLOps 운영 및 모니터링**: **MLflow**를 통해 에이전트와 예측 모델의 성능 지표를 추적하고, **Evidently AI**를 연동하여 실시간 데이터/모델 드리프트(Drift) 탐지 및 자동 재학습 파이프라인 연동.

---

## 🗺️ 커리큘럼 로드맵 (Curriculum Roadmap)

각 폴더로 이동하여 상세한 구현 코드와 주피터 노트북을 확인하세요.

### 📈 [Season 1: Predictive Modeling & Optimization](./Industrial_MLOps_Cognitive_DS_Masterclass/Season1_Predictive_Modeling_Optimization/)
산업용 센서 데이터를 다루는 데이터 분석부터 머신러닝 예측 모델 및 설명 가능한 AI(XAI) 분석까지 다루는 5단계 실습 과정입니다.

*   **Phase 1: Industrial Time-Series Preprocessing** (시계열 센서 데이터 전처리 및 정제)
*   **Phase 2: Imbalanced Data & Feature Engineering** (클래스 불균형 해결 및 도메인 피처 생성)
*   **Phase 3: Equipment Failure Classification** (설비 장애 분류 모델링 및 XGBoost)
*   **Phase 4: RUL (Remaining Useful Life) Regression** (잔여 수명 예측 회귀 모델 구현)
*   **Phase 5: Explainable AI & Root Cause Analysis** (SHAP 기반 기여도 시각화 및 근본 원인 분석)

👉 **[Season 1 상세 커리큘럼 보기](./Industrial_MLOps_Cognitive_DS_Masterclass/Season1_Predictive_Modeling_Optimization/README.md)**

---

### 🕸️ Season 2: Cognitive Search & GraphRAG (준비 중)
비정형 산업 문서를 파싱하고 Neo4j를 이용하여 논리적 지식망(Knowledge Graph) 하이브리드 검색 엔진을 구축하는 인지형 검색 포털 설계 과정입니다. (시즌 1 완료 후 개설 예정)

*   **Phase 1: Structural Ingest & Parsing** (산업 매뉴얼 텍스트 데이터 파싱)
*   **Phase 2: Industrial Knowledge Triplet Extraction** (LLM 프롬프팅 기반 Entity & Relation 추출)
*   **Phase 3: Neo4j Graph DB Integration** (지식 그래프 DB 적재 및 Cypher 검색 설계)
*   **Phase 4: Cognitive Hybrid Retrieval** (의미 유사도 + 지식 위상 하이브리드 검색 엔진)
*   **Phase 5: Web Command Portal** (Streamlit 기반 지식 검색 UI 구축)

---

### ⚙️ Season 3: Agent Swarm & MLOps (준비 중)
LangGraph 에이전트 군집 환경과 배포 자동화, 그리고 MLflow 및 Evidently AI를 활용한 실시간 MLOps 아키텍처 구축 과정입니다. (시즌 2 완료 후 개설 예정)

*   **Phase 1: Agent Collaboration Architecture** (LangGraph 기반 예외 처리 에이전트 군집 설계)
*   **Phase 2: Production API Service** (FastAPI & Docker 기반 에이전트 마이크로서비스 빌드)
*   **Phase 3: MLflow Tracking & Register** (모델 매트릭 트래킹 및 중앙 관리)
*   **Phase 4: Data Drift & Monitoring** (Evidently AI 연동 실시간 데이터 변동 탐지)
*   **Phase 5: Automated CI/CD & Retraining Pipeline** (자동 재학습 파이프라인 배포)

---

## 🗄️ Completed Projects (Archived)
기존에 완료된 AI Agent 및 RAG 기초 프로젝트들은 아래 링크를 통해 안전하게 유지 및 확인하실 수 있습니다.

*   🧠 **[Season 1: LLM Foundation & Agents (Archived)](./Season1_LLM_Masterclass/)** - 밑바닥 트랜스포머 구현, LoRA 파인튜닝, RLHF/DPO 정렬, ReAct 에이전트.
*   🕸️ **[Season 2: Enterprise GraphRAG Masterclass (Archived)](./Season2_GraphRAG_Masterclass/)** - Neo4j 지식 그래프 추출, 하이브리드 검색 엔진 및 자동 수집 파이프라인.
*   🤖 **[Season 3: Autonomous AX Command Center (Archived)](./Season3_MultiAgent_Swarm/)** - LangGraph 멀티 에이전트 군집 기반 스마트팩토리 실시간 관제 시스템.

---

## 🛠️ 기술 스택 (Tech Stack)

### Core AI & Data Science
* **ML & DL Frameworks:** PyTorch, HuggingFace, XGBoost, Scikit-learn, Scipy, Pandas
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
