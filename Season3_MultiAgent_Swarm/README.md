# ⚙️ Season 3: Autonomous AX Command Center (Multi-Agent Swarm)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Framework: LangGraph & Neo4j](https://img.shields.io/badge/Framework-LangGraph%20%7C%20Neo4j-0A84C6.svg)](#)

이 마스터클래스(Season 3)는 Season 1과 2의 핵심 기술을 집대성하여, 기업 내에서 각기 다른 데이터 포맷(CSV, GraphDB, SQL)을 다루는 여러 AI 에이전트들이 협업하는 **스마트팩토리 관제 센터(Command Center)**를 구축하고, 모델 및 데이터의 실시간 지표를 관리하는 MLOps 체계를 학습하는 최고난도 프로젝트입니다.

---

## 🎯 Architecture: Multi-Agent Swarm

우리의 가상 공장은 3명의 전문 에이전트와 1명의 총괄 감독관(Supervisor)으로 이루어집니다.

1. **🚨 이상 탐지 에이전트 (Monitor Agent)**
   *   **데이터:** 실시간 센서 로그 (`data/ai4i2020.csv`)
   *   **역할:** 설비의 온도, 토크, 진동 데이터를 분석하고 임계값 초과 시 경보 발송.
2. **🛠️ 정비 엔지니어 에이전트 (Engineer Agent)**
   *   **데이터:** 지식망 매뉴얼 (`data/cnc_manual.txt` ➡️ `Neo4j GraphRAG`)
   *   **역할:** 고장 부위를 전달받으면 매뉴얼에서 해결책과 필요 교체 부품을 검색하여 지시.
3. **📦 자재 관리 에이전트 (Supply Chain Agent)**
   *   **데이터:** 관계형 재고 DB (`data/inventory.sqlite`)
   *   **역할:** Text-to-SQL을 통해 부품 재고를 파악하고, 부족할 경우 공급사(Supplier)에 자동 발주 처리.
4. **👑 총괄 감독관 (Supervisor Agent)**
   *   **프레임워크:** `LangGraph` State Machine
   *   **역할:** 메시지를 분석하여 누구에게 일을 시킬지 결정하고 릴레이 협업(Workflow)을 지휘.

---

## 🗺️ 5단계 커리큘럼 로드맵 (Curriculum Roadmap)

### 🧱 Phase 1: Edge Sensor Data & Environment Setup (환경 셋업)
*   프로젝트 진행에 필요한 관계형 재고 데이터베이스(SQLite) 구축 및 제조업 설비 센서 모의 수집 환경 세팅.
*   `src/init_db.py` 스크립트를 통한 데이터셋 파이프라인 초기화.

### 🕸️ Phase 2: Individual Specialist Agent Nodes (전문가 노드 개발)
*   센서 실시간 감시 모니터링 노드, Neo4j GraphRAG 연동 가이드 노드, Text-to-SQL 자재 관리 노드 등 개별 특화 에이전트 설계 및 도구(Tools) 통합.

### 🧠 Phase 3: LangGraph Supervisor Choreography (에이전트 군집 오케스트레이션)
*   `LangGraph` 상태 머신 아키텍처를 기반으로 자율적인 라우팅 루프와 예외 해결을 조율하는 Supervisor 에이전트 구축.

### 🏢 Phase 4: Real-time Web Dashboard Portal (관제 웹 포털)
*   Streamlit 웹 애플리케이션 개발을 통한 센서 스트리밍, 에이전트 협업 메시지 로그, 인벤토리 현황을 한눈에 보는 통합 팩토리 대시보드 구현.

### ⚙️ Phase 5: MLOps Monitoring & Drift Analysis (실시간 데이터/모델 모니터링)
*   **MLflow**를 활용한 에이전트 응답 성능 로깅 및 지표 추적.
*   **Evidently AI**를 사용하여 공장 센서 데이터 드리프트(Data Drift) 및 모델 예측 지표의 변동을 실시간으로 추적하여 비정상 탐지 성능을 보장하는 MLOps 인프라 구축.

---

## 🗂️ Directory Structure

```text
Season3_MultiAgent_Swarm/
├── data/
│   ├── ai4i2020.csv          # 센서 데이터 (수학/정량)
│   ├── cnc_manual.txt        # 설비 매뉴얼 (자연어/비정형)
│   └── inventory.sqlite      # 재고 데이터 (관계형/정형)
├── src/
│   ├── init_db.py            # SQLite 초기화 스크립트
│   ├── tools/                # 에이전트용 개별 툴 (Pandas, Neo4j, SQL)
│   ├── agents/               # LangGraph 노드(Node) 정의
│   └── app.py                # Streamlit 대시보드
├── notebook/                 # 테스트 및 시뮬레이션 노트북
├── requirements.txt
└── .env.example
```

---

<br>
<div align="center">
  <i>Created with ❤️ by Jung Seyoon (SuwonRockman)</i>
</div>
