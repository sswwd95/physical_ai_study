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
y_true = sensor_df["true_anomaly"].to_numpy()

predictions = {}

iforest_model = IsolationForest(
    n_estimators=200,
    contamination=0.1,
    random_state=42,
)
predictions["IsolationForest"] = (
    iforest_model.fit_predict(x_scaled) == -1
).astype(int)

lof_model = LocalOutlierFactor(
    n_neighbors=25,
    contamination=0.1,
)
predictions["LOF"] = (
    lof_model.fit_predict(x_scaled) == -1
).astype(int)

ocsvm_model = OneClassSVM(
    kernel="rbf",
    gamma="scale",
    nu=0.1,
)
predictions["OneClassSVM"] = (
    ocsvm_model.fit_predict(x_scaled) == -1
).astype(int)

vote_count = sum(predictions.values())
predictions["Ensemble"] = (
    vote_count >= 2
).astype(int)

metric_rows = []
for model_name, y_pred in predictions.items():
    metric_rows.append({
        "model": model_name,
        "predicted_count": int(y_pred.sum()),
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "f1": f1_score(y_true, y_pred, zero_division=0),
    })
    sensor_df[f"{model_name}_anomaly"] = y_pred

metrics_df = pd.DataFrame(metric_rows).sort_values(
    "f1",
    ascending=False,
)

sensor_df["ensemble_vote_count"] = vote_count
anomaly_df = sensor_df.loc[
    sensor_df["Ensemble_anomaly"] == 1
].copy()

lot_summary = (
    sensor_df.groupby("lot_id")
    .agg(
        row_count=("timestamp", "size"),
        true_anomaly_count=("true_anomaly", "sum"),
        ensemble_anomaly_count=("Ensemble_anomaly", "sum"),
    )
    .reset_index()
)
lot_summary["ensemble_anomaly_rate"] = (
    lot_summary["ensemble_anomaly_count"]
    / lot_summary["row_count"]
)

excel_file = OUTPUT_DIR / "ex100_automated_anomaly_report.xlsx"
with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
    metrics_df.to_excel(writer, sheet_name="model_metrics", index=False)
    anomaly_df.to_excel(writer, sheet_name="anomaly_rows", index=False)
    lot_summary.to_excel(writer, sheet_name="lot_summary", index=False)

metrics_df.to_csv(
    OUTPUT_DIR / "ex100_model_metrics.csv",
    index=False,
    encoding="utf-8-sig",
)

print(metrics_df.round(4))
print("보고서 저장:", excel_file)
