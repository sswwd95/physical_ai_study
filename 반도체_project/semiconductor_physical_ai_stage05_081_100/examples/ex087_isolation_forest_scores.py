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

x_scaled = StandardScaler().fit_transform(sensor_df[features])

model = IsolationForest(
    n_estimators=200,
    contamination="auto",
    random_state=42,
)
model.fit(x_scaled)

sensor_df["iforest_anomaly_score"] = (
    -model.score_samples(x_scaled)
)

top_df = (
    sensor_df.sort_values(
        "iforest_anomaly_score",
        ascending=False,
    )
    .head(20)
)

print(top_df[
    ["timestamp", "lot_id", "iforest_anomaly_score", "true_anomaly"]
].round(4))
top_df.to_csv(
    OUTPUT_DIR / "ex087_iforest_top_scores.csv",
    index=False,
    encoding="utf-8-sig",
)
