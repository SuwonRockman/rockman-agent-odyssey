# 🔄 순환 신경망과 Seq2Seq: 시계열 데이터의 장기 의존성 정복하기

[![Generated](https://img.shields.io/badge/Date-2026.06.16-blue.svg)](#) [![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red.svg)](#)

> [!NOTE]
> **핵심 질문:** 모델이 어떻게 "과거의 기억"을 품고 미래를 예측할까요? 문장이 길어질수록 과거의 기억이 왜 희미해지며(기울기 소실), 이를 극복하기 위해 어떤 수학적 트릭(게이트 메커니즘)이 고안되었을까요?

이 레포지토리는 과거 언어 모델의 지배자였던 **RNN(Recurrent Neural Network)**의 역전파(BPTT) 수학과, 한계를 극복하기 위한 **LSTM**, 그리고 기계 번역의 혁신이었던 **Seq2Seq** 아키텍처를 심도 있게 다룹니다.

---

## 📂 목차 (Contents)

- **`01_theory.md`**: RNN의 BPTT(시간을 거슬러 올라가는 역전파) 수식 증명, 기울기 소실(Vanishing Gradient)의 자코비안 행렬 분석, LSTM의 3대 게이트(Forget, Input, Output) 수학적 해부
- **`02_algorithm_from_scratch.ipynb`**: 파이토치 내장 함수 없이 밑바닥부터 텐서 곱셈으로 Vanilla RNN Cell 구현, Teacher Forcing(교사 강요) 확률 제어 루프 시뮬레이션
- **`03_advanced_practice.ipynb`**: `nn.LSTM`을 활용한 Seq2Seq 기계 번역기 실전 구현 및 문장 길이에 따른 컨텍스트 벡터(Context Vector) 병목 현상 한계 테스트

---

## 🛠️ 기술 스택 (Tech Stack)
- Python
- PyTorch (Autograd & Matrix Multiplication)
- Math (Calculus, Linear Algebra)
- Jupyter Notebook

---
<div align="right">
  <b>GitHub:</b> <a href="https://github.com/SuwonRockman/rockman-agent-odyssey/tree/master/Season1_Foundation/03_rnn_seq2seq">SuwonRockman/03_rnn_seq2seq</a>
</div>
