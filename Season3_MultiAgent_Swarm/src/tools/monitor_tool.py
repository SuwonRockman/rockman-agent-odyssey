import pandas as pd
import os
from langchain_core.tools import tool

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'ai4i2020.csv')

@tool
def check_sensor_anomalies() -> str:
    """
    Reads the latest sensor data from the factory equipment and checks for any anomalies (e.g., high torque, machine failure flags).
    Returns a summary report of the machine's current status.
    """
    try:
        # Read the CSV dataset
        df = pd.read_csv(DATA_PATH)
        
        # Simulate getting the "latest" 50 records
        latest_data = df.tail(50)
        
        # Check if any failure flags are triggered in the latest data
        failures = latest_data[latest_data['Machine failure'] == 1]
        
        if not failures.empty:
            # Extract reasons
            failure_types = []
            if failures['TWF'].sum() > 0: failure_types.append("Tool Wear Failure (TWF)")
            if failures['HDF'].sum() > 0: failure_types.append("Heat Dissipation Failure (HDF)")
            if failures['PWF'].sum() > 0: failure_types.append("Power Failure (PWF)")
            if failures['OSF'].sum() > 0: failure_types.append("Overstrain Failure (OSF)")
            
            # Find max torque during failure
            max_torque = failures['Torque [Nm]'].max()
            
            report = f"🚨 ANOMALY DETECTED! 🚨\n"
            report += f"- {len(failures)} failure events detected in the last 50 cycles.\n"
            report += f"- Failure Types: {', '.join(failure_types)}\n"
            report += f"- Max Torque reached: {max_torque} Nm\n"
            report += "Action required: Dispatch maintenance engineer to check equipment immediately."
            return report
        else:
            return "✅ Machine status is normal. No anomalies detected in the latest 50 cycles."
            
    except Exception as e:
        return f"Error reading sensor data: {str(e)}"

# For testing
if __name__ == "__main__":
    print(check_sensor_anomalies.invoke({}))
