# Step 03. Theory: Why Hybrid Search? 🧠

일반적인 RAG(Retrieval-Augmented Generation) 튜토리얼을 보면 십중팔구 Chroma나 FAISS 같은 Vector DB를 사용합니다. 
그렇다면 왜 글로벌 IT 기업들은 복잡한 Graph DB를 도입하여 **하이브리드 검색(Hybrid Search)**을 구축하는 것일까요?

## 1. Vector Search의 치명적인 한계 (단어의 파편화)
Vector Search(유사도 검색)는 문장이나 단어의 '의미적 유사성(Cosine Similarity)'만을 기준으로 데이터를 가져옵니다.
*   **사용자 질문:** "애플의 신제품 발표가 테슬라 주가에 미치는 영향은?"
*   **Vector Search의 결과:** '애플', '신제품', '테슬라', '주가' 라는 단어와 가장 비슷한 문서 3~4개를 각각 따로따로 가져옵니다. 
*   **문제점:** 애플 문서 2개, 테슬라 문서 2개를 가져왔을 뿐, **애플과 테슬라 사이의 인과관계나 숨겨진 연결고리**는 가져오지 못합니다. LLM은 파편화된 정보를 보고 환각(Hallucination)을 일으키기 쉽습니다.

## 2. Graph Traversal의 강력함 (문맥의 연결)
Graph Search는 점(Node)과 선(Edge)을 타고 들어갑니다.
*   "애플" 노드를 찾은 뒤, `[COMPETES_WITH]` 선을 타고 "마이크로소프트"를 가져오고, `[AFFECTS]` 선을 타고 "테슬라"를 연쇄적으로 가져옵니다.
*   정보가 파편화되지 않고, 하나의 거대한 '문맥 덩어리(Context Subgraph)'로 묶여서 LLM에게 전달됩니다.

## 3. 하이브리드 서치 (Hybrid Search = Vector + Graph)
따라서 이 두 가지를 결합한 하이브리드 서치가 현재 엔터프라이즈 AI의 SOTA(State-of-the-Art)입니다.

1.  **시작점 찾기 (Vector Search):** 수백만 개의 노드 중에서 질문과 가장 유사한 핵심 노드 2~3개를 벡터로 빠르게 찾아냅니다. (예: '애플' 노드 발견)
2.  **문맥 확장 (Graph Traversal):** 찾아낸 '애플' 노드에서 출발하여 1단계, 2단계 깊이로 선(Edge)을 타고 들어가 주변의 연관된 리스크, 인물, 제품 정보를 싹 다 긁어옵니다.
3.  **LLM 답변:** 이 거대한 문맥 덩어리를 프롬프트에 담아 `gpt-4o`에게 전달하면, 환각 없이 완벽한 분석 보고서가 탄생합니다.

다음 노트북에서는 이를 **프레임워크의 블랙박스 함수 없이 순수 Cypher 쿼리로 바닥부터(From Scratch)** 구현합니다.
