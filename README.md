# 🚀 Advanced AI Agents Masterclass

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](#)
[![Frameworks: PyTorch & Neo4j](https://img.shields.io/badge/Framework-PyTorch%20%7C%20Neo4j-0A84C6.svg)](#)

> **"What I cannot create, I do not understand."** - Richard Feynman
> (내가 직접 만들 수 없는 것은, 내가 온전히 이해한 것이 아니다.)

단순히 오픈소스 라이브러리(HuggingFace, LangChain)를 조립해서 그럴싸한 장난감을 만드는 것에 만족하지 않습니다.
이 프로젝트는 **자연어 처리의 밑바닥(Word2Vec, Tokenization)부터 시작하여, 최상위 엔터프라이즈급 AI 자율 에이전트 및 GraphRAG 하이브리드 검색 아키텍처까지 100% 직접 텐서 단위로 증명하며 구축해 나가는 대규모 마스터클래스 포트폴리오**입니다.

전체 커리큘럼은 크게 **Season 1 (LLM Foundation & Agents)**과 **Season 2 (Enterprise GraphRAG)** 두 가지 거대한 모듈로 구성되어 있습니다.

---

## 🎯 주요 아키텍처 및 하이라이트

1. **밑바닥부터 짜는 트랜스포머 (PyTorch)**: BPE 토크나이저, Attention 매트릭스, LoRA 파라미터 튜닝, RLHF(DPO)를 직접 수학적으로 구현.
2. **사내 데이터 분석 에이전트 (Code Interpreter)**: Text-to-SQL 및 자가 디버깅 루프(ReAct)가 내장된 BI 자율 분석기.
3. **제조업 다운타임 방어 (AX Factory Agent)**: ERP(센서 데이터)와 공장 매뉴얼을 연동하여 스스로 장애를 해결하는 도메인 특화 에이전트.
4. **거대 지식망 구축 (Enterprise GraphRAG)**: 비정형 데이터에서 개체/관계(Entity/Relation)를 추출하여 **Neo4j DB**에 적재하고 Vector와 하이브리드 검색을 수행하는 최첨단 RAG 엔진.
5. **엔터프라이즈 운영 (LLMOps)**: FastAPI 마이크로서비스, Docker 컨테이너화, GitHub Actions 기반 CI/CD 파이프라인.

---

## 🗺️ 커리큘럼 로드맵 (Curriculum Roadmap)

각 폴더로 이동하여 상세한 구현 코드와 주피터 노트북(`01_theory.md`, `02_algorithm_from_scratch.ipynb`)을 확인하세요.

### 🧠 [Season 1: LLM Foundation & Agents](./Season1_LLM_Masterclass/)
언어 모델의 수학적 기초부터 트랜스포머 아키텍처, 그리고 자율 행동 에이전트(Autonomous Agents)까지 진화하는 13단계의 퀘스트입니다.

* **Phase 1: Foundation** (Embeddings, Tokenization)
* **Phase 2: Architecture** (RNN/Seq2Seq, Attention, Transformer)
* **Phase 3: Scaling & Optimization** (Pretrained LM, LoRA)
* **Phase 4: Agents & Production** (RLHF, Advanced RAG, Agentic Workflow)
* **Phase 5: Domain AX Solutions** (Data Analyst Agent, Factory Agent)
* **Phase 6: Enterprise LLMOps** (CI/CD Pipeline, Docker)

👉 **[Season 1 상세 커리큘럼 보기](./Season1_LLM_Masterclass/README.md)**

---

### 🕸️ [Season 2: Enterprise GraphRAG Masterclass](./Season2_GraphRAG_Masterclass/)
기업의 방대한 비정형 데이터를 논리적 지식망(Knowledge Graph)으로 정제하여 연결하는 Cognitive Search 아키텍처 구축기입니다.

* **Phase 1: Data Parsing** (구조적 청킹, Regex, 메타데이터 태깅)
* **Phase 2: Graph Extraction** (LLM 프롬프팅 기반 Entity & Relation 자동 추출)
* **Phase 3: Hybrid Search** (Neo4j 기반 그래프 검색 + Vector 유사도 하이브리드 엔진)
* **Phase 4: Web Portal** (Streamlit & NetworkX 기반 사내 지식 검색 UI)
* **Phase 5: Auto-Ingestion Pipeline** (매일 쏟아지는 원본 데이터를 자동으로 파싱하고 Neo4j에 적재하는 완전 자동화 봇)

👉 **[Season 2 상세 커리큘럼 보기](./Season2_GraphRAG_Masterclass/README.md)**

---

## 🛠️ 기술 스택 (Tech Stack)

### Core AI & Data
* **Machine Learning:** Python, PyTorch, HuggingFace (Transformers, TRL, Evaluate)
* **Agentic Frameworks:** LangChain, LlamaIndex, OpenAI API
* **Vector & Graph DB:** FAISS, Sentence-Transformers, Neo4j, Cypher

### Infrastructure & Ops
* **Backend:** FastAPI, SQLite
* **Frontend/Visualization:** Streamlit, NetworkX, PyVis
* **DevOps:** Docker, GitHub Actions (CI/CD), Pytest

---

<br>
<div align="center">
  <i>Created with ❤️ by Jung Seyoon (SuwonRockman)</i>
</div>
