# 📊 AX Data Analyst Agent: 자율형 데이터 사이언티스트 (Code Interpreter)

[![Generated](https://img.shields.io/badge/Date-2026.06.18-blue.svg)](#) [![Dataset](https://img.shields.io/badge/Dataset-NASA_CMAPSS-orange.svg)](#)

본 프로젝트는 대규모 제조/항공 데이터를 LLM이 스스로 분석하는 **AX(AI Transformation) 데이터 사이언티스트 에이전트**입니다.

## 📌 핵심 기능
1. **NASA 제트 엔진 데이터 연동:** 전 세계 예지 보전(Predictive Maintenance)의 표준 벤치마크인 NASA CMAPSS 데이터를 로컬 SQLite DB로 구축.
2. **Text-to-SQL 엔진:** 자연어 지시를 바탕으로 다중 테이블(JOIN) 쿼리를 스스로 작성하여 데이터 추출.
3. **Code Interpreter & Self-Correction:** 추출된 데이터를 시각화하기 위해 파이썬 코드를 작성하고 로컬에서 강제 실행(`exec`). 에러 발생 시 스스로 에러 로그를 읽고 코드를 수정하는 자가 디버깅 루프 구현.

---
<div align="right">
  <b>GitHub:</b> <a href="https://github.com/SuwonRockman/ax-data-analyst-agent">SuwonRockman/ax-data-analyst-agent</a>
</div>
