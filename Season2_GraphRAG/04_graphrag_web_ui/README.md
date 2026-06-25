# Step 04. Web UI (Streamlit & PyVis) 🎨

이 레포지토리는 완성된 백엔드 엔진을 시각적으로 돋보이게 만들어줄 **웹 챗봇 및 지식망 시각화 애플리케이션**입니다.

## 🚀 주요 기능
- **Streamlit 챗봇:** OpenAI의 스트리밍(Streaming) 기능을 활용해 자연스럽고 빠른 채팅 경험 제공
- **실시간 Graph Visualization:** 하이브리드 검색으로 추출된 서브그래프(문맥)를 PyVis 모듈을 통해 인터랙티브 네트워크 맵으로 우측 패널에 렌더링
- **출처 증명 (Traceability):** LLM이 어떤 지식 기반으로 답변했는지 원본 Context를 아코디언 UI로 공개

## 💻 실행 방법
```bash
cd graphrag-web-ui
pip install streamlit pyvis
streamlit run app.py
```
