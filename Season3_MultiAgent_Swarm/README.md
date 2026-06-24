# 🚀 Season 3: Autonomous AX Command Center (스마트팩토리 멀티 에이전트 군집)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Framework: LangGraph & Neo4j](https://img.shields.io/badge/Framework-LangGraph%20%7C%20Neo4j-0A84C6.svg)](#)

이 마스터클래스(Season 3)는 Season 1과 2의 핵심 기술을 집대성하여, 기업 내에서 각기 다른 데이터 포맷(CSV, GraphDB, SQL)을 다루는 여러 AI 에이전트들이 협업하는 **스마트팩토리 관제 센터(Command Center)**를 구축하는 최고난도 프로젝트입니다.

---

## 🎯 Architecture: Multi-Agent Swarm

우리의 가상 공장은 3명의 전문 에이전트와 1명의 총괄 감독관(Supervisor)으로 이루어집니다.

1. **🚨 이상 탐지 에이전트 (Monitor Agent)**
   *   **데이터:** 실시간 센서 로그 (`data/ai4i2020.csv`)
   *   **역할:** Pandas를 이용해 설비의 온도, 토크, 진동 데이터를 분석하고 임계값 초과 시 경보 발송.
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
