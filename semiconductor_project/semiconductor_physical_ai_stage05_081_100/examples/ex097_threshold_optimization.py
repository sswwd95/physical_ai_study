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
from sklearn.metrics import precision_score, recall_score, f1_score
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

model = IsolationForest(
    n_estimators=200,
    contamination="auto",
    random_state=42,
).fit(x_scaled)

score = -model.score_samples(x_scaled)

rows = []
for quantile in np.arange(0.90, 1.00, 0.01):
    threshold = np.quantile(score, quantile)
    y_pred = (score >= threshold).astype(int)
    rows.append({
        "quantile": round(float(quantile), 2),
        "threshold": threshold,
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "f1": f1_score(y_true, y_pred, zero_division=0),
    })

result_df = pd.DataFrame(rows)
best_row = result_df.loc[result_df["f1"].idxmax()]

print(result_df.round(4))
print("\n최적 설정:")
print(best_row.round(4))
