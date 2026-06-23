# 트랜스포머 아키텍처 (Transformer Architecture)

![Date](https://img.shields.io/badge/Date-2026.06.16-blue) ![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

> [!NOTE]
> 핵심 질문: 시계열 데이터를 처리할 때, 왜 순차적으로 연산해야만 할까요? 한 번에 모든 단어를 병렬로 연산하면서 문맥을 이해할 수는 없을까요?

## 📌 배경: RNN과 Seq2Seq의 한계

기존의 순환 신경망(RNN)이나 이를 활용한 Seq2Seq 모델들은 문장을 처리할 때 **순차적 연산(Sequential Processing)**이 필수적이었습니다.
1. `I` 처리 후 $\rightarrow$ `love` 처리 $\rightarrow$ `you` 처리.
2. 이로 인해 GPU의 강력한 병렬 처리 능력을 제대로 활용하지 못합니다.
3. 시퀀스가 길어지면 여전히 기울기 소실(Vanishing Gradient)과 장기 의존성(Long-Term Dependency) 문제가 발생합니다.

이러한 문제를 해결하기 위해 구글 연구팀은 2017년 **"Attention Is All You Need"**라는 논문에서, RNN을 완전히 배제하고 오직 Attention 메커니즘만으로 문맥을 파악하는 아키텍처, **Transformer**를 제안했습니다.

---

## 🏗️ 1. 트랜스포머의 핵심 아이디어: Self-Attention

트랜스포머의 가장 중요한 혁신은 **Self-Attention (자기 주의 메커니즘)**입니다.
Seq2Seq에서의 어텐션은 "디코더가 인코더의 어떤 단어에 집중할까?"를 결정했다면, Self-Attention은 **"입력된 문장 내에서, 어떤 단어가 어떤 단어와 연관되어 있을까?"**를 스스로 찾아냅니다.

* 예: `"The animal didn't cross the street because it was too tired."`
* 이 문장에서 `it`이 `animal`인지 `street`인지 판단하기 위해, `it`이라는 단어는 문장 내의 모든 다른 단어들과 연관성을 계산(Attention Score)합니다. 이 때 `animal`에 가장 높은 가중치가 부여됩니다.

### Q, K, V 행렬
Self-Attention은 세 가지 가중치 행렬을 사용하여 입력 벡터에서 **Query(질의)**, **Key(키)**, **Value(값)** 벡터를 뽑아냅니다.
* **Query (Q):** 현재 포커스를 맞추고 있는 단어의 표현 (예: `it`)
* **Key (K):** 문장 내 모든 단어들이 가진 라벨 (예: `animal`, `street`)
* **Value (V):** 문장 내 모든 단어들이 가진 실제 의미값

어텐션 스코어는 $Q \cdot K^T$ 로 계산되며, 이를 $\sqrt{d_k}$ 로 나누어 스케일링한 후 Softmax를 취해 V와 곱합니다. (Scaled Dot-Product Attention)

---

## 🎭 2. Multi-Head Attention

하나의 어텐션만 사용하면 문맥의 다양한 의미(동음이의어, 문법적 관계, 의미적 관계 등)를 놓칠 수 있습니다. 
따라서 트랜스포머는 여러 개의 어텐션 헤드(Head)를 두어, 동일한 문장에 대해 **서로 다른 관점으로 관찰**합니다. 이를 **Multi-Head Attention**이라고 합니다.

---

## ⏱️ 3. 위치 정보 주입: Positional Encoding

트랜스포머는 RNN처럼 단어를 순서대로 입력받지 않고 **한꺼번에 병렬로 입력**받습니다.
따라서 모델은 단어의 순서(위치) 정보를 전혀 알지 못합니다. "I love you"와 "you love I"를 똑같이 인식할 수 있습니다.

이를 해결하기 위해, 입력 단어 임베딩에 **단어의 위치를 수학적으로 암호화한 벡터(Positional Encoding)**를 더해줍니다. 논문에서는 `sin`과 `cos` 함수의 주기를 활용하여 위치 벡터를 만듭니다.

---

## 🧱 4. 전체 구조 (Encoder & Decoder)

* **Encoder (인코더):** 입력 문장을 이해합니다. (Self-Attention + Feed Forward) $\times$ N개 층
* **Decoder (디코더):** 인코더의 출력(문맥)을 참조하여 출력 문장을 생성합니다. (Masked Self-Attention + Encoder-Decoder Attention + Feed Forward) $\times$ N개 층

다음 02번 알고리즘 실습 노트북에서, 이 부품들을 파이토치(PyTorch)로 하나씩 조립해 보겠습니다.
