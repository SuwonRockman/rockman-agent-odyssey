import streamlit as st
import time
import os
import matplotlib
import pandas as pd
import sqlite3
import traceback
import matplotlib.pyplot as plt

# Headless 모드로 Matplotlib 설정 (클라우드 환경 대응)
matplotlib.use('Agg')

# 페이지 설정
st.set_page_config(page_title="AX Data Analyst", page_icon="📊", layout="wide")

st.title("📊 AX Data Analyst Agent")
st.caption("NASA CMAPSS 제트 엔진 센서 데이터를 자율 분석하는 Code Interpreter 에이전트")

# 사이드바 (포트폴리오 설명)
with st.sidebar:
    st.header("📌 About This Demo")
    st.markdown("""
    이 데모는 **LLM Masterclass Phase 5**의 결과물입니다.
    사용자의 자연어 지시를 받아 다음 과정을 자율 수행합니다:
    1. **Text-to-SQL**: SQLite DB에서 데이터 추출
    2. **Code Generation**: 파이썬 시각화 코드 작성
    3. **Local Execution**: 코드 실행 (`exec`)
    4. **Self-Correction**: 에러 발생 시 스스로 디버깅
    
    *참고: 포트폴리오 체험을 위해 API 과금 없이 동작하는 100% 성공 보장형 시뮬레이션 모드로 작동합니다.*
    """)
    st.divider()
    st.write("👨‍💻 **Developer:** Jung Seyoon")

# DB 경로 설정 및 확인
db_path = os.path.join(os.path.dirname(__file__), 'data', 'factory_db.sqlite')

# 초기 데이터 (세션 상태 유지)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "안녕하세요! 저는 NASA 제트 엔진 데이터를 관리하는 AI 데이터 분석가입니다. 어떤 분석 보고서가 필요하신가요?\\n\\n*(추천 질문: 엔진 1번의 비행 사이클별 온도 변화를 꺾은선 그래프로 그려줘!)*"}
    ]

# 채팅 기록 출력
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "image" in msg:
            st.image(msg["image"])

# 사용자 입력 처리
if prompt := st.chat_input("질문을 입력하세요..."):
    # 1. 사용자 질문 출력
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. 에이전트 사고 과정 (시뮬레이션 UI)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        with st.status("에이전트가 분석을 시작합니다...", expanded=True) as status:
            st.write("🔍 데이터베이스 스키마(Schema) 분석 중...")
            time.sleep(1.5)
            st.write("📝 Text-to-SQL 쿼리 작성 완료:")
            st.code("SELECT cycle, sensor_2_temp FROM sensor_logs WHERE engine_id = 1;")
            time.sleep(1.5)
            st.write("⬇️ SQLite 데이터 추출 완료 (211 rows)")
            time.sleep(1.5)
            
            st.write("💻 파이썬 시각화 코드 작성 및 실행 중 (`exec`)....")
            time.sleep(1.5)
            st.error("Traceback (most recent call last):\\nKeyError: 'temperatur'")
            st.write("🤖 [Self-Correction] 오타를 발견했습니다. `temperatur` -> `sensor_2_temp`로 수정 후 재실행합니다.")
            time.sleep(2)
            
            # 실제 파이썬 코드 실행 시뮬레이션 (로컬에 저장된 DB에서 실제 데이터를 가져와 그림)
            try:
                conn = sqlite3.connect(db_path)
                df = pd.read_sql_query("SELECT cycle, sensor_2_temp FROM sensor_logs WHERE engine_id = 1", conn)
                conn.close()
                
                plt.figure(figsize=(10, 5))
                plt.plot(df['cycle'], df['sensor_2_temp'], color='red', marker='.')
                plt.title("NASA Engine 1: Temperature Degradation over Cycles")
                plt.xlabel("Flight Cycle")
                plt.ylabel("Temperature (sensor_2)")
                plt.grid(True)
                
                # 이미지 파일로 저장
                img_path = os.path.join(os.path.dirname(__file__), 'engine1_report.png')
                plt.savefig(img_path)
                plt.close()
                st.write("✅ 파이썬 코드 실행 성공! 그래프 렌더링 완료.")
            except Exception as e:
                st.write(f"데이터베이스 연결 에러 (시뮬레이션 fallback): {e}")
                img_path = None
            
            status.update(label="분석 완료!", state="complete", expanded=False)

        # 3. 최종 결과 출력
        final_answer = "엔진 1번의 수명(Cycle)에 따른 온도 변화 그래프입니다. 수명이 다해갈수록 온도가 기하급수적으로 치솟는 이상 패턴(Anomaly)을 발견했습니다."
        message_placeholder.markdown(final_answer)
        
        if img_path and os.path.exists(img_path):
            st.image(img_path)
            # 세션 상태에 저장
            st.session_state.messages.append({"role": "assistant", "content": final_answer, "image": img_path})
        else:
            st.session_state.messages.append({"role": "assistant", "content": final_answer})
