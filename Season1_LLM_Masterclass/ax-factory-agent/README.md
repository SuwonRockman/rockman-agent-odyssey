# 🏭 AX-Factory-Agent: 제조업 다운타임 최소화를 위한 자율형 AI 에이전트

[![Generated](https://img.shields.io/badge/Date-2026.06.17-blue.svg)](#) [![Domain](https://img.shields.io/badge/Domain-Manufacturing_AX-green.svg)](#)

> [!NOTE]
> **비즈니스 문제(Pain Point):** 공장 설비가 에러 코드를 뿜으며 정지했을 때, 작업자가 수천 페이지의 매뉴얼을 뒤지고 부품 재고를 확인하느라 허비하는 시간(Downtime)은 시간당 수억 원의 손실을 낳습니다.

본 프로젝트는 LLM 기반의 **RAG(검색 증강 생성)** 기술과 **Agentic Workflow(자율 행동 에이전트)**를 결합하여, 현장의 에러를 0.1초 만에 진단하고 ➔ 재고를 조회하며 ➔ 정비 티켓을 자동 발행하는 **B2B 엔터프라이즈 AX 솔루션**입니다.

---

## 📌 비즈니스 기대 효과 (ROI)
1. **Downtime 혁신적 단축:** 매뉴얼 검색 및 트러블슈팅 시간 80% 단축.
2. **지식 자산화 (Knowledge Transfer):** 퇴직을 앞둔 숙련공의 노하우(정비 일지)를 벡터 데이터베이스화하여 주니어 엔지니어도 즉각 활용 가능.
3. **ERP 자동화:** 에이전트가 재고 조회 및 발주(Work Order) API를 스스로 호출하여 백오피스 업무 완전 자동화.

---

## ⚙️ 시스템 아키텍처 (RAG + Agent Multi-Tools)
이 시스템은 단순한 챗봇이 아니라, 사내 시스템과 연동되어 능동적으로 행동하는 **소프트웨어 로봇**입니다.

1.  **Brain:** 언어 모델(LLM)이 현장 작업자의 거친 질문("3번 기계 E-04 원인이 뭐야?")을 논리적으로 분석합니다.
2.  **Tool 1 (RAG):** `search_manual()` 함수를 호출하여 `FAISS` 벡터 DB에 저장된 PDF 매뉴얼과 정비 일지에서 해결책을 찾습니다.
3.  **Tool 2 (ERP 연동):** 해결책에 '서보 모터 교체'가 있다면, 에이전트는 스스로 `check_inventory("servo_motor")`를 호출하여 창고 재고를 묻습니다.
4.  **Tool 3 (Ticketing):** 재고가 확인되면 `issue_work_order()`를 호출하여 정비 부서에 수리 지시서를 자동으로 전송합니다.

---

## 🗂️ 프로젝트 구조 (Contents)

단순한 AI 모델 학습을 넘어, **데이터-검색-행동-응답**으로 이어지는 실제 비즈니스 솔루션 파이프라인을 구축합니다.

*   **`01_business_and_architecture.md`**: 제조업 현장의 딥러닝/LLM 도입 시 보안 문제 및 AX 기획 관점 상세 리뷰
*   **`data/`**: 가상의 CNC 공작 기계 매뉴얼 및 과거 정비 일지 데이터셋
*   **`tools.py`**: 에이전트가 호출할 사내 가상 API 함수 모음
*   **`notebook/02_factory_rag_pipeline.ipynb`**: 공장 매뉴얼 텍스트를 임베딩하고 FAISS 벡터 DB에 적재하는 파이프라인
*   **`notebook/03_factory_agent_workflow.ipynb`**: RAG 검색과 사내 API(Tools)를 융합하여 스스로 판단하고 티켓을 발행하는 자율형 ReAct 엔진

---
<div align="right">
  <b>GitHub:</b> <a href="https://github.com/SuwonRockman/ax-factory-agent">SuwonRockman/ax-factory-agent</a>
</div>
