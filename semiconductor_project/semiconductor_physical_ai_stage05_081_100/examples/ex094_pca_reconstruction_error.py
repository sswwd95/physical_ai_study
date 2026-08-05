from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_anomaly_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_anomaly_data.csv 파일이 없습니다.")

from sklearn.decomposition import PCA
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

pca = PCA(n_components=3, random_state=42)
score = pca.fit_transform(x_scaled)
reconstructed = pca.inverse_transform(score)

error = np.mean(
    (x_scaled - reconstructed) ** 2,
    axis=1,
)
threshold = np.quantile(error, 0.975)

sensor_df["pca_reconstruction_error"] = error
sensor_df["pca_reconstruction_anomaly"] = (
    error > threshold
).astype(int)

print("PCA 재구성 이상 수:", int(
    sensor_df["pca_reconstruction_anomaly"].sum()
))
