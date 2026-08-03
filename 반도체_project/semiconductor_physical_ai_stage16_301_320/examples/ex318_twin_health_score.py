from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "digital_twin_sensor_stream.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "data/digital_twin_sensor_stream.csv 파일이 없습니다."
    )

sensor_df = pd.read_csv(DATA_FILE)

temp_error = np.abs(
    sensor_df["temp_sensor_a_c"]
    - sensor_df["true_temperature_c"]
).fillna(2.0)

pressure_error = np.abs(
    sensor_df["pressure_sensor_a_pa"]
    - sensor_df["true_pressure_pa"]
).fillna(1.0)

rf_error = np.abs(
    sensor_df["rf_sensor_w"]
    - sensor_df["true_rf_power_w"]
)

gas_error = np.abs(
    sensor_df["gas_sensor_sccm"]
    - sensor_df["true_gas_flow_sccm"]
).fillna(3.0)

normalized_risk = (
    temp_error / 2.0
    + pressure_error / 1.0
    + rf_error / 20.0
    + gas_error / 5.0
) / 4

sensor_df["twin_health_score"] = np.exp(-normalized_risk)

print(sensor_df["twin_health_score"].describe().round(4))
