import os
import pandas as pd
import sqlite3
import numpy as np

def build_nasa_db():
    db_path = os.path.join(os.path.dirname(__file__), 'data', 'factory_db.sqlite')
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    print("Generating High-Fidelity NASA CMAPSS Synthetic Dataset...")
    np.random.seed(42)
    
    # 1. Engines Table
    num_engines = 100
    engines = pd.DataFrame({
        'engine_id': range(1, num_engines + 1),
        'model_type': ['Turbofan_FD001'] * num_engines
    })
    
    # 2. Sensor Logs Table (시뮬레이션)
    logs = []
    maintenance = []
    
    for eid in range(1, num_engines + 1):
        # 엔진마다 고장 날 때까지의 수명(RUL)이 다름 (150 ~ 250 사이클)
        max_cycles = np.random.randint(150, 250)
        
        for cycle in range(1, max_cycles + 1):
            # 엔진이 오래될수록 온도(sensor_2)와 진동(sensor_3)이 기하급수적으로 상승하는 패턴 모사
            degradation_factor = (cycle / max_cycles) ** 2
            
            sensor_2 = 641.82 + (degradation_factor * 2.5) + np.random.normal(0, 0.1)
            sensor_3 = 1589.70 + (degradation_factor * 15.0) + np.random.normal(0, 2.0)
            
            logs.append({
                'engine_id': eid,
                'cycle': cycle,
                'setting_1': np.random.normal(35.0, 0.5),
                'sensor_2_temp': round(sensor_2, 2),
                'sensor_3_vibration': round(sensor_3, 2)
            })
            
        # 고장 시점 기록
        maintenance.append({
            'engine_id': eid,
            'failure_cycle': max_cycles,
            'repair_cost_usd': np.random.randint(5000, 15000)
        })
            
    sensor_logs_df = pd.DataFrame(logs)
    maintenance_df = pd.DataFrame(maintenance)
    
    # SQLite 저장
    conn = sqlite3.connect(db_path)
    engines.to_sql('engines', conn, if_exists='replace', index=False)
    sensor_logs_df.to_sql('sensor_logs', conn, if_exists='replace', index=False)
    maintenance_df.to_sql('maintenance_records', conn, if_exists='replace', index=False)
    
    conn.commit()
    conn.close()
    print(f"Dataset generated. Logs count: {len(sensor_logs_df)}")
    print(f"NASA CMAPSS SQLite DB successfully created at: {db_path}")

if __name__ == "__main__":
    build_nasa_db()
