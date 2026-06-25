# 🤖 자율형 에이전트와 도구 사용 (Tool Use) 이론

## 📌 1. Agent의 3대 핵심 요소
LLM을 단순한 문장 생성기에서 "디지털 인턴"으로 격상시키려면 세 가지 구조가 결합되어야 합니다.
1. **Brain (두뇌):** 목표를 이해하고, 계획(Plan)을 세우고, 현재 상황을 추론(Reasoning)하는 거대 언어 모델(LLM).
2. **Memory (기억):**
   - *Short-term Memory:* 현재 진행 중인 작업의 대화 기록(Context Window).
   - *Long-term Memory:* 과거의 경험이나 지식을 벡터 DB(RAG) 등에 저장하고 꺼내어 쓰는 능력.
3. **Tools (도구):** 모델이 외부 세상과 상호작용할 수 있는 인터페이스. (웹 브라우저, 파이썬 REPL, 날씨 API, 사내 DB 접근 권한 등)

---

## 🔄 2. ReAct (Reasoning + Acting) 알고리즘 패턴
2022년 발표된 ReAct 논문은 에이전트의 교과서입니다. 모델이 행동하기 전에 반드시 **자신의 생각을 소리 내어 말하게(Chain of Thought)** 강제함으로써 성능을 극적으로 높였습니다.

*   **일반적인 LLM:**
    *   질문: "현재 미국 대통령의 나이는 몇 살인가요?"
    *   대답: "저는 2021년 데이터까지만 알아서 현재 대통령을 모릅니다." (또는 환각 발생)
*   **ReAct 프레임워크가 적용된 Agent LLM:**
    *   **Thought:** "현재 미국 대통령이 누군지 검색(Search) 도구를 통해 알아봐야겠다."
    *   **Action:** `Search("Current US President")`
    *   **Observation:** (외부 API 반환값) "조 바이든 (Joe Biden)"
    *   **Thought:** "조 바이든의 나이를 계산해야 하니, 그의 출생 연도를 검색하자."
    *   **Action:** `Search("Joe Biden birth year")`
    *   **Observation:** (외부 API 반환값) "1942년 11월 20일"
    *   **Thought:** "지금은 2026년이니, 2026 - 1942 연산을 계산기(Calculator) 도구에 넣자."
    *   **Action:** `Calculator("2026 - 1942")`
    *   **Observation:** (외부 API 반환값) "84"
    *   **Final Answer:** "현재 미국 대통령 조 바이든의 나이는 84세입니다."

---

## 🛠️ 3. Function Calling (도구 사용) 내부 구조
ReAct 루프에서 가장 중요한 것은 **모델이 '언제', '어떤 도구'를 '어떤 인자값'을 넣어 실행할지 결정**하는 것입니다. 이를 위해 개발자는 모델에게 도구 설명서(JSON Schema)를 프롬프트로 주입합니다.

```json
// 개발자가 모델에게 던져주는 도구 설명서
{
  "name": "get_weather",
  "description": "특정 지역의 현재 날씨를 가져옵니다.",
  "parameters": {
    "type": "object",
    "properties": {
      "location": { "type": "string", "description": "도시 이름 (예: Seoul, Tokyo)" }
    },
    "required": ["location"]
  }
}
```

모델은 이 스키마를 읽고, 질문이 들어오면 사람에게 대답하는 대신 다음과 같은 특별한 JSON 구조의 텍스트를 출력합니다.
`{"name": "get_weather", "arguments": {"location": "Seoul"}}`

소프트웨어 엔진(파이썬)은 모델의 이 응답을 가로채어 파싱한 뒤, 실제 파이썬 함수 `get_weather("Seoul")`을 실행합니다. 그 결과를 다시 텍스트로 바꿔 모델에게 "관찰(Observation)" 결과로 던져주는 무한 루프가 바로 에이전트의 실체입니다.
