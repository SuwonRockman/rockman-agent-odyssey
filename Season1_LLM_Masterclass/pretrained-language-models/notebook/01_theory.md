# Pre-trained Language Models: 트랜스포머의 두 갈래 길

![Date](https://img.shields.io/badge/Date-2026.06.16-blue) ![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

> [!NOTE]
> 핵심 질문: 트랜스포머 아키텍처는 인코더와 디코더로 구성되어 있습니다. 그렇다면 문맥을 이해하는 모델과 글을 생성하는 모델은 이 아키텍처를 어떻게 활용할까요?

## 📌 배경: 트랜스포머의 분화

트랜스포머가 자연어 처리의 패러다임을 바꾼 후, 연구자들은 이 아키텍처를 사전학습(Pre-training)에 활용하기 시작했습니다. 
이 과정에서 트랜스포머는 목적에 따라 두 가지 파생 모델로 갈라지게 됩니다.

1. **BERT (Encoder-Only):** 문맥을 양방향(Bidirectional)으로 이해하는 데 집중합니다.
2. **GPT (Decoder-Only):** 단방향(Unidirectional)으로 텍스트를 생성하는 데 집중합니다.

---

## 🧐 1. BERT: 문맥 이해의 일인자

**BERT(Bidirectional Encoder Representations from Transformers)**는 구글에서 발표한 모델로, 트랜스포머의 **인코더(Encoder)** 블록만을 겹겹이 쌓아 올린 구조입니다.

### 어떻게 학습하는가?
*   **Masked Language Modeling (MLM):** 문장 내 토큰의 15%를 무작위로 `[MASK]`로 가린 뒤, 주변의 모든 단어(앞/뒤)를 보고 빈칸을 맞추도록 학습합니다. (마치 빈칸 채우기 시험과 같습니다.)
*   **Next Sentence Prediction (NSP):** 두 문장이 이어지는 문장인지 아닌지 판별합니다.

### 특징 및 활용
*   문맥의 전체를 볼 수 있으므로(Bidirectional) 문장 분류(감성 분석), 개체명 인식(NER), 기계 독해(QA) 등 **자연어 이해(NLU)** 태스크에 압도적인 성능을 보입니다.
*   "Pre-training + Fine-tuning" 패러다임을 정착시켰습니다.

---

## ✍️ 2. GPT: 텍스트 생성의 절대강자

**GPT(Generative Pre-trained Transformer)**는 OpenAI에서 발표한 모델로, 트랜스포머의 **디코더(Decoder)** 블록만을 쌓아 올린 구조입니다.

### 어떻게 학습하는가?
*   **Causal Language Modeling (CLM):** 주어진 단어들의 시퀀스를 보고 **"다음 단어가 무엇일지"** 예측하는 방식으로 학습합니다.
*   **Causal Masking:** 이전 단어들만 보고 미래의 단어는 보지 못하게 차단(Masking)하는 하삼각행렬(Lower Triangular Matrix)을 사용합니다.

### 특징 및 활용
*   이전 토큰들만을 보고 다음 토큰을 생성하므로(Unidirectional), 대화형 AI, 문서 요약, 코드 생성 등 **자연어 생성(NLG)** 태스크에 강력합니다.
*   모델 크기가 커질수록 파인튜닝 없이 프롬프트(Prompt)만으로 다양한 작업을 수행하는 **Few-shot/Zero-shot Learning** 능력이 생깁니다. (Scaling Law)

---

## ⚖️ 요약 비교

| 특징 | BERT | GPT |
| :--- | :--- | :--- |
| **사용 블록** | 인코더 (Encoder) | 디코더 (Decoder) |
| **어텐션 방식** | Bidirectional (양방향) | Unidirectional / Causal (단방향) |
| **사전학습 목표** | MLM (빈칸 채우기) | CLM (다음 단어 예측) |
| **강점 분야** | 분류, 독해 (NLU) | 생성, 대화 (NLG) |

다음 02번 노트북에서는 이 두 모델의 심장과도 같은 **Masking 기법(MLM과 Causal Mask)**을 파이토치로 구현해 보겠습니다.
