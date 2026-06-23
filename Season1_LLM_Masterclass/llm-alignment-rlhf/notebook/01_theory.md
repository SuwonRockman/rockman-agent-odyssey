# ⚖️ 얼라인먼트 튜닝: RLHF와 DPO의 수학적 심층 분석

## 📌 1. Base Model과 Instruct Model
인터넷 문서를 긁어모아 만든 대형 언어 모델(Base Model)은 오직 **"다음 단어 예측(Next Token Prediction)"**만 할 줄 압니다.
*   **프롬프트:** "프랑스의 수도는"
*   **Base Model의 출력:** "영국의 수도는 런던이고, 일본의 수도는 도쿄이다." (그냥 인터넷 위키백과 패턴을 이어감)
*   **Instruct Model의 출력:** "프랑스의 수도는 파리입니다." (질문에 대답을 함)

이렇게 모델의 행동 양식을 인간이 원하는 의도(Helpful, Honest, Harmless)에 맞게 교정하는 과정을 **얼라인먼트(Alignment)**라고 부릅니다.

---

## 🧠 2. RLHF (Reinforcement Learning from Human Feedback)의 3단계
OpenAI의 InstructGPT 논문에서 제시된 표준 파이프라인입니다.

1. **SFT (Supervised Fine-Tuning):** 사람이 직접 프롬프트와 정답을 정성껏 작성하여 모델에게 기본 말투를 가르칩니다. (비용이 매우 비쌈)
2. **RM (Reward Model, 보상 모델) 훈련:** 모델이 내뱉은 2개의 답변(A, B)을 사람에게 보여주고, "A가 B보다 낫다"고 채점(Ranking)합니다. 이를 통해 인간의 선호도를 수치화(Score)하는 별도의 심판 모델을 훈련합니다.
3. **PPO (Proximal Policy Optimization) 강화학습:** 원래의 모델(Policy)이 텍스트를 생성하면, 보상 모델(RM)이 점수를 매깁니다. 점수가 높으면 그 문장 패턴을 칭찬(Reward)하고, 낮으면 벌을 줍니다. 이를 수만 번 반복합니다.

> [!WARNING]
> **PPO의 치명적 단점:**
> Actor 모델, Critic 모델, Reward 모델, Reference 모델 등 총 4개의 거대 모델을 동시에 GPU 메모리에 올려야 하므로 일반적인 서버 환경에서는 OOM(Out of Memory)이 발생하여 학습이 거의 불가능합니다.

---

## 🚀 3. 혁신: DPO (Direct Preference Optimization)
2023년 스탠퍼드 대학교에서 발표한 DPO는 복잡하고 불안정한 3단계 강화학습(PPO)과 별도의 보상 모델(RM)을 완전히 없애버린 혁명적인 수식입니다.

### 💡 DPO의 핵심 수학적 치환 (Bradley-Terry 모델 우회)
원래 RLHF는 인간이 선호하는 응답($y_w$)과 버리는 응답($y_l$)에 대해 다음 Loss로 보상 모델 $r$을 학습시킵니다.
$$ L_{RM} = -\log \sigma(r(x, y_w) - r(x, y_l)) $$

DPO 연구진은 보상(Reward) $r(x,y)$를 **"현재 학습 중인 모델의 확률($\pi_{\theta}$)과 원본 모델의 확률($\pi_{ref}$)의 비율"**로 수학적으로 치환해버렸습니다.
$$ r(x, y) = \beta \log \frac{\pi_\theta(y|x)}{\pi_{ref}(y|x)} $$

이 수식을 위의 Loss에 대입하면, **별도의 보상 모델(RM) 없이도 언어 모델 자체가 보상 모델의 역할을 겸하며 직접 선호도를 학습**하게 됩니다!

$$ L_{DPO} = -\log \sigma \left( \beta \log \frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)} - \beta \log \frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)} \right) $$

이 수식 하나로 인해 메모리 사용량이 절반으로 줄어들고 파인튜닝이 압도적으로 쉬워지면서, 현재 Llama 3 등 거의 모든 오픈소스 진영이 RLHF 대신 DPO를 사용하여 모델을 튜닝하고 있습니다.
