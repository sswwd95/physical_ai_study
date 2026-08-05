from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data_stage04.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_sensor_data_stage04.csv 파일이 없습니다.")

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

features = [
    "chamber_temp_c",
    "chamber_pressure_pa",
    "rf_power_w",
    "gas_flow_sccm",
    "vibration_g",
]

baseline_x = sensor_df[features].iloc[:120].to_numpy()
all_x = sensor_df[features].to_numpy()

mean_vector = baseline_x.mean(axis=0)
covariance = np.cov(baseline_x, rowvar=False)
inverse_covariance = np.linalg.pinv(covariance)

def mahalanobis_squared(row):
    difference = row - mean_vector
    return float(
        difference.T
        @ inverse_covariance
        @ difference
    )

baseline_distance = np.array([
    mahalanobis_squared(row)
    for row in baseline_x
])
all_distance = np.array([
    mahalanobis_squared(row)
    for row in all_x
])

threshold = np.quantile(baseline_distance, 0.99)
sensor_df["mahalanobis_d2"] = all_distance
sensor_df["mahalanobis_alarm"] = (
    sensor_df["mahalanobis_d2"] > threshold
)

print("Mahalanobis D² 기준:", round(threshold, 4))
print(
    "경보 수:",
    int(sensor_df["mahalanobis_alarm"].sum()),
)
