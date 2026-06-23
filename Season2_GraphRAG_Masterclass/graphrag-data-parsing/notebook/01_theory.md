# Step 01. Advanced Data Parsing (데이터 정제와 청킹)

## 1. GIGO (Garbage In, Garbage Out) 원칙
RAG(Retrieval-Augmented Generation) 시스템, 특히 지식 그래프(Knowledge Graph)를 구축할 때 가장 흔히 저지르는 실수는 **"원본 데이터를 그대로 LLM에 던지는 것"**입니다. 

LLM은 마법이 아닙니다. 다음과 같은 데이터가 그대로 들어가면 할루시네이션(환각)이나 잘못된 관계(Relation) 추출이 발생합니다.
* 불필요한 줄바꿈(`\n\n`)과 하이픈(`---`)
* 여러 출처(YouTube, Substack)의 뉴스가 뒤섞인 상태
* 문맥이 단절된 파편화된 문장들

따라서 GraphRAG의 **첫 번째 임무(Phase 1)**는 더러운 텍스트를 LLM이 가장 소화하기 좋은 '구조화된 JSON 딕셔너리' 형태로 가공하는 것입니다.

## 2. Chunking (청킹) 전략: 왜 헤더(Header) 기준인가?
텍스트를 자르는 방법에는 여러 가지가 있습니다.
1. **고정 길이 분할 (Fixed-size Chunking):** 무조건 500자씩 자름. (문맥이 잘려나가는 치명적 단점)
2. **문장 분할 (Sentence Splitting):** 마침표 기준으로 자름. (지식망을 그리기엔 정보가 너무 부족함)
3. **구조 기반 분할 (Structural Chunking):** 마크다운의 헤더(`##`)나 HTML 태그를 기준으로 자름.

우리의 미국 주식 데이터는 `## 1️⃣ 수페TV - 나스닥 반등 vs 금값` 처럼 완벽한 **구조적 마크다운(Markdown)** 형태를 띄고 있습니다. 
따라서 정규표현식(Regex)을 이용해 헤더(Header)를 기준으로 청크를 나누는 **Structural Chunking** 기법을 사용합니다. 이를 통해 각 출처별(Source)로 완벽하게 독립적인 문맥(Context)을 LLM에게 전달할 수 있습니다.

## 3. Metadata Tagging (메타데이터 태깅)
데이터를 쪼갠 후에는 반드시 꼬리표(Metadata)를 달아야 합니다.
* `source`: 이 정보가 어디서 왔는가? (예: 수페TV)
* `title`: 핵심 주제는 무엇인가?
* `content`: 정제된 순수 텍스트 내용

이렇게 메타데이터를 태깅해두면, 나중에 GraphRAG 엔진이 사용자에게 답변할 때 **"이 분석은 수페TV의 데이터를 기반으로 추론되었습니다"** 라며 정확한 출처(Citation)를 밝힐 수 있어 시스템의 신뢰도가 수백 배 상승합니다.

---

> 다음 실습 파일인 `02_markdown_parsing.ipynb`에서 파이썬 정규표현식을 이용해 실제로 데이터를 파싱하고 JSON으로 저장하는 코드를 구현합니다.
