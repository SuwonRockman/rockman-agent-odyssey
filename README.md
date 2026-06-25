# 🧠 LLM Masterclass Portfolio (From Foundation to Multi-Agent Systems)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](#)
[![Frameworks: PyTorch & Neo4j](https://img.shields.io/badge/Framework-PyTorch%20%7C%20Neo4j-0A84C6.svg)](#)

> **"What I cannot create, I do not understand."** - Richard Feynman
> (내가 직접 만들 수 없는 것은, 내가 온전히 이해한 것이 아니다.)

이 저장소는 언어 모델(LLM)의 기초 기초 수학 이론부터 시작하여 밑바닥 트랜스포머 구현, 파라미터 효율적인 미세조정(LoRA), 기업형 인지 검색망(GraphRAG), 그리고 자율 에이전트 협업 군집(Multi-Agent Swarm)까지 아우르는 **LLM 풀스택 전문가 포트폴리오** 저장소입니다.

---

## 🎯 주요 아키텍처 및 하이라이트

1. **밑바닥부터 구현하는 딥러닝 뼈대 (Scratch implementation)**: Word2Vec, 토크나이저 BPE, LSTM, Attention, Transformer 디코더/인코더 블록의 순수 PyTorch 구현.
2. **거대 모델 튜닝 및 정렬 (PEFT & Alignment)**: VRAM V100 환경에서의 LoRA 파인튜닝 수식 검증 및 RLHF 보상 모델(Bradley-Terry), DPO 손실 함수 수동 코딩.
3. **인지형 지식 검색 (Enterprise GraphRAG)**: 비정형 데이터 정제부터 Neo4j Cypher 연동 하이브리드 검색엔진 및 시각화 검색포털 빌드.
4. **실시간 스마트팩토리 자율 관제 (Multi-Agent Swarm)**: LangGraph 기반 예외 처리 분기 에이전트 군집 설계 및 FastAPI/Docker 패키징, 실시간 대시보드 구축.

---

## 🗺️ 커리큘럼 로드맵 (Curriculum Roadmap)

### 🧱 [Season 1: LLM Foundation & Agents](./Season1_Foundation/)
모델이 어떻게 인간의 언어를 숫자로 이해하고 압축하며, 자율적인 행동 주체로 거듭나는지 수학적 이론과 파이토치 텐서 코드로 직접 증명하며 올라가는 13단계의 풀스택 딥러닝 퀘스트입니다.

*   **Phase 1. Foundation**: [Embeddings Basics](./Season1_Foundation/01_embeddings_basics/), [Tokenization](./Season1_Foundation/02_tokenization/)
*   **Phase 2. Architecture**: [RNN & Seq2Seq](./Season1_Foundation/03_rnn_seq2seq/), [Attention Mechanism](./Season1_Foundation/04_attention_mechanism/), [Transformer Architecture](./Season1_Foundation/05_transformer_architecture/)
*   **Phase 3. Scaling & Optimization**: [Pretrained Language Models](./Season1_Foundation/06_pretrained_language_models/), [LLM Optimization (LoRA)](./Season1_Foundation/07_llm_optimization_lora/)
*   **Phase 4. Production & Agents**: [AI Alignment (RLHF & DPO)](./Season1_Foundation/08_llm_alignment_rlhf/), [Advanced RAG System](./Season1_Foundation/09_advanced_rag_hnsw/), [LLM Agentic Workflow](./Season1_Foundation/10_llm_agentic_workflow/)
*   **Phase 5. Manufacturing AX**: [AX Factory Agent](./Season1_Foundation/11_ax_factory_agent/), [AX Data Analyst Agent](./Season1_Foundation/12_ax_data_analyst_agent/)
*   **Phase 6. Enterprise LLMOps**: [Enterprise LLMOps CI/CD](./Season1_Foundation/13_llmops_agent_deployment/)

👉 **[Season 1 상세 커리큘럼 보기](./Season1_Foundation/README.md)**

---

### 🕸️ [Season 2: Enterprise GraphRAG Masterclass](./Season2_GraphRAG/)
비정형 기업 데이터를 단순한 벡터 검색으로 찾는 한계를 넘어, 데이터 간의 '논리적 관계(Relationship)'를 추출하여 거대한 사내 지식망을 구축하고 하이브리드 검색을 수행하는 5단계 풀스택 퀘스트입니다.

*   **Step 01. Advanced Data Parsing**: [Structural Ingest & Parsing](./Season2_GraphRAG/01_graphrag_data_parsing/)
*   **Step 02. Knowledge Graph Extraction**: [Entity & Relation Extraction](./Season2_GraphRAG/02_knowledge_graph_extraction/)
*   **Step 03. Neo4j Hybrid Search**: [Graph DB Integration & Hybrid Search](./Season2_GraphRAG/03_neo4j_hybrid_search/)
*   **Step 04. GraphRAG Web UI**: [Streamlit Visual Search Portal](./Season2_GraphRAG/04_graphrag_web_ui/)
*   **Step 05. Auto-Ingestion Pipeline**: [Auto Monitoring Ingestor](./Season2_GraphRAG/05_auto_ingestion_pipeline/)

👉 **[Season 2 상세 커리큘럼 보기](./Season2_GraphRAG/README.md)**

---

### 🤖 [Season 3: Autonomous AX Command Center](./Season3_MultiAgent_Swarm/)
LangGraph 멀티 에이전트 군집 기반 스마트팩토리 실시간 관제 및 예외 처리 자율 제어 시스템입니다. FastAPI 마이크로서비스 및 Streamlit 시각화 대시보드를 구축합니다.

*   **Core Systems**: FastAPI Service, Streamlit UI, SQLite/Neo4j Database
*   **Tech Stacks**: LangGraph, OpenAI, Pytest, Docker

👉 **[Season 3 상세 커리큘럼 보기](./Season3_MultiAgent_Swarm/README.md)**

---

## 🛠️ 기술 스택 (Tech Stack)

### Core AI & Data Science
* **DL & Agent Frameworks:** PyTorch, HuggingFace, LangGraph, LangChain
* **Vector & Graph DB:** FAISS, Neo4j, SQLite

### Infrastructure, Ops & Monitoring
* **LLMOps:** FastAPI, Docker, GitHub Actions, Pytest
* **Frontend & Visuals:** Streamlit, NetworkX, PyVis

---
<div align="center">
  <i>Created with ❤️ by Jung Seyoon (SuwonRockman)</i>
</div>
