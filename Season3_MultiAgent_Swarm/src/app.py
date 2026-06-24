import streamlit as st
import os
import sys
import pandas as pd
from dotenv import load_dotenv

# Path setup
sys.path.append(os.path.dirname(__file__))
from agents.swarm import build_swarm_graph
from langchain_core.messages import HumanMessage, AIMessage

# Page Config
st.set_page_config(page_title="AX Command Center", page_icon="🏭", layout="wide")

# Custom CSS for dark aesthetic
st.markdown("""
<style>
    .stApp { background-color: #0E1117; color: #FAFAFA; }
    .header-text { font-size: 36px; font-weight: 800; color: #00FFCC; margin-bottom: 0px; }
    .sub-text { font-size: 18px; color: #888888; margin-bottom: 30px; }
    .agent-msg { padding: 15px; border-radius: 10px; margin-bottom: 15px; background: rgba(255, 255, 255, 0.05); border-left: 5px solid #00FFCC; }
    .system-alert { padding: 15px; border-radius: 10px; margin-bottom: 15px; background: rgba(255, 50, 50, 0.1); border-left: 5px solid #FF3333; color: #FFaaaa;}
    .agent-name { font-weight: bold; color: #00FFCC; margin-bottom: 5px;}
    .supervisor-msg { border-left: 5px solid #BB86FC; }
    .supervisor-name { color: #BB86FC; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="header-text">🏭 Autonomous AX Command Center</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Powered by LangGraph Swarm Intelligence</p>', unsafe_allow_html=True)

# Load ENV and Graph
@st.cache_resource
def init_graph():
    env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    load_dotenv(env_path)
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "your_openai_api_key_here":
        return None
    return build_swarm_graph(api_key)

graph = init_graph()

if not graph:
    st.error("⚠️ OPENAI_API_KEY is missing or invalid in .env file.")
    st.stop()

# Thread Config for Memory
thread_config = {"configurable": {"thread_id": "streamlit_shift_003"}}

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📊 Live Sensor Telemetry")
    # Load dummy telemetry data for visualization
    try:
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'ai4i2020.csv')
        df = pd.read_csv(csv_path)
        
        # Design enhanced: Use area_chart with custom colors for premium look
        chart1_df = df[['Torque [Nm]']].tail(100).rename(columns={'Torque [Nm]': 'Torque (Nm)'}).reset_index(drop=True)
        st.area_chart(chart1_df, color="#FF4B4B")
        
        chart2_df = df[['Rotational speed [rpm]']].tail(100).rename(columns={'Rotational speed [rpm]': 'Rotational Speed (rpm)'}).reset_index(drop=True)
        st.area_chart(chart2_df, color="#00D4FF")
    except:
        st.warning("Sensor data not found.")
        
    st.markdown("---")
    st.markdown("### 👨‍💼 Human-in-the-Loop")
    st.info("When an agent attempts to make a critical database change or purchase order, the workflow will pause here for your approval.")
    
    # State inspection
    state = graph.get_state(thread_config)
    is_paused = state.next and "SupplyChain_Tools" in state.next
    
    if is_paused:
        st.markdown('<div class="system-alert" style="background-color: rgba(0, 212, 255, 0.1); border-left-color: #00d4ff; color: #e0e0e0;">📝 <b>공장장 결재 대기 중</b><br>SupplyChain 에이전트가 데이터베이스 조작을 요청했습니다. 승인하시겠습니까?</div>', unsafe_allow_html=True)
        if st.button("✅ Approve Action & Resume", type="primary"):
            with st.spinner("Resuming Swarm execution..."):
                # Resume graph execution
                for output in graph.stream(None, thread_config, stream_mode="updates"):
                    pass
                st.rerun()

with col2:
    st.subheader("🤖 Swarm Comm-Link")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history
    for msg in st.session_state.messages:
        role = msg["role"]
        content = msg["content"]
        if role == "User":
            st.markdown(f'<div class="agent-msg" style="border-left-color: #888888;"><div class="agent-name" style="color: #888888;">👤 User</div>{content}</div>', unsafe_allow_html=True)
        elif role == "Supervisor":
            st.markdown(f'<div class="agent-msg supervisor-msg"><div class="agent-name supervisor-name">👨‍💼 Supervisor</div>{content}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="agent-msg"><div class="agent-name">🤖 {role}</div>{content}</div>', unsafe_allow_html=True)
    # Chat input - Block input if graph is paused to prevent OpenAI tool call sequence errors
    if prompt := st.chat_input("Command the Swarm (e.g. 'Check Machine #2 status')", disabled=bool(is_paused)):
        # Add user message
        st.session_state.messages.append({"role": "User", "content": prompt})
        st.markdown(f'<div class="agent-msg" style="border-left-color: #888888;"><div class="agent-name" style="color: #888888;">👤 User</div>{prompt}</div>', unsafe_allow_html=True)
        
        with st.spinner("Swarm is coordinating..."):
            inputs = {"messages": [HumanMessage(content=prompt)]}
            
            # Stream from graph (single execution loop)
            for output in graph.stream(inputs, thread_config, stream_mode="updates"):
                for node_name, node_state in output.items():
                    # Handle Supervisor routing msg
                    if node_name == "Supervisor":
                        next_node = node_state.get("next", "FINISH")
                        msg_text = f"Routing task to: **{next_node}** ➡️"
                        st.session_state.messages.append({"role": "Supervisor", "content": msg_text})
                        st.markdown(f'<div class="agent-msg supervisor-msg"><div class="agent-name supervisor-name">👨‍💼 Supervisor</div>{msg_text}</div>', unsafe_allow_html=True)
                    else:
                        # Handle Worker msg
                        if "messages" in node_state and len(node_state["messages"]) > 0:
                            last_msg = node_state["messages"][-1]
                            sender = getattr(last_msg, 'name', node_name)
                            if isinstance(last_msg, AIMessage) and last_msg.content:
                                st.session_state.messages.append({"role": sender, "content": last_msg.content})
                                st.markdown(f'<div class="agent-msg"><div class="agent-name">🤖 {sender}</div>{last_msg.content}</div>', unsafe_allow_html=True)
                                
        # Update UI completely
        st.rerun()
