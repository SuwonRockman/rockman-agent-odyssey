# 🔄 시계열 모델의 수학적 심층 분석 (RNN, LSTM, Seq2Seq)

## 📌 1. BPTT (Backpropagation Through Time)와 기울기 소실
RNN은 이전 시간(t-1)의 은닉 상태(Hidden State)를 현재(t)로 전달합니다. 
수식으로 표현하면 $h_t = 	anh(W_{hh} h_{t-1} + W_{xh} x_t + b)$ 입니다.

이 모델을 학습시키려면 시간의 역순으로 미분 값을 계속 곱해나가야 합니다(BPTT).
시점 $t$에서의 손실 $L$을 과거 시점 $k$의 가중치로 편미분하면 연쇄 법칙(Chain Rule)에 의해 다음과 같은 자코비안(Jacobian) 행렬의 연속적인 곱셈이 발생합니다.

$$ \frac{\partial L_t}{\partial W_{hh}} = \sum_{k=1}^{t} \frac{\partial L_t}{\partial y_t} \frac{\partial y_t}{\partial h_t} \left( \prod_{j=k+1}^{t} \frac{\partial h_j}{\partial h_{j-1}} \right) \frac{\partial h_k}{\partial W_{hh}} $$

> [!WARNING]
> **Vanishing Gradient (기울기 소실) 증명**
> 위 수식에서 $\frac{\partial h_j}{\partial h_{j-1}} = W_{hh}^T \cdot \text{diag}(\tanh'(...))$ 입니다. 
> 만약 가중치 행렬 $W_{hh}$의 가장 큰 고윳값(Eigenvalue)이 1보다 작다면, 이 행렬을 계속해서 곱할수록(시퀀스가 길어질수록) 값은 기하급수적으로 0에 수렴합니다. 결국 시점 1의 단어 정보는 시점 100에 도달할 때 그래디언트가 소실되어 전혀 학습되지 않습니다.

---

## 🛡️ 2. 장기 기억의 보존: LSTM (Long Short-Term Memory)
기울기 소실을 막기 위해 1997년에 고안된 천재적인 구조가 LSTM입니다. RNN의 단순한 행렬 곱셈 대신 **정보를 얼마나 버리고(Forget), 얼마나 취할지(Input)를 결정하는 수학적 '게이트(Gate)'**를 도입했습니다.

1. **Forget Gate ($f_t$):** 과거 정보 $C_{t-1}$ 중 불필요한 것을 지우는 비율 ($0 \sim 1$ 사이의 시그모이드 함수)
   $$ f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f) $$
2. **Input Gate ($i_t$):** 현재의 새로운 정보 $\tilde{C}_t$ 중 얼마만큼을 기록할지 결정
   $$ i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i) $$
3. **Cell State ($C_t$): 핵심 컨베이어 벨트!** 덧셈(+) 연산으로만 정보가 흐르기 때문에 역전파 시 기울기가 곱해져서 소실되는 것을 막아줍니다.
   $$ C_t = f_t * C_{t-1} + i_t * \tilde{C}_t $$
4. **Output Gate ($o_t$):** 업데이트된 Cell State를 바탕으로 다음 층으로 보낼 은닉 상태($h_t$) 결정
   $$ o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o) $$

---

## 🌉 3. 기계 번역의 패러다임: Seq2Seq 아키텍처
입력 시퀀스(예: 한국어)를 출력 시퀀스(예: 영어)로 변환하는 모델입니다.

1. **Encoder:** 입력 문장을 모두 읽고, 문장의 모든 의미를 압축한 단 하나의 **고정 크기 컨텍스트 벡터(Fixed-size Context Vector)**를 만듭니다. (인코더의 마지막 Hidden State)
2. **Decoder:** 이 컨텍스트 벡터를 초기 상태로 전달받아, 종료 토큰 `<EOS>`가 나올 때까지 하나씩 단어를 생성합니다.

> [!CAUTION]
> **Seq2Seq의 치명적 한계 (병목 현상):**
> 아무리 긴 문장이라도 인코더는 반드시 '단 하나의 고정된 크기'의 벡터로 압축해야 합니다. 문장이 100단어가 넘어가면 정보가 넘쳐흘러 유실되는 병목(Bottleneck) 현상이 발생합니다. 이를 해결하기 위해 등장한 것이 바로 **'어텐션(Attention)'** 메커니즘입니다.
