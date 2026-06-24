# 🚀 Season 1: LLM Foundation & Agents (From Scratch to Agent)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](#)
[![Framework: PyTorch](https://img.shields.io/badge/Framework-PyTorch-ee4c2c.svg)](#)

> **"What I cannot create, I do not understand."** - Richard Feynman
> (내가 직접 만들 수 없는 것은, 내가 온전히 이해한 것이 아니다.)

이 마스터클래스는 단순히 HuggingFace 라이브러리의 함수를 호출하는 튜토리얼이 아닙니다. 
언어 모델의 가장 밑바닥인 단어 벡터(Word2Vec)부터 시작해 트랜스포머의 심장(Attention), 파라미터 최적화(LoRA), 윤리 학습(RLHF), 그리고 최상위 자율형 에이전트(Agent) 아키텍처까지 **수학적 이론과 텐서(Tensor) 파이토치 코드로 직접 증명하며 올라가는 13단계의 풀스택 딥러닝 퀘스트**입니다.

[English Version 🇺🇸](./README_EN.md)

---

## 🗺️ 5단계 커리큘럼 로드맵 (Curriculum Roadmap)

각 폴더의 링크를 클릭하여 해당 단계의 `01_theory.md`와 `02_algorithm_from_scratch.ipynb`를 확인해 보세요!

### 🧱 Phase 1: NLP Foundation (언어의 수학적 변환)
모델이 어떻게 인간의 언어를 숫자로 이해하고 압축하는지 배웁니다.
*   **Step 01. [Embeddings Basics](./embeddings-basics/)**
    *   Word2Vec, Negative Sampling 로스 함수 밑바닥 구현, 벡터 공간에서의 산술 연산 (`King - Man + Woman = Queen`)
*   **Step 02. [Tokenization](./tokenization/)**
    *   Subword 토큰화의 핵심: BPE(Byte-Pair Encoding) 트리 병합 알고리즘 구현 및 압축률 증명

### 🏗️ Phase 2: Deep Learning & Attention (딥러닝 뼈대의 진화 및 사전학습)
순차 데이터(Sequence) 처리의 한계를 극복하며 트랜스포머 시대로 넘어가는 역사를 텐서로 추적합니다.
*   **Step 03. [RNN & Seq2Seq](./rnn-seq2seq/)**
    *   BPTT(시간 역전파)에서의 기울기 소실 증명, LSTM의 3대 게이트 로직 파이토치 수동 구현
*   **Step 04. [Attention Mechanism](./attention-mechanism/)**
    *   시계열 병목(Bottleneck)을 파괴한 닷-프로덕트(Dot-product) 어텐션 행렬 연산 구현
*   **Step 05. [Transformer Architecture](./transformer-architecture/)**
    *   자연어 처리의 패러다임 전환: Self-Attention, Multi-head 메커니즘, Positional Encoding
*   **Step 06. [Pretrained Language Models](./pretrained-language-models/)**
    *   인코더(BERT, MLM) vs 디코더(GPT, Causal LM)의 구조적 차이와 양방향 마스킹 시뮬레이션

### 🧠 Phase 3: Parameter-Efficient Tuning & Alignment (파인튜닝 및 인간 정렬)
일반 GPU 환경에서 거대 모델을 효율적으로 튜닝하고, 인간의 선호도에 맞춰 모델 행동을 정렬하는 기법을 배웁니다.
*   **Step 07. [LLM Optimization (LoRA)](./llm-optimization-lora/)**
    *   VRAM 폭발을 막는 거대 행렬 분해(Rank Decomposition)와 PEFT(파라미터 효율적 파인튜닝) 증명
*   **Step 08. [AI Alignment (RLHF & DPO)](./llm-alignment-rlhf/)**
    *   인간 선호도를 학습하는 보상 모델(Bradley-Terry) 로스 구현 및 DPO(직접 선호도 최적화) 알고리즘

### 🤖 Phase 4: Advanced Retrieval & Agents (검색 및 에이전틱 워크플로우)
LLM을 실제 지식 소스에 연결하고, 스스로 도구를 판단하고 실행하는 자율 시스템을 개발합니다.
*   **Step 09. [Advanced RAG System](./advanced-rag-hnsw/)** 
    *   단순한 검색을 넘어선 HNSW 기반의 고성능 벡터 데이터베이스 직접 구현 및 환각(Hallucination) 방지 아키텍처
*   **Step 10. [LLM Agentic Workflow](./llm-agentic-workflow/)** 
    *   ReAct 프롬프팅을 통한 추론(Thought) 및 도구 사용(Action) 파서 직접 구현, 자율 행동(Autonomous) 루프 설계

### 🏭 Phase 5: Domain Solutions & Production (산업용 에이전트 및 배포)
구현된 AI 엔진을 제조 도메인(BI 데이터 분석, 설비 장애 대응)에 적용하고 프로덕션 수준의 API 서버 및 배포 인프라를 구축합니다.
*   **Step 11. [AX Factory Troubleshooting Agent](./ax-factory-agent/)** 
    *   RAG와 Agent 기술을 융합하여 공장 매뉴얼을 스스로 검색하고 설비 ERP(재고, 센서) 데이터와 연동해 정비 티켓을 발행하는 제조업 다운타임 방어 AI
*   **Step 12. [AX Data Analyst Agent (Code Interpreter)](./ax-data-analyst-agent/)** 
    *   사내 관계형 DB(SQLite) 환경에서, 에이전트가 스스로 **Text-to-SQL 쿼리를 작성하고 파이썬 시각화 코드를 실행(exec) 및 자가 디버깅(Self-Correction)** 하는 BI 자율 분석 에이전트
*   **Step 13. [Enterprise LLMOps CI/CD Pipeline](./llmops-agent-deployment/)** 
    *   FastAPI 기반의 마이크로서비스 설계, Docker 컨테이너화, GitHub Actions를 통한 단위 테스트(Pytest)와 도커 빌드 자동화

---

## 🤝 기여하기 (Contributing)
참여 방법은 [CONTRIBUTING.md](./CONTRIBUTING.md)를 참고해 주세요.
