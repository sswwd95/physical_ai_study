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

iforest = (
    IsolationForest(
        n_estimators=200,
        contamination=0.1,
        random_state=42,
    ).fit_predict(x_scaled) == -1
).astype(int)

lof = (
    LocalOutlierFactor(
        n_neighbors=25,
        contamination=0.1,
    ).fit_predict(x_scaled) == -1
).astype(int)

ocsvm = (
    OneClassSVM(
        kernel="rbf",
        gamma="scale",
        nu=0.1,
    ).fit_predict(x_scaled) == -1
).astype(int)

vote_count = iforest + lof + ocsvm
ensemble = (vote_count >= 2).astype(int)

sensor_df["ensemble_vote_count"] = vote_count
sensor_df["ensemble_anomaly"] = ensemble

print("앙상블 이상 수:", int(ensemble.sum()))
print("Precision:", round(precision_score(y_true, ensemble), 4))
print("Recall:", round(recall_score(y_true, ensemble), 4))
print("F1:", round(f1_score(y_true, ensemble), 4))
