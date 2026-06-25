# 📚 Advanced RAG: 지식 검색 증강과 HNSW 벡터 데이터베이스

[![Generated](https://img.shields.io/badge/Date-2026.06.17-blue.svg)](#) [![Difficulty](https://img.shields.io/badge/Difficulty-Expert-purple.svg)](#)

> [!NOTE]
> **핵심 질문:** 언어 모델이 자신의 지식을 과신하여 거짓말을 지어내는 '환각(Hallucination)' 현상을 어떻게 막을 수 있을까요? 수백만 장의 사내 기밀 문서를 0.1초 만에 훑어보고 정확한 근거를 찾아오는 벡터 데이터베이스의 코어 알고리즘은 무엇일까요?

이 레포지토리는 언어 모델과 외부 지식을 결합하는 **RAG (Retrieval-Augmented Generation)** 파이프라인의 실전과, 검색 속도를 획기적으로 끌어올려 업계 표준이 된 **HNSW (Hierarchical Navigable Small World)** 알고리즘의 원리를 다룹니다.

---

## 📌 배경: 언어 모델의 한계와 RAG의 등장

LLM은 인터넷 데이터를 미리 학습한 "과거의 지식 덩어리"입니다. 따라서 두 가지 치명적인 한계가 있습니다.
1. **지식 단절:** 학습 데이터 수집이 끝난 시점 이후의 최신 뉴스나 정보를 알지 못합니다.
2. **환각 (Hallucination):** 모르는 것을 모른다고 하지 않고, 그럴듯한 문장으로 거짓말을 지어냅니다.

이를 해결하기 위해 모델이 대답을 하기 전, **질문과 관련된 외부 문서(PDF, 웹페이지 등)를 먼저 검색하여 모델의 프롬프트에 끼워 넣어주는 기술이 RAG**입니다.

---

## 🛠️ HNSW: 수백만 개의 문서를 0.1초 만에 검색하는 마법

문서가 100만 개라면, 질문과 가장 비슷한 문서를 찾기 위해 100만 번의 코사인 유사도 연산을 해야 합니다 (Brute-force KNN). 이는 실시간 챗봇 서비스에서는 불가능한 속도입니다.
이를 해결하기 위해 정확도를 1% 정도 포기하고 검색 속도를 수천 배 끌어올리는 **ANN (Approximate Nearest Neighbor)** 기술이 도입되었습니다. 그중 현재 FAISS, ChromaDB 등 모든 상용 벡터 DB가 채택한 끝판왕 알고리즘이 바로 **HNSW**입니다.

*   **NSW (Navigable Small World):** 비슷한 문서들끼리 선(Edge)을 그어 그래프를 만듭니다. 임의의 지점에서 시작해, 목적지와 거리가 더 가까워지는 이웃 노드로 계속 뛰어넘는 방식(Greedy Routing)으로 고속 탐색을 합니다.
*   **H (Hierarchical):** 고속도로망처럼 그래프를 여러 층(Layer)으로 겹겹이 쌓아 올립니다. 최상위 층(고속도로)에서 성큼성큼 건너뛰어 근처로 간 뒤, 아래층(골목길)으로 내려와 세밀하게 목적지를 찾습니다.

---

## 🗂️ 프로젝트 구조 (Contents)

단순한 랭체인(LangChain) 튜토리얼을 넘어, 파이토치와 FAISS를 이용해 텐서 레벨에서 검색과 생성 파이프라인을 직접 조립합니다.

*   **`01_theory.md`**: 전수 조사(KNN)의 한계와, HNSW가 어떻게 검색 시간 복잡도를 $O(N)$에서 $O(\log N)$으로 줄이는지 수학적 그래프 원리 해설
*   **`02_algorithm_from_scratch.ipynb`**: 파이썬 딕셔너리로 밑바닥부터 구현하는 Brute-force 탐색 vs 기초적인 NSW(Navigable Small World) 그리디 그래프 탐색 시뮬레이션
*   **`03_advanced_practice.ipynb`**: `sentence-transformers`를 활용한 텍스트 임베딩, FAISS 기반 인덱스 빌드, 그리고 HuggingFace 언어 모델을 결합한 실전 RAG QA 챗봇 파이프라인 구축

---
<div align="right">
  <b>GitHub:</b> <a href="https://github.com/SuwonRockman/rockman-agent-odyssey/tree/master/Season1_Foundation/09_advanced_rag_hnsw">SuwonRockman/09_advanced_rag_hnsw</a>
</div>
