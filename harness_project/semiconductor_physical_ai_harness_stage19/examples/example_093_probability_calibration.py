"""
반도체 Physical AI 하네스 엔지니어링 실습 091~095
Windows 10 / Anaconda / Pandas / scikit-learn
Decision Tree, Random Forest, 확률 보정, 특징 중요도
"""

from pathlib import Path
import json
import joblib
import numpy as np
import pandas as pd
from sklearn.calibration import CalibratedClassifierCV
from sklearn.metrics import brier_score_loss, log_loss

PROJECT_ROOT = Path(__file__).resolve().parents[1]
TRAIN_PATH = PROJECT_ROOT / "outputs" / "train_tree_data.csv"
TEST_PATH = PROJECT_ROOT / "outputs" / "test_tree_data.csv"
RF_PATH = PROJECT_ROOT / "models" / "random_forest_model.joblib"
CALIBRATED_PATH = PROJECT_ROOT / "models" / "calibrated_random_forest.joblib"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "probability_calibration_comparison.csv"
PREDICTION_PATH = PROJECT_ROOT / "outputs" / "calibrated_rf_predictions.csv"

train_df = pd.read_csv(TRAIN_PATH, parse_dates=["timestamp"])
test_df = pd.read_csv(TEST_PATH, parse_dates=["timestamp"])
rf_model = joblib.load(RF_PATH)

feature_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
    "recipe_id",
    "tool_id",
]

target = test_df["defect_flag"].to_numpy()

# 1. 원본 Random Forest 확률을 계산한다.
raw_probability = rf_model.predict_proba(
    test_df[feature_columns]
)[:, 1]

# 2. 학습 데이터 내부 3-fold isotonic 방식으로 확률을 보정한다.
calibrated = CalibratedClassifierCV(
    estimator=rf_model,
    method="isotonic",
    cv=3,
)
calibrated.fit(
    train_df[feature_columns],
    train_df["defect_flag"],
)

calibrated_probability = calibrated.predict_proba(
    test_df[feature_columns]
)[:, 1]

joblib.dump(calibrated, CALIBRATED_PATH)

# 3. Brier score와 Log loss를 비교한다.
rows = [
    {
        "model": "RandomForest_raw",
        "brier_score": float(
            brier_score_loss(target, raw_probability)
        ),
        "log_loss": float(
            log_loss(target, raw_probability, labels=[0, 1])
        ),
    },
    {
        "model": "RandomForest_isotonic_calibrated",
        "brier_score": float(
            brier_score_loss(target, calibrated_probability)
        ),
        "log_loss": float(
            log_loss(target, calibrated_probability, labels=[0, 1])
        ),
    },
]

result = pd.DataFrame(rows)
result["better_brier"] = (
    result["brier_score"]
    == result["brier_score"].min()
)

result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

prediction_df = test_df[
    [
        "timestamp",
        "wafer_id",
        "lot_id",
        "defect_flag",
    ]
].copy()
prediction_df["raw_probability"] = raw_probability
prediction_df["calibrated_probability"] = calibrated_probability

prediction_df.to_csv(
    PREDICTION_PATH,
    index=False,
    encoding="utf-8-sig",
)

print(result.round(6))
print(f"[완료] 보정 모델: {CALIBRATED_PATH}")
print(f"[완료] 비교 결과: {OUTPUT_PATH}")
