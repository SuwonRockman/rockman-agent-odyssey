# 🚀 트랜스포머 아키텍처: 자연어 처리의 패러다임 전환

[![Generated](https://img.shields.io/badge/Date-2026.06.16-blue.svg)](#) [![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red.svg)](#)

> [!NOTE]
> **핵심 질문:** 수십 년간 언어 처리의 왕좌를 지켰던 RNN(순환 신경망)은 왜 몰락했을까요? 그리고 "Attention Is All You Need"라는 도발적인 논문 제목과 함께 등장한 트랜스포머는 어떻게 언어 모델의 유일한 표준이 되었을까요?

---

## 📌 배경: 기존 RNN/LSTM의 치명적 한계

트랜스포머 이전의 자연어 처리는 단어를 순차적으로 하나씩 읽어들이는 **RNN(Recurrent Neural Network)** 계열이 주도했습니다. 하지만 이 구조에는 두 가지 치명적인 문제가 있었습니다.

1. **병렬 처리 불가 (Sequential Bottleneck):** 단어를 1번부터 10번까지 순서대로 읽어야 하므로, 아무리 좋은 GPU를 써도 연산을 동시에(병렬로) 처리할 수 없어 학습 속도가 절망적으로 느렸습니다.
2. **장기 의존성 소실 (Long-Term Dependency):** 문장이 길어질수록 맨 처음에 읽었던 단어의 정보가 문장 끝에 도달할 때쯤이면 희미해지거나 소실되는 현상이 발생했습니다.

이러한 한계를 완벽하게 박살 낸 것이 바로 **트랜스포머(Transformer)** 아키텍처입니다.

---

## 🧠 핵심 혁신 1: Self-Attention (Q, K, V)

트랜스포머는 단어를 순서대로 읽는 대신, **문장 전체의 단어를 한 번에 통째로 쏟아붓고 각 단어들끼리 서로 얼마나 연관되어 있는지(Attention)를 동시에 계산**합니다.

이 과정은 우리가 도서관에서 책을 찾는 과정에 비유할 수 있습니다.
*   **Query (질의):** 현재 내가 집중하고 있는 단어 (예: "나는")
*   **Key (키):** 문장 내 다른 모든 단어들의 이름표 (예: "어제", "사과를", "먹었다")
*   **Value (값):** 그 단어들이 실제로 품고 있는 의미 정보

**계산 방식:** 내가 가진 Query와 다른 단어들의 Key를 내적(Dot-Product)하여 **관련성 점수(Attention Score)**를 구합니다. 이 점수가 높을수록 그 단어의 Value를 강하게 끌어당겨 내 의미를 풍부하게 만듭니다.

---

## 🧩 핵심 혁신 2: Multi-Head Attention

사람도 한 문장을 읽을 때 '누가 했는지(주어)', '언제 했는지(시간)', '어디서 했는지(장소)' 등 다양한 관점으로 문맥을 파악합니다.
트랜스포머 역시 하나의 거대한 어텐션만 수행하는 것이 아니라, 여러 개의 작은 어텐션 머리(Head)로 쪼개어 각기 다른 관점에서 단어 간의 관계를 파악합니다.

> [!TIP]
> **Multi-Head의 장점:** "The animal didn't cross the street because **it** was too tired." 라는 문장에서, 하나의 Head는 `it`이 `animal`을 가리킨다고 집중하고, 다른 Head는 `it`이 `tired`와 연관되어 있다고 집중하여 더욱 입체적인 문맥을 이해합니다.

---

## 📏 핵심 혁신 3: Positional Encoding

트랜스포머는 단어를 순서대로 읽지 않고 한 번에 통째로 입력받기 때문에, **"단어의 순서(어순)"** 개념을 상실합니다. "나 너 사랑해"와 "너 나 사랑해"를 똑같이 인식할 위험이 있습니다.

이를 해결하기 위해 각 단어의 벡터 값에 **위치 정보(주파수가 다른 사인/코사인 함수 값)**를 더해줍니다. 이것이 바로 **Positional Encoding**입니다. 이 수학적 마법 덕분에 모델은 단어들이 문장 내에서 어디에 위치하는지 절대적/상대적 위치를 깨닫게 됩니다.

---

## ⚠️ 트랜스포머의 아킬레스건: $O(N^2)$ 복잡도

트랜스포머가 완벽해 보이지만 치명적인 단점도 존재합니다.
문장 내의 모든 단어가 서로 다른 모든 단어와 한 번씩 관계(Attention)를 계산해야 하기 때문입니다.

*   10개의 단어 ➔ $10 \times 10 = 100$번의 계산
*   10,000개의 단어 ➔ $10,000 \times 10,000 = 100,000,000$ (1억)번의 계산

> [!WARNING]
> 문장의 길이($N$)가 길어질수록 메모리와 연산량이 **제곱($N^2$)으로 폭증**합니다. 이를 해결하기 위해 최근 등장한 모델들이 바로 `Longformer`, `Mamba(SSM)` 등입니다.

---

## 🗂️ 프로젝트 구조 (Contents)

본 레포지토리에서는 위에서 설명한 수학적 기법들을 PyTorch를 이용해 밑바닥부터 텐서 연산으로 구현합니다.

*   **`01_theory.md`**: 트랜스포머의 한계와 Self-Attention 심층 수학
*   **`02_algorithm_from_scratch.ipynb`**: Q, K, V 행렬 곱셈, Softmax 어텐션 스코어 계산 및 Positional Encoding 파이토치 구현
*   **`03_advanced_practice.ipynb`**: HuggingFace 모델 연동, 어텐션 맵 시각화 및 $O(N^2)$ 병목 현상 벤치마크

---
<div align="right">
  <b>GitHub:</b> <a href="https://github.com/SuwonRockman/transformer-architecture">SuwonRockman/transformer-architecture</a>
</div>