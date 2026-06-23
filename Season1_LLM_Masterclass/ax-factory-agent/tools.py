import pandas as pd
import os

# 데이터셋 로드 (글로벌 변수로 캐싱)
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'ai4i2020.csv')
try:
    df = pd.read_csv(DATA_PATH)
except:
    df = None

# 가상의 티켓팅 데이터베이스
TICKET_DB = []

def get_sensor_data(machine_id: str) -> str:
    """
    주어진 머신 ID(예: M14860)의 현재 설비 센서 데이터를 실제 CSV에서 조회합니다.
    """
    if df is None:
        return "[ERP Error] 센서 데이터베이스(CSV)에 접근할 수 없습니다."
        
    # 'Product ID' 컬럼에서 machine_id를 찾습니다.
    machine_data = df[df['Product ID'] == machine_id]
    
    if machine_data.empty:
        return f"[ERP Response] 기기 '{machine_id}'를 찾을 수 없습니다."
        
    row = machine_data.iloc[0]
    
    # 실제 수치를 포맷팅하여 리턴
    return (
        f"[ERP Response] Machine {machine_id} 상태:\n"
        f"- 공정 온도(Process Temp): {row['Process temperature [K]']} K\n"
        f"- 회전 속도(Rotational speed): {row['Rotational speed [rpm]']} RPM\n"
        f"- 토크(Torque): {row['Torque [Nm]']} Nm\n"
        f"- 툴 마모도(Tool wear): {row['Tool wear [min]']} min"
    )

def issue_work_order(machine_id: str, task_description: str) -> str:
    """
    정비 부서에 수리 지시(Work Order) 티켓을 발행합니다.
    """
    ticket_id = len(TICKET_DB) + 100
    ticket = {"ticket_id": ticket_id, "machine": machine_id, "task": task_description, "status": "OPEN"}
    TICKET_DB.append(ticket)
    return f"[Ticketing System] 성공적으로 정비 티켓(Ticket #{ticket_id})이 발행되었습니다. 내용: {machine_id} - {task_description}"
