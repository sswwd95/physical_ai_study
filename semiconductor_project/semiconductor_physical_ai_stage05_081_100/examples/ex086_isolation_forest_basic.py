from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_anomaly_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_anomaly_data.csv 파일이 없습니다.")

from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

features = [
    "chamber_temp_c",
    "chamber_pressure_pa",
    "rf_power_w",
    "gas_flow_sccm",
    "vibration_g",
    "particle_count",
]

scaler = StandardScaler()
x_scaled = scaler.fit_transform(sensor_df[features])

model = IsolationForest(
    n_estimators=200,
    contamination=0.1,
    random_state=42,
)
prediction = model.fit_predict(x_scaled)

sensor_df["iforest_anomaly"] = (prediction == -1).astype(int)

print(
    "Isolation Forest 이상 수:",
    int(sensor_df["iforest_anomaly"].sum()),
)
sensor_df.to_csv(
    OUTPUT_DIR / "ex086_isolation_forest.csv",
    index=False,
    encoding="utf-8-sig",
)
