import streamlit as st
import streamlit.components.v1 as components
from backend import get_hybrid_context, generate_answer
from visualize import create_network_html

# 페이지 기본 설정 (다크 모드와 어울리는 레이아웃)
st.set_page_config(page_title="GraphRAG Masterclass", page_icon="🕸️", layout="wide")

st.title("🕸️ GraphRAG Hybrid Search Engine")
st.markdown("**Powered by Neo4j Vector Index & Graph Traversal (From Scratch)**")

# 좌우 반반 레이아웃 분할
col1, col2 = st.columns([1, 1])

# 세션 상태 초기화 (채팅 내역 및 그래프 저장)
if "messages" not in st.session_state:
    st.session_state.messages = []
if "graph_html" not in st.session_state:
    st.session_state.graph_html = ""
if "context" not in st.session_state:
    st.session_state.context = ""

with col1:
    st.subheader("💬 AI Analyst Chat")
    
    # 이전 채팅 내역 출력
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    # 사용자 입력창
    if prompt := st.chat_input("질문을 입력하세요 (예: 테슬라와 관련된 주요 리스크가 뭐야?)"):
        # 1. 사용자 질문 출력
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        # 2. 백엔드(하이브리드 검색) 호출
        with st.spinner("Neo4j 하이브리드 탐색 중 (Vector + Graph)..."):
            context_str, records = get_hybrid_context(prompt)
            st.session_state.context = context_str
            # PyVis 그래프 생성 (우측 화면용)
            st.session_state.graph_html = create_network_html(records)
            
        # 3. LLM 스트리밍 답변 생성
        with st.chat_message("assistant"):
            response_stream = generate_answer(prompt, context_str)
            full_response = st.write_stream(response_stream)
            
        st.session_state.messages.append({"role": "assistant", "content": full_response})
        st.rerun()

with col2:
    st.subheader("🔍 Interactive Graph Visualization")
    
    # 그래프 렌더링
    if st.session_state.graph_html:
        components.html(st.session_state.graph_html, height=520)
    else:
        st.info("좌측에 질문을 입력하시면, 탐색된 지식망(Subgraph)이 이곳에 시각화됩니다.")
        
    # 투명성 확보 (LLM이 참고한 원본 텍스트)
    if st.session_state.context:
        with st.expander("🛠️ Show Retrieved Context (Traceability)"):
            st.code(st.session_state.context)
