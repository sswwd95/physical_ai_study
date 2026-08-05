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
from sklearn.metrics import confusion_matrix
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
    contamination=0.1,
    random_state=42,
)
y_pred = (model.fit_predict(x_scaled) == -1).astype(int)

tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

precision = tp / (tp + fp) if tp + fp else 0
recall = tp / (tp + fn) if tp + fn else 0
specificity = tn / (tn + fp) if tn + fp else 0
f1 = (
    2 * precision * recall / (precision + recall)
    if precision + recall
    else 0
)

report_df = pd.DataFrame([{
    "tn": tn,
    "fp": fp,
    "fn": fn,
    "tp": tp,
    "precision": precision,
    "recall": recall,
    "specificity": specificity,
    "f1": f1,
}])

print(report_df.round(4))
report_df.to_csv(
    OUTPUT_DIR / "ex096_confusion_matrix_report.csv",
    index=False,
    encoding="utf-8-sig",
)
