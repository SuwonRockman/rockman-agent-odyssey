# 📊 고급 파싱 (Advanced Data Parsing): 텍스트의 구조화 및 청킹

[![Generated](https://img.shields.io/badge/Date-2026.06.21-blue.svg)](#) [![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange.svg)](#)

> [!NOTE]
> **핵심 질문:** LLM에게 여러 출처의 복잡한 뉴스가 뒤섞인 마크다운 텍스트를 통째로 던져주면 지식 그래프를 제대로 그릴 수 있을까요? 정답은 '아니오'입니다. 그렇다면 어떻게 텍스트를 '의미 단위'로 쪼개고 꼬리표를 달아줄 수 있을까요?

이 레포지토리는 GraphRAG 구축의 첫 단추로서, 더러운 원본 텍스트(Raw Data)를 LLM이 완벽하게 소화할 수 있는 깨끗한 단위(Chunk)로 분할하고 메타데이터(Metadata)를 주입하는 파이프라인의 수학적/논리적 기반을 탐구합니다.

---

## 📂 목차 (Contents)

- **`01_theory.md`**: GIGO(Garbage In, Garbage Out) 현상의 위험성, 일반적인 Fixed-size Chunking의 한계와 마크다운 기반 Structural Chunking의 우월성 비교 분석
- **`02_algorithm_from_scratch.ipynb`**: 파이썬 정규표현식(`re`)을 활용한 헤더 단위 청킹 알고리즘 구현 및 `[Source, Title, Content]` 구조의 메타데이터 태깅 자동화 로직

---

## 🛠️ 기술 스택 (Tech Stack)
- Python
- Regular Expression (`re`)
- JSON Data Structuring
- Jupyter Notebook

---
<div align="right">
  <b>GitHub:</b> <a href="https://github.com/SuwonRockman/rockman-agent-odyssey/tree/master/Season2_GraphRAG/01_graphrag_data_parsing">SuwonRockman/01_graphrag_data_parsing</a>
</div>
