from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data_stage04.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_sensor_data_stage04.csv 파일이 없습니다.")

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

features = [
    "chamber_temp_c",
    "chamber_pressure_pa",
    "rf_power_w",
    "gas_flow_sccm",
    "vibration_g",
]

baseline_x = sensor_df[features].iloc[:120]
all_x = sensor_df[features]

scaler = StandardScaler()
baseline_scaled = scaler.fit_transform(baseline_x)
all_scaled = scaler.transform(all_x)

pca = PCA(n_components=2, random_state=42)
baseline_score = pca.fit_transform(baseline_scaled)
all_score = pca.transform(all_scaled)

center = baseline_score.mean(axis=0)
baseline_distance = np.linalg.norm(
    baseline_score - center,
    axis=1,
)
threshold = np.quantile(baseline_distance, 0.99)

sensor_df["pca_distance"] = np.linalg.norm(
    all_score - center,
    axis=1,
)
sensor_df["pca_distance_alarm"] = (
    sensor_df["pca_distance"] > threshold
)

print("PCA 거리 기준:", round(threshold, 4))
print(
    "PCA 거리 경보 수:",
    int(sensor_df["pca_distance_alarm"].sum()),
)
