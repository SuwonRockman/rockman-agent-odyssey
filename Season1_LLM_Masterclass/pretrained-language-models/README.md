# 🤖 사전 학습된 언어 모델: BERT & GPT의 분화

[![Generated](https://img.shields.io/badge/Date-2026.06.16-blue.svg)](#) [![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red.svg)](#)

> [!NOTE]
> **핵심 질문:** 구글의 'BERT'와 오픈AI의 'GPT'는 둘 다 트랜스포머에서 출발했지만 완전히 다른 길을 걸었습니다. 어떤 구조적 차이가 이 둘의 운명(이해 vs 생성)을 갈라놓았을까요?

---

## 📌 배경: 트랜스포머의 두 얼굴 (Encoder vs Decoder)

원래 트랜스포머 모델(2017)은 기계 번역을 위해 만들어졌으며, 두 파트로 나뉩니다.
1. **인코더(Encoder):** 전체 문장을 한 번에 읽고 문맥을 깊게 이해하는 역할
2. **디코더(Decoder):** 앞서 생성된 단어들을 바탕으로 다음 단어를 하나씩 생성하는 역할

이후 학계는 굳이 두 파트를 다 쓸 필요 없이, 목적에 맞게 한쪽 파트만 극대화하여 거대한 모델을 만들기로 결심합니다. 이것이 바로 **Pre-trained Language Models (PLM)**의 시작입니다.

---

## 🟦 진영 1: 인코더(Encoder)의 극한, BERT

**BERT (Bidirectional Encoder Representations from Transformers)**는 구글이 2018년에 발표한 모델로, 트랜스포머의 인코더 부분만을 쌓아 올린 구조입니다.

### 핵심 메커니즘: 양방향(Bidirectional)과 빈칸 채우기(MLM)
BERT는 텍스트를 읽을 때 과거 단어뿐만 아니라 미래 단어까지 전체 문맥을 **양방향**으로 동시에 바라봅니다. 
이를 학습시키기 위해 구글은 **MLM (Masked Language Modeling)**이라는 천재적인 방법을 고안했습니다.

*   입력 문장의 단어 중 15%를 무작위로 `[MASK]` 처리하여 가려버립니다.
*   **예시:** "나는 오늘 점심으로 `[MASK]`를 먹어서 배가 부르다."
*   모델은 앞뒤 문맥("점심으로", "먹어서 배가 부르다")을 모두 고려하여 `[MASK]`에 들어갈 단어가 '피자'인지 '햄버거'인지 맞추는 훈련을 수억 번 반복합니다.

### 강점 (NLU - 자연어 이해)
양방향 문맥을 완벽히 파악하기 때문에, 텍스트 분류, 감성 분석, 개체명 인식, 기계 독해(QA) 등 **텍스트의 의미를 이해하고 판단**하는 작업에서 압도적인 성능을 냅니다.

---

## 🟧 진영 2: 디코더(Decoder)의 극한, GPT

**GPT (Generative Pre-trained Transformer)**는 OpenAI가 발표한 모델로, 트랜스포머의 디코더 부분만을 쌓아 올린 구조입니다.

### 핵심 메커니즘: 단방향(Unidirectional)과 다음 단어 예측(CLM)
GPT는 미래를 보지 못합니다. 철저하게 **왼쪽에서 오른쪽으로(단방향)** 읽어나가며, 오직 과거의 단어들만을 단서로 삼아 **다음에 올 단어를 예측 (Causal Language Modeling)**합니다.

*   이를 위해 미래의 단어를 컨닝하지 못하게 가리는 **Causal Masking (하삼각행렬)** 기법을 필수로 사용합니다.
*   **예시:** "나는 오늘 점심으로" ➔ 모델은 다음에 올 단어 "피자를"을 예측함.
*   자신이 방금 내뱉은 단어를 다시 입력으로 집어넣어 끊임없이 이어가는 **자기 회귀(Autoregressive)** 특성을 가집니다.

### 강점 (NLG - 자연어 생성)
상상력이 풍부하여 소설 쓰기, 코드 작성, 챗봇 대화 등 **새로운 텍스트를 끝없이 생성해 내는 작업**에서 인류 역사상 최고의 성능을 자랑하게 되었습니다. (현재의 ChatGPT가 바로 이 구조입니다.)

---

## 📊 요약: BERT vs GPT 비교

| 특징 | BERT (구글) | GPT (OpenAI) |
| :--- | :--- | :--- |
| **기반 아키텍처** | Transformer **Encoder** | Transformer **Decoder** |
| **문맥 파악 방향** | 양방향 (Bidirectional) | 단방향 (Unidirectional, Left-to-Right) |
| **학습 방법** | 빈칸 채우기 (Masked Language Modeling) | 다음 단어 예측 (Causal Language Modeling) |
| **특징적 기법** | `[MASK]` 토큰 치환 | Causal Masking (미래 컨닝 방지) |
| **주요 강점 분야** | 자연어 이해 (분류, 평가, 독해) | 자연어 생성 (작문, 번역, 대화) |

---

## 🗂️ 프로젝트 구조 (Contents)

본 레포지토리에서는 BERT의 마스킹 전처리와 GPT의 자기 회귀 생성 루프를 직접 구현해 봅니다.

*   **`01_theory.md`**: 트랜스포머의 분화, BERT(MLM)와 GPT(Causal LM) 이론 비교 심화
*   **`02_algorithm_from_scratch.ipynb`**: GPT의 Causal Mask 시각화 및 Autoregressive 생성 루프 구현, BERT의 `[MASK]` 토큰 치환기 코딩
*   **`03_advanced_practice.ipynb`**: HuggingFace를 이용한 실제 소형 BERT(감성 분석) 튜닝 및 GPT-2 텍스트 생성 테스트 파이프라인

---
<div align="right">
  <b>GitHub:</b> <a href="https://github.com/SuwonRockman/pretrained-language-models">SuwonRockman/pretrained-language-models</a>
</div>