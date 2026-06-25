# ⚡ LLM 최적화: 파라미터 효율적 파인튜닝 (PEFT & LoRA)

[![Generated](https://img.shields.io/badge/Date-2026.06.16-blue.svg)](#) [![Difficulty](https://img.shields.io/badge/Difficulty-Expert-purple.svg)](#)

> [!NOTE]
> **핵심 질문:** LLaMA-70B 같은 초거대 모델의 용량은 140GB가 넘습니다. 이런 모델을 파인튜닝하려면 H100 GPU 8대가 묶인 수천만 원짜리 서버가 필요한데, 스타트업이나 개인은 어떻게 거대 모델을 학습(Fine-Tuning)시킬 수 있을까요?

---

## 📌 배경: Full Fine-Tuning의 끔찍한 비용

사전 학습된 모델을 내 데이터(의료, 법률, 회사 규정 등)에 맞게 재학습하는 것을 **파인튜닝(Fine-tuning)**이라고 합니다.
과거에는 모델의 모든 가중치를 업데이트하는 **Full Fine-Tuning**이 표준이었습니다. 

하지만 매개변수(Parameter)가 수백억 개 단위로 넘어가면서 물리적인 한계에 부딪혔습니다.
1. **VRAM 폭발:** 모델의 가중치뿐만 아니라, 역전파 기울기(Gradients), 옵티마이저 상태(Adam Momentum 등)를 모두 그래픽카드 메모리에 올려야 하므로 원본 모델 크기의 **3~4배의 VRAM**이 필요합니다.
2. **저장 공간 낭비:** 파인튜닝 할 때마다 140GB짜리 새로운 모델 파일이 통째로 생성됩니다. 태스크가 10개면 1.4TB의 용량이 낭비됩니다.

이를 구원하기 위해 등장한 개념이 **PEFT (Parameter-Efficient Fine-Tuning)** 입니다.

---

## 💡 해결책: PEFT와 대세가 된 LoRA

**PEFT**는 원본 거대 모델의 가중치는 꽁꽁 얼려두고(Freeze, 학습 불가 상태), **아주 소량의 파라미터(어댑터)만 추가로 덧붙여서 그 부분만 학습**하는 모든 기술을 뜻합니다.
그중에서도 현재 업계 표준으로 완전히 자리 잡은 기술이 바로 2021년 마이크로소프트가 발표한 **LoRA(Low-Rank Adaptation)** 입니다.

### ✂️ LoRA의 핵심 원리: 거대 행렬 쪼개기 (Rank Decomposition)

어떤 거대한 가중치 행렬 $W$ (예: $10,000 \times 10,000$)가 학습을 통해 $\Delta W$만큼 변했다고 가정해 봅시다.
새로운 모델의 가중치는 $W + \Delta W$ 가 됩니다.

LoRA는 원래의 $W$는 얼려버리고, $\Delta W$를 직접 학습하는 대신 **두 개의 아주 작은 행렬 $A$와 $B$의 곱($BA$)으로 대체**해 버립니다.
이때 $A$와 $B$는 **랭크(Rank, $r$)**라는 아주 얇은 내부 차원을 가집니다. (보통 $r=8$ 또는 $16$)

*   **원본 모델 연산:** $h = Wx$
*   **LoRA 모델 연산:** $h = Wx + \Delta Wx = Wx + B(Ax)$

### 📉 메모리 절감 효과 체감하기

만약 $10,000 \times 10,000$ 차원의 가중치 행렬을 학습한다고 해봅시다.

<table style="width: 100%; display: table;">
  <thead>
    <tr>
      <th align="center" width="25%">방식</th>
      <th align="center" width="50%">연산식 / 행렬 크기</th>
      <th align="center" width="25%">학습 파라미터 수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><b>Full Fine-Tuning</b></td>
      <td align="center">$\Delta W$ (10000 × 10000) 행렬 전체 학습</td>
      <td align="center"><b>100,000,000 개 (1억)</b></td>
    </tr>
    <tr>
      <td align="center"><b>LoRA ($r=8$)</b></td>
      <td align="center">행렬 $A$ (10000 × 8) + 행렬 $B$ (8 × 10000) 학습</td>
      <td align="center"><b>160,000 개 (16만)</b></td>
    </tr>
  </tbody>
</table>

> [!TIP]
> **결론:** 파라미터가 1억 개에서 16만 개로 줄어들었습니다. 무려 **99.8% 이상의 파라미터 학습을 생략**하면서도 Full Fine-tuning과 거의 동일한 성능을 내는 기적을 보여줍니다!

---

## 🚀 현업에서의 활용: QLoRA

최근에는 LoRA에 **양자화(Quantization)** 기술을 결합한 **QLoRA**가 주로 쓰입니다.
얼려놓은 원본 가중치 $W$의 정밀도를 16-bit 부동소수점에서 4-bit 정수형으로 깎아내려 VRAM 점유율을 4분의 1로 극단적으로 압축한 뒤, 그 위에 LoRA 어댑터를 붙여 학습하는 방식입니다.
이 기술 덕분에 방구석의 RTX 3090 / 4090 (24GB) 1대만으로도 수백억 파라미터의 LLM을 파인튜닝할 수 있는 시대가 열렸습니다.

---

## 🗂️ 프로젝트 구조 (Contents)

본 레포지토리에서는 HuggingFace `peft` 라이브러리의 블랙박스를 걷어내고, 파이토치를 이용해 직접 행렬을 동결하고 A, B 행렬을 덧대어 파라미터를 계산하는 과정을 코드로 증명해 봅니다.

*   **`01_theory.md`**: Full Fine-Tuning의 메모리 한계와 LoRA의 행렬 분해 수학적 원리 (현재 문서와 연계)
*   **`02_algorithm_from_scratch.ipynb`**: PyTorch `nn.Linear`를 동결시키고 랭크 행렬을 구현하여, 파라미터 감소량을 코드로 직접 확인하는 실습
*   **`03_advanced_practice.ipynb`**: HuggingFace `peft`를 사용해 소형 모델에 `LoraConfig`를 씌우고 실제 Trainable Parameter 비율을 확인하는 파이프라인 경험

---
<div align="right">
  <b>GitHub:</b> <a href="https://github.com/SuwonRockman/07_llm_optimization_lora">SuwonRockman/07_llm_optimization_lora</a>
</div>