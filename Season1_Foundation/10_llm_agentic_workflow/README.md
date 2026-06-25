# 🤖 자율형 AI 에이전트: Agentic Workflow & Tool Use

[![Generated](https://img.shields.io/badge/Date-2026.06.17-blue.svg)](#) [![Difficulty](https://img.shields.io/badge/Difficulty-Expert-purple.svg)](#)

> [!NOTE]
> **핵심 질문:** 언어 모델은 어떻게 텍스트 대답만 하는 것을 넘어, 스스로 계산기를 두드리고 인터넷 검색을 하며 외부 API를 호출하는 "자율형 소프트웨어(Agent)"로 진화했을까요?

이 레포지토리는 언어 모델을 단순한 챗봇이 아니라 시스템의 "컨트롤러(두뇌)"로 사용하는 **Agentic Workflow**와, 모델이 외부 도구를 다루게 해주는 **Function Calling (도구 사용)** 알고리즘을 밑바닥부터 파헤칩니다.

---

## 📌 배경: 텍스트 생성기에서 Agent로의 진화

지금까지 배운 트랜스포머, RLHF, RAG는 모두 훌륭하지만 여전히 **수동적인(Passive)** 시스템입니다. 사용자가 질문을 던져야만 검색을 하고 답을 내놓습니다.
하지만 최근의 AI는 다음과 같은 파이프라인을 스스로 구동하는 **자율형 에이전트(Autonomous Agent)**로 진화했습니다.

*   **Brain (두뇌):** LLM이 논리적 추론(Reasoning)을 담당하며 계획을 세웁니다.
*   **Memory (기억):** 프롬프트 체인을 통해 과거의 실패와 성공 기록을 유지합니다.
*   **Tools (도구):** LLM이 파이썬 코드를 실행하거나 날씨 API를 호출할 수 있게 해줍니다.

---

## 🛠️ ReAct (Reasoning and Acting) 프레임워크

에이전트를 구동하는 가장 핵심적인 알고리즘 패턴입니다. 모델은 정답을 내놓기 전, 반드시 다음 세 가지 스텝을 순환(Loop)합니다.

1.  **Thought (생각):** "사용자가 123 곱하기 456을 물어봤다. 나는 언어 모델이라 계산에 약하니 계산기 도구를 써야겠다."
2.  **Action (행동):** `calculator(123, 456)` 함수 호출.
3.  **Observation (관찰):** 파이썬 함수가 `56088` 이라는 결과를 리턴하면, 이를 프롬프트에 다시 주입받아 관찰.
*   ➔ **결과 도출:** "관찰 결과를 보니 56088이네. 사용자에게 알려주자."

---

## 🚀 Function Calling: 언어 모델과 API의 결합

언어 모델은 자연어("사과", "안녕")를 출력하도록 훈련되었습니다. 그러나 외부 프로그램을 실행하려면 엄격한 형식(JSON)의 인자(Arguments)가 필요합니다.
최신 에이전트 모델들은 사용자에게 대답을 하기 전, **"현재 제공된 도구(함수)들의 JSON 스키마를 읽어보고, 도구를 써야 할 상황이라면 사람에게 대답하는 대신 함수명과 JSON 인자를 출력하도록"** 특별히 파인튜닝(SFT) 되어 있습니다.

---

## 🗂️ 프로젝트 구조 (Contents)

LangChain이나 LlamaIndex 같은 프레임워크의 블랙박스에 의존하지 않고, 파이썬 While 루프와 정규표현식을 사용해 에이전트 엔진을 직접 짜봅니다.

*   **`01_theory.md`**: Agent의 3요소 해부, ReAct 아키텍처 논리, 그리고 JSON 기반 Function Calling의 파이프라인 구조
*   **`02_algorithm_from_scratch.ipynb`**: 파이썬 `while` 루프와 텍스트 파싱을 사용하여, LLM이 '생각➔행동➔관찰'을 반복하다 정답을 내는 수동(Manual) ReAct 엔진 밑바닥 구현
*   **`03_advanced_practice.ipynb`**: OpenAI/HuggingFace 표준 JSON 스키마를 정의하고, 모델이 알아서 함수를 골라 연쇄적으로 호출하는 실전 상태 기계(State Machine) 시뮬레이션

---
<div align="right">
  <b>GitHub:</b> <a href="https://github.com/SuwonRockman/10_llm_agentic_workflow">SuwonRockman/10_llm_agentic_workflow</a>
</div>
