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
from sklearn.neighbors import LocalOutlierFactor
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
y_true = sensor_df["true_anomaly"].to_numpy()

predictions = {
    "IsolationForest": (
        IsolationForest(
            n_estimators=200,
            contamination=0.1,
            random_state=42,
        ).fit_predict(x_scaled) == -1
    ).astype(int),
    "LOF": (
        LocalOutlierFactor(
            n_neighbors=25,
            contamination=0.1,
        ).fit_predict(x_scaled) == -1
    ).astype(int),
    "OneClassSVM": (
        OneClassSVM(
            kernel="rbf",
            gamma="scale",
            nu=0.1,
        ).fit_predict(x_scaled) == -1
    ).astype(int),
}

rows = []
for name, y_pred in predictions.items():
    rows.append({
        "model": name,
        "predicted_count": int(y_pred.sum()),
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "f1": f1_score(y_true, y_pred, zero_division=0),
    })

result_df = pd.DataFrame(rows).sort_values("f1", ascending=False)
print(result_df.round(4))
result_df.to_csv(
    OUTPUT_DIR / "ex095_model_metric_comparison.csv",
    index=False,
    encoding="utf-8-sig",
)
