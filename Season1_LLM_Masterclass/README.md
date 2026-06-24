# 🚀 Season 1: LLM Masterclass (From Scratch to Agent)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](#)
[![Framework: PyTorch](https://img.shields.io/badge/Framework-PyTorch-ee4c2c.svg)](#)

> **"What I cannot create, I do not understand."** - Richard Feynman
> (내가 직접 만들 수 없는 것은, 내가 온전히 이해한 것이 아니다.)

이 마스터클래스는 단순히 HuggingFace 라이브러리의 함수를 호출하는 튜토리얼이 아닙니다. 
언어 모델의 가장 밑바닥인 단어 벡터(Word2Vec)부터 시작해 트랜스포머의 심장(Attention), 파라미터 최적화(LoRA), 윤리 학습(RLHF), 그리고 최상위 자율형 에이전트(Agent) 아키텍처까지 **수학적 이론과 텐서(Tensor) 파이토치 코드로 직접 증명하며 올라가는 13단계의 풀스택 딥러닝 퀘스트**입니다.

[English Version 🇺🇸](./README_EN.md)

---

## 🗺️ 13단계 커리큘럼 로드맵 (Curriculum Roadmap)

각 폴더의 링크를 클릭하여 해당 단계의 `01_theory.md`와 `02_algorithm_from_scratch.ipynb`를 확인해 보세요!

### 🧱 Phase 1: Foundation (언어의 수학적 변환)
모델이 어떻게 인간의 언어를 숫자로 이해하고 압축하는지 배웁니다.
*   **Step 01. [Embeddings Basics](./embeddings-basics/)**
    *   Word2Vec, Negative Sampling 로스 함수 밑바닥 구현, 벡터 공간에서의 산술 연산 (`King - Man + Woman = Queen`)
*   **Step 02. [Tokenization](./tokenization/)**
    *   Subword 토큰화의 핵심: BPE(Byte-Pair Encoding) 트리 병합 알고리즘 구현 및 압축률 증명

### 🏗️ Phase 2: Architecture (딥러닝 뼈대의 진화)
순차 데이터(Sequence) 처리의 한계를 극복하며 트랜스포머 시대로 넘어가는 역사를 텐서로 추적합니다.
*   **Step 03. [RNN & Seq2Seq](./rnn-seq2seq/)**
    *   BPTT(시간 역전파)에서의 기울기 소실 증명, LSTM의 3대 게이트 로직 파이토치 수동 구현
*   **Step 04. [Attention Mechanism](./attention-mechanism/)**
    *   시계열 병목(Bottleneck)을 파괴한 닷-프로덕트(Dot-product) 어텐션 행렬 연산 구현
*   **Step 05. [Transformer Architecture](./transformer-architecture/)**
    *   자연어 처리의 패러다임 전환: Self-Attention, Multi-head 메커니즘, Positional Encoding

### 🧠 Phase 3: Scaling & Optimization (거대 모델과 튜닝)
수백억 파라미터 시대의 모델 구조와, 이를 일반 GPU에서 훈련하기 위한 최적화 마법을 다룹니다.
*   **Step 06. [Pretrained Language Models](./pretrained-language-models/)**
    *   인코더(BERT, MLM) vs 디코더(GPT, Causal LM)의 구조적 차이와 양방향 마스킹 시뮬레이션
*   **Step 07. [LLM Optimization (LoRA)](./llm-optimization-lora/)**
    *   VRAM 폭발을 막는 거대 행렬 분해(Rank Decomposition)와 PEFT(파라미터 효율적 파인튜닝) 증명

### 🤖 Phase 4: 실전 애플리케이션 및 자율화 (Production & Agents)
LLM을 실제 비즈니스 환경에 배포하고, 스스로 판단하여 행동하는 완전 자율형 시스템으로 진화시킵니다.
*   **Step 08: [AI Alignment (RLHF & DPO)](./llm-alignment-rlhf/)**
    *   인간 선호도를 학습하는 보상 모델(Bradley-Terry) 로스 구현 및 DPO(직접 선호도 최적화) 알고리즘
*   **Step 09: [Advanced RAG System](./advanced-rag-hnsw/)** 
    *   단순한 검색을 넘어선 HNSW 기반의 고성능 벡터 데이터베이스 직접 구현 및 환각(Hallucination) 방지 아키텍처.
*   **Step 10: [LLM Agentic Workflow](./llm-agentic-workflow/)** 
    *   ReAct 프롬프팅을 통한 추론(Thought) 및 도구 사용(Action) 파서 직접 구현, 자율 행동(Autonomous) 루프의 이해.

### 🏭 Phase 5: 산업 도메인 특화 비즈니스 솔루션 (Manufacturing AX)
앞선 10단계의 코어 기술을 '제조업(Manufacturing)'이라는 가장 거대한 B2B 도메인에 적용하여 비즈니스 가치(ROI)를 창출하는 엔터프라이즈 솔루션 라인업입니다.
*   **Step 11: [AX Factory Troubleshooting Agent](./ax-factory-agent/)** 
    *   RAG와 Agent 기술을 융합하여 공장 매뉴얼을 스스로 검색하고 설비 ERP(재고, 센서) 데이터와 연동해 정비 티켓을 발행하는 제조업 다운타임 방어 AI.
*   **Step 12: [AX Data Analyst Agent (Code Interpreter)](./ax-data-analyst-agent/)** 
    *   사내 관계형 DB(SQLite) 환경에서, 에이전트가 스스로 **Text-to-SQL 쿼리를 작성하고 파이썬 시각화 코드를 실행(exec) 및 자가 디버깅(Self-Correction)** 하는 최상위 비즈니스 인텔리전스(BI) 자율 분석 에이전트.

### 🚀 Phase 6: Enterprise LLMOps (배포 및 운영 자동화)
실험실의 주피터 노트북을 실제 기업의 프로덕션(Production) 서버로 승격시키는 엔지니어링 파이프라인입니다.
*   **Step 13: [Enterprise LLMOps CI/CD Pipeline](./llmops-agent-deployment/)** 
    *   완성된 에이전트를 **FastAPI** 기반의 마이크로서비스로 분리하고, **Docker** 컨테이너화하여 인프라 독립성을 확보합니다. 또한 **GitHub Actions**를 통해 코드 푸시 시 자동으로 단위 테스트(Pytest)와 도커 빌드를 수행하는 CI/CD 파이프라인을 구축하여 엔터프라이즈급 신뢰성을 증명합니다.

---

## 🤝 기여하기 (Contributing)
참여 방법은 [CONTRIBUTING.md](./CONTRIBUTING.md)를 참고해 주세요.
