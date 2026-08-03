from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_anomaly_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_anomaly_data.csv 파일이 없습니다.")

from sklearn.covariance import MinCovDet
from sklearn.preprocessing import StandardScaler

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

model = MinCovDet(random_state=42).fit(x_scaled)
distance_squared = model.mahalanobis(x_scaled)
threshold = np.quantile(distance_squared, 0.975)

sensor_df["robust_mahalanobis_d2"] = distance_squared
sensor_df["robust_covariance_anomaly"] = (
    distance_squared > threshold
).astype(int)

print("임계값:", round(threshold, 4))
print(
    "Robust Covariance 이상 수:",
    int(sensor_df["robust_covariance_anomaly"].sum()),
)
