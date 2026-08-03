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

iforest_model = IsolationForest(
    n_estimators=200,
    contamination=0.1,
    random_state=42,
)
iforest_pred = iforest_model.fit_predict(x_scaled)
sensor_df["iforest_score"] = -iforest_model.score_samples(x_scaled)
sensor_df["iforest_anomaly"] = (iforest_pred == -1).astype(int)

lof_model = LocalOutlierFactor(
    n_neighbors=25,
    contamination=0.1,
)
lof_pred = lof_model.fit_predict(x_scaled)
sensor_df["lof_score"] = -lof_model.negative_outlier_factor_
sensor_df["lof_anomaly"] = (lof_pred == -1).astype(int)

ocsvm_model = OneClassSVM(
    kernel="rbf",
    gamma="scale",
    nu=0.1,
)
ocsvm_pred = ocsvm_model.fit_predict(x_scaled)
sensor_df["ocsvm_score"] = -ocsvm_model.decision_function(x_scaled)
sensor_df["ocsvm_anomaly"] = (ocsvm_pred == -1).astype(int)

sensor_df["ensemble_vote_count"] = (
    sensor_df["iforest_anomaly"]
    + sensor_df["lof_anomaly"]
    + sensor_df["ocsvm_anomaly"]
)

dashboard_columns = [
    "timestamp",
    "lot_id",
    *features,
    "iforest_score",
    "lof_score",
    "ocsvm_score",
    "iforest_anomaly",
    "lof_anomaly",
    "ocsvm_anomaly",
    "ensemble_vote_count",
    "true_anomaly",
]

sensor_df[dashboard_columns].to_csv(
    OUTPUT_DIR / "ex099_anomaly_dashboard_data.csv",
    index=False,
    encoding="utf-8-sig",
)

print(sensor_df[dashboard_columns].tail(10).round(4))
