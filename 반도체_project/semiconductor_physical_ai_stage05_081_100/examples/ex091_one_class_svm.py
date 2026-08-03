from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_anomaly_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_anomaly_data.csv 파일이 없습니다.")

from sklearn.preprocessing import StandardScaler
from sklearn.svm import OneClassSVM

sensor_df = pd.read_csv(DATA_FILE)

features = [
    "chamber_temp_c",
    "chamber_pressure_pa",
    "rf_power_w",
    "gas_flow_sccm",
    "vibration_g",
    "particle_count",
]

x_scaled = StandardScaler().fit_transform(sensor_df[features])

model = OneClassSVM(
    kernel="rbf",
    gamma="scale",
    nu=0.1,
)
prediction = model.fit_predict(x_scaled)

sensor_df["ocsvm_anomaly"] = (prediction == -1).astype(int)
sensor_df["ocsvm_anomaly_score"] = (
    -model.decision_function(x_scaled)
)

print(
    "One-Class SVM 이상 수:",
    int(sensor_df["ocsvm_anomaly"].sum()),
)
