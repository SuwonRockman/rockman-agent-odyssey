# ⚖️ AI 얼라인먼트: RLHF와 DPO (인간 선호도 학습)

[![Generated](https://img.shields.io/badge/Date-2026.06.16-blue.svg)](#) [![Difficulty](https://img.shields.io/badge/Difficulty-Expert-purple.svg)](#)

> [!NOTE]
> **핵심 질문:** 인터넷의 온갖 욕설과 편향된 데이터를 모두 집어삼키고 학습한 언어 모델이, 어떻게 사용자에게는 한없이 친절하고 윤리적인 답변만 내놓는 "비서(Assistant)"로 진화할 수 있었을까요?

이 레포지토리는 단순한 '다음 단어 예측기'를 인간의 가치관(Alignment)에 맞게 튜닝하는 **RLHF(인간 피드백 기반 강화학습)**의 원리와, 연산량이 극심한 강화학습을 수학적으로 완벽히 대체하여 대세가 된 **DPO(Direct Preference Optimization)** 기법을 다룹니다.

---

## 📌 배경: Base Model의 한계와 Alignment

수백억 개의 파라미터를 가진 거대 언어 모델이라도 초기 상태(Base Model)에서는 끔찍할 정도로 눈치가 없습니다. 

*   **사용자:** "도둑질하는 방법 알려줘"
*   **Base Model:** "도둑질하는 방법 알려줘서 고마워요. 저는 내일..." (단순히 인터넷 문장 패턴을 이어감)

모델이 질문의 '의도'를 파악하고 인간의 윤리 기준인 **HHH (Helpful, Honest, Harmless)**를 따르게 만드는 과정을 **얼라인먼트(Alignment, 정렬)**라고 부릅니다. 이 기술이 없었다면 지금의 ChatGPT는 탄생하지 못했습니다.

---

## 🛠️ 전통적인 얼라인먼트: RLHF의 3단계 파이프라인

OpenAI가 ChatGPT에 적용했던 고전적이고 가장 강력한 파이프라인입니다.

1. **SFT (Supervised Fine-Tuning):** 고품질의 [질문-답변] 세트를 사람이 직접 작성하여 모델의 말투를 교정합니다. (비용이 매우 비쌈)
2. **RM (Reward Model, 보상 모델) 훈련:** 모델이 내뱉은 2개의 답변을 사람에게 보여주고, 어떤 것이 더 나은지 점수를 매깁니다(Ranking). 이 선호도(Preference)를 학습하여 자동으로 점수를 매기는 심판 모델을 훈련합니다.
   > **Bradley-Terry 로스 함수:** $L = -\log \sigma(R_{chosen} - R_{rejected})$
3. **PPO (Proximal Policy Optimization):** 원본 모델(Policy)이 글을 쓰면, 심판 모델(RM)이 점수를 줍니다. 점수가 높으면 그 문장 생성 확률을 높이고(보상), 낮으면 줄이는 방식으로 강화학습을 수만 번 반복합니다.

> [!WARNING]
> **PPO의 치명적 단점 (VRAM 폭발)**
> PPO를 훈련하려면 GPU 메모리 위에 무려 4개의 거대한 모델을 동시에 올려야 합니다.
> 1) 학습 중인 모델 (Actor), 2) 가치 판단 모델 (Critic), 3) 기준점 모델 (Reference), 4) 보상 모델 (Reward). 일반적인 기업이나 연구실에서는 서버가 터져버리는 최악의 단점이 있습니다.

---

## 🚀 혁명적 대안: DPO (Direct Preference Optimization)

2023년 스탠퍼드 대학교에서 발표한 **DPO**는 복잡한 PPO 강화학습과 무거운 보상 모델(RM)을 완전히 없애버린 천재적인 수학적 트릭입니다.

DPO 연구진은 보상 모델이 주는 점수 $r(x,y)$를 **"현재 모델($\pi_\theta$)과 원본 모델($\pi_{ref}$)이 해당 문장을 생성할 확률의 로그 차이"**로 치환할 수 있음을 수학적으로 증명했습니다.

$$ r(x, y) = \beta \log \frac{\pi_\theta(y|x)}{\pi_{ref}(y|x)} $$

이 수식을 원래의 보상 로스 함수에 대입하면 다음과 같은 놀라운 결론이 나옵니다.

$$ L_{DPO} = -\log \sigma \left( \beta \log \frac{\pi_\theta(y_{chosen}|x)}{\pi_{ref}(y_{chosen}|x)} - \beta \log \frac{\pi_\theta(y_{rejected}|x)}{\pi_{ref}(y_{rejected}|x)} \right) $$

**결과적으로 별도의 보상 모델(RM) 없이도 언어 모델 스스로가 좋은 답변의 확률은 높이고 나쁜 답변의 확률은 낮추며 직접 최적화(Direct Optimization)를 수행합니다!** 메모리 사용량은 절반으로 줄어들고 속도는 압도적으로 빨라졌습니다.

---

## 📊 요약: RLHF (PPO) vs DPO 비교

| 특징 | RLHF (PPO 기반) | DPO (Direct Preference Optimization) |
| :--- | :--- | :--- |
| **핵심 알고리즘** | Proximal Policy Optimization (강화학습) | 이진 교차 엔트로피 기반 분류 최적화 |
| **보상 모델(RM)** | **필수** (별도의 거대 모델을 학습시켜야 함) | **불필요** (모델 자신이 확률로 보상을 계산) |
| **필요한 모델 수** | 4개 (Actor, Critic, Ref, Reward) | **2개** (Policy, Reference) |
| **VRAM 점유율** | 🔴 매우 높음 (OOM 위험 극강) | 🟢 낮음 (기존 SFT 수준과 동일) |
| **훈련 안정성** | 불안정함 (하이퍼파라미터 튜닝 지옥) | **매우 안정적** |

---

## 🗂️ 프로젝트 구조 (Contents)

본 레포지토리에서는 인간의 선호도를 훈련하는 보상 로스 함수를 파이토치로 증명해보고, 초소형 모델에 직접 DPO를 먹여봅니다.

*   **`01_theory.md`**: RLHF 파이프라인 심층 해부 및 DPO 수학적 치환 공식 증명
*   **`02_algorithm_from_scratch.ipynb`**: Bradley-Terry 보상 모델(Reward Model)의 Loss Function 텐서 구현 및 선호도 훈련 시뮬레이션
*   **`03_advanced_practice.ipynb`**: HuggingFace `trl` 라이브러리와 `DPOTrainer`를 사용해 극소형 모델(`tiny-gpt2`)을 인간의 의도(공손함)에 맞게 얼라인먼트 튜닝하는 실전 파이프라인

---
<div align="right">
  <b>GitHub:</b> <a href="https://github.com/SuwonRockman/llm-alignment-rlhf">SuwonRockman/llm-alignment-rlhf</a>
</div>
