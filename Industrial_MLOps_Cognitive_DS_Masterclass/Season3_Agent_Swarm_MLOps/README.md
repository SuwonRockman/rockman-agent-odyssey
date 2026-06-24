# ⚙️ Season 3: Agent Swarm & MLOps (에이전트 군집 & MLOps)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Framework: LangGraph & MLflow](https://img.shields.io/badge/Framework-LangGraph%20%7C%20MLflow-0A84C6.svg)](#)

본 과정은 앞선 시즌의 데이터 과학 모델과 지식 검색 포털을 에이전트 군집(Agent Swarm)으로 확장하여, 프로덕션 환경에 Docker 컨테이너로 배포하고 MLflow와 Evidently AI로 모델의 성능과 데이터 변동성을 실시간 감시하는 최상위 운영 엔지니어링 과정입니다.

---

## 🗺️ 5단계 커리큘럼 로드맵 (Curriculum Roadmap)

### 🧱 Phase 1: Agent Collaboration Architecture
*   `LangGraph` 상태 머신 프레임워크 기반 설계.
*   공장 내 이상 징후를 감지하여 조치 방안을 검색하고 자재 발주를 진행하는 개별 전문 AI 노드 간의 오케스트레이션 및 데이터 라우팅 루프 구현.

### 🕸️ Phase 2: Production API Service
*   멀티 에이전트 협업 시스템을 `FastAPI` 기반 마이크로서비스로 추상화하고, `Docker` 컨테이너로 묶어 배포 및 인프라 이식성을 보장하는 기술.

### 🧠 Phase 3: MLflow Tracking & Register
*   실시간으로 추론하는 에이전트 응답 지표와 분류 모델 메트릭을 `MLflow` 서버에 수집 및 기록하고, 프로덕션 배포용 중앙 모델 저장소(Model Registry) 구축.

### 🏢 Phase 4: Data Drift & Monitoring
*   **Evidently AI** 모니터링 대시보드 구축.
*   실시간 유입되는 센서 시계열 데이터의 통계적 분포(Data Drift) 및 모델 예측 지표의 하락을 실시간으로 감지하여 비정상 위험 탐지.

### ⚙️ Phase 5: Automated CI/CD & Retraining Pipeline
*   데이터 드리프트 감지 경보 시, GitHub Actions와 MLflow 파이프라인을 연동하여 새로운 데이터로 모델을 자동으로 재학습하고, 무중단으로 신규 버전을 배포하는 완전 자동화 MLOps 고리 완성.

---

## 🛠️ 실습 환경 준비
시즌 3를 시작하게 될 경우 필요한 핵심 패키지들은 추후 업데이트될 예정입니다.
*   **대표 사용 패키지**: `langgraph`, `fastapi`, `docker`, `mlflow`, `evidently`
