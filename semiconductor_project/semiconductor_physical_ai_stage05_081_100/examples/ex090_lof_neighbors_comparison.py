from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_anomaly_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_anomaly_data.csv 파일이 없습니다.")

from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.neighbors import LocalOutlierFactor
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
y_true = sensor_df["true_anomaly"].to_numpy()

rows = []
for neighbors in [10, 20, 30, 50]:
    model = LocalOutlierFactor(
        n_neighbors=neighbors,
        contamination=0.1,
    )
    y_pred = (model.fit_predict(x_scaled) == -1).astype(int)
    rows.append({
        "n_neighbors": neighbors,
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "f1": f1_score(y_true, y_pred, zero_division=0),
    })

result_df = pd.DataFrame(rows)
print(result_df.round(4))
result_df.to_csv(
    OUTPUT_DIR / "ex090_lof_neighbors_comparison.csv",
    index=False,
    encoding="utf-8-sig",
)
