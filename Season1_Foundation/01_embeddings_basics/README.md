# 📊 임베딩 (Embeddings): 단어에 수학적 좌표 부여하기

[![Generated](https://img.shields.io/badge/Date-2026.06.16-blue.svg)](#) [![Difficulty](https://img.shields.io/badge/Difficulty-Medium%20High-orange.svg)](#)

> [!NOTE]
> **핵심 질문:** 컴퓨터는 글자를 모릅니다. 그렇다면 "사과"와 "배"가 비슷하고, "사과"와 "컴퓨터"가 다르다는 '의미적 연관성(Semantics)'을 숫자로 어떻게 가르칠 수 있을까요?

이 레포지토리는 단순한 빈도수 계산(TF-IDF)을 넘어, 인공신경망을 통해 단어를 고차원 벡터 공간의 좌표로 매핑하는 **분산 표현(Distributed Representation)**과 **Word2Vec**의 수학적 깊이를 탐구합니다.

---

## 📂 목차 (Contents)

- **`01_theory.md`**: One-Hot 인코딩의 차원의 저주, Word2Vec(CBOW vs Skip-gram)의 구조 차이, 거대 어휘 사전을 다루기 위한 네거티브 샘플링(Negative Sampling)의 수학적 유도
- **`02_algorithm_from_scratch.ipynb`**: PyTorch `nn.Embedding` 레이어를 직접 학습시키는 Skip-gram 훈련 루프 구현 및 차원 축소(PCA/t-SNE)를 통한 단어 공간 시각화
- **`03_advanced_practice.ipynb`**: 사전 학습된 GloVe 임베딩을 로드하여 `King - Man + Woman = Queen` 이라는 유명한 벡터 산술(Vector Arithmetic) 방정식 증명 및 코사인 유사도 분석

---

## 🛠️ 기술 스택 (Tech Stack)
- Python
- PyTorch (Embedding, Negative Sampling)
- Scikit-Learn (PCA, t-SNE)
- Matplotlib / Seaborn
- Jupyter Notebook

---
<div align="right">
  <b>GitHub:</b> <a href="https://github.com/SuwonRockman/rockman-agent-odyssey/tree/master/Season1_Foundation/01_embeddings_basics">SuwonRockman/01_embeddings_basics</a>
</div>
