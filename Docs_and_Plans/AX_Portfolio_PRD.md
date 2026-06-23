# [포트폴리오 마스터 기획서]
**프로젝트명**: AX 기획자 역량 증명 포트폴리오 (Daily AI Study & Build with Agent)

**대상**: 정세윤  
- 학력: 정치국제학 학사 / 한양대 AI대학원 재학
- 경력: PSK 6년 (부품 영업기획 4.5년 + 전략기획 1.5년) / **현재: AI 실무 경험 없음**
- 타겟 직무: AI 기획, AX 기획

**목표**: 2025년 6월 이내 AI/AX 기획 직무 이직  

**배경**: 대학원 공부만으로는 부족 → 실제 LLM/DL/Agent 구현 경험 필요 / 기획자로서 기술 깊이 증명 필요

**전략**: AI 튜터 에이전트(Claude)와 함께 LLM/DL/Agent 마스터하고 GitHub에 주제별 30~40개 독립 레포 구축

**실행 방식**:
- **시작**: 다음주 (2026.06.02)
- **학습 순서**: LLM → DL → Agent
- **깊이**: 기초부터 단계적
- **코드**: Python(.py) + Jupyter(.ipynb) (필요시 데이터셋 포함)
- **대화**: Claude Code 세션(antigravity 터미널)에서 자유롭게 진행
- **GitHub**: 최종 완성본만 업로드 (중간 결과물/대화는 GitHub에 올리지 않음)
- **진행 추적**: 주간 목표 미달 시 다음 주로 지연
- **README 업데이트**: 수동 (사용자 요청 시)

## 1. 전략 (Strategy)

### 기술 스택 마스터링 (LLM/DL/Agent 중심)
'기술 스택(Tech Stack)'을 하나씩 깊이 있게 구축해 나갑니다.
*   **LLM (Large Language Model)**: 트랜스포머 아키텍처 / 토크나이제이션 / Fine-tuning / Prompt Engineering
*   **DL (Deep Learning)**: CNN, RNN, Attention, Transformer 등 신경망 아키텍처 / 특징 추출 원리
*   **AI Agent**: 언어 모델 추론 / RAG (Retrieval-Augmented Generation) / Tool Use / 멀티 에이전트 시스템

> [!NOTE]
> LLM/DL/Agent 순서를 고정하지 않음. AI 튜터 에이전트가 능동적으로 주제를 제시하고, 
> 관심도에 맞춰 유연하게 진행. (예: Attention 학습 → Transformer → LLM으로 자연 전환)

### AI 튜터 에이전트의 역할
*   **주제 설계**: 매주/매일 학습할 구체적 주제 능동적 제시 (예: "Attention Mechanism의 원리", "LLM Fine-tuning 실전")
*   **함께 선정**: 제시된 주제 중 당신이 선택하거나, 역제시
*   **이론-실습 연결**: "왜 이 기술이 필요한가?" + "실무에서 어떤 문제를 푸는가?" 설명
*   **구현 코칭**: 이론을 코드(Jupyter/Python)로 변환하는 과정 가이드
*   **면접 대비**: 배운 내용을 "기획자 + 개발자가 이해할 수 있도록" 설명하는 스토리텔링

## 2. 워크플로우 (Workflow)

> [!NOTE]
> **GitHub Issues + Projects를 통한 일원화 관리**
> AI 튜터(에이전트)와 정세윤이 함께 만들어가는 매일의 스터디 및 포트폴리오 누적 루틴입니다.

### 주간 사이클 (Weekly Cycle)
```
월: Claude와 대화로 주제 1~2개 선정 (난이도, 예상 시간, 학습 목표 결정)

화~목: Claude 세션에서 학습 진행
       - 이론 학습 (개념, 수학적 배경, 실무 사례)
       - 코드 구현 (Python + Jupyter 노트북)
       - 분석 및 인사이트 정리
       
금: 완성본 정리 → 새 GitHub 레포 생성 및 업로드
    - 레포명: [주제명] (예: transformer-basics)
    - README.md (이론 정리)
    - /notebook/[주제].ipynb (코드 + 실행 결과)
    - /scripts/[주제].py (Python 스크립트)
    - 초기 커밋 → push (PR 없음)
    
주말: 선택적 심화 학습 또는 휴식
```

### 주제별 학습 프로세스 (Per-Topic Process)

| 단계 | 내용 | 산출물 |
|------|------|--------|
| **1. 주제 선정** | Claude와 대화로 주제, 난이도, 학습 목표 결정 | 선정된 주제 + 계획 |
| **2. 이론 학습** | 개념, 수학적 배경, 실무 적용 사례 학습 | 학습 노트 (대화 기록) |
| **3. 코드 구현** | Python + Jupyter에서 실제 모델 구축 및 검증 | 실행 가능한 코드 |
| **4. 분석 & 정리** | 왜 이런 결과가 나왔는지, 언제 써야 하는지 정리 | 분석 결과 |
| **5. GitHub 업로드** | 이론 문서 + 코드를 GitHub에 단일 커밋으로 업로드 | 최종 완성본 (docs + notebooks + scripts) |

### GitHub 저장소 구조 (주제별 독립 레포)

**각 주제마다 독립적인 GitHub 레포 생성**

예시: `transformer-basics` 레포
```
transformer-basics/ (GitHub Repository)
│
├── README.md                          # 학습 내용 정리
│   └─ 개념 설명 + 학습 목표 + 핵심 내용
│
├── notebook/
│   └── transformer_basics.ipynb       # Jupyter 노트북 (실행 결과 포함)
│
├── scripts/
│   └── transformer_basics.py          # Python 실행 스크립트
│
├── data/                              # 필요시만 포함
│   └── sample_data.csv
│
└── .gitignore                          # Python/Jupyter 표준 설정
```

**전체 포트폴리오 (30~40개 레포)**
```
GitHub 프로필
├── transformer-basics
├── tokenization
├── llm-fine-tuning
├── prompt-engineering
├── cnn-basics
├── rnn-seq2seq
├── attention-mechanism
├── rag-system
├── tool-use
├── multi-agent-system
└── ... (30~40개)
```

## 3. 기대 효과 (Expected Output & Timeline)

### 산출물 (6개월)
- **GitHub 레포**: 30~40개 (주제별 독립 레포)
- **GitHub 커밋**: 30~40개 (각 레포당 초기 커밋 1개)
- **이론 문서**: 30~40개 (각 레포의 README.md)
- **Jupyter 노트북**: 30~40개 (각 레포의 notebook/)
- **Python 스크립트**: 30~40개 (각 레포의 scripts/)
- **데이터셋**: 필요시 포함
- **GitHub 잔디**: 26~52개 커밋 (주간 1~2개 주제)

