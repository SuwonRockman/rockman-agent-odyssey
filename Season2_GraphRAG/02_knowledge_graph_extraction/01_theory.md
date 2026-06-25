# Step 02. Knowledge Graph Theory: RDBMS vs GraphDB 🕸️

## 1. RDBMS의 한계: 왜 MySQL/PostgreSQL로 지식망을 그릴 수 없을까?

우리가 흔히 쓰는 관계형 데이터베이스(RDBMS)도 이름에 '관계(Relational)'가 들어있는데, 왜 굳이 Neo4j 같은 그래프 데이터베이스(Graph DB)를 써야 할까요?

*   **RDBMS (MySQL 등):**
    *   테이블(표) 구조로 데이터를 저장합니다.
    *   '테슬라' 테이블과 '일론 머스크' 테이블을 연결하려면 복잡한 **JOIN 연산**이 필요합니다.
    *   "테슬라와 3단계 이상 연결된 모든 리스크 요인을 찾아줘" 같은 쿼리를 날리면, JOIN이 기하급수적으로 늘어나 서버가 뻗어버립니다. (Index-Free Adjacency의 부재)
*   **Graph DB (Neo4j 등):**
    *   데이터를 처음부터 점(Node)과 선(Edge)으로 저장합니다.
    *   JOIN 연산 없이 포인터를 따라 선을 타고 이동하기 때문에, 관계의 깊이가 아무리 깊어져도 검색 속도가 압도적으로 빠릅니다. (밀리초 단위)

## 2. Cypher 쿼리 언어 기초 (Cypher Fundamentals)

SQL이 RDBMS의 언어라면, **Cypher**는 Neo4j의 언어입니다. Cypher는 시각적으로 직관적인 ASCII Art 형태를 띕니다.

### 🟢 1. 노드 (Node)
노드는 소괄호 `()`로 표현합니다. (동그란 점 모양)
```cypher
(c:Company {name: "Tesla", industry: "Automotive"})
```
*   `c`: 변수명 (이후 쿼리에서 재사용하기 위함)
*   `Company`: 라벨 (Node의 타입/종류)
*   `{name: "Tesla"}`: 속성 (Property)

### ➖ 2. 관계 (Relationship/Edge)
관계는 대괄호 `[]`와 화살표 `->`로 표현합니다.
```cypher
-[r:COMPETES_WITH {since: 2020}]->
```
*   `COMPETES_WITH`: 관계의 타입 (반드시 대문자 및 언더바 사용)

### 🔗 3. 패턴 매칭 (Pattern Matching)
노드와 관계를 이어 붙여 문장을 만듭니다.
```cypher
(c1:Company {name: "Tesla"})-[r:COMPETES_WITH]->(c2:Company {name: "Rivian"})
```

### 🔍 4. 조회 (MATCH)와 생성 (MERGE)
*   `MATCH`: 데이터를 찾습니다. (SQL의 SELECT)
*   `MERGE`: 데이터가 있으면 찾고, 없으면 새로 만듭니다. (그래프 적재 시 가장 많이 씁니다)

---

> 다음 실습 파일인 `02_algorithm_from_scratch.ipynb`에서는 LLM이 텍스트에서 이러한 Node와 Relationship을 뽑아내어, 자동으로 Cypher 쿼리를 생성하고 Neo4j에 `MERGE` 하는 전체 자동화 파이프라인을 구현합니다.
