"""
반도체 Physical AI 하네스 엔지니어링 실습 086~090
Windows 10 / Anaconda / Pandas / scikit-learn
로지스틱 회귀 기반 불량 예측
"""

from pathlib import Path
import json
import joblib
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    average_precision_score,
    balanced_accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = PROJECT_ROOT / "models" / "logistic_defect_model.joblib"
TEST_PATH = PROJECT_ROOT / "outputs" / "test_modeling_data.csv"
PREDICTION_PATH = PROJECT_ROOT / "outputs" / "logistic_test_predictions.csv"
METRICS_PATH = PROJECT_ROOT / "outputs" / "logistic_evaluation_metrics.json"

model = joblib.load(MODEL_PATH)
test_df = pd.read_csv(TEST_PATH, parse_dates=["timestamp"])

feature_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
    "recipe_id",
    "tool_id",
]

target = test_df["defect_flag"]

# 1. 기본 임계값 0.5로 예측한다.
probability = model.predict_proba(
    test_df[feature_columns]
)[:, 1]

prediction = (probability >= 0.50).astype(int)

# 2. 분류 성능 지표를 계산한다.
tn, fp, fn, tp = confusion_matrix(
    target,
    prediction,
    labels=[0, 1],
).ravel()

metrics = {
    "threshold": 0.50,
    "accuracy": float(
        accuracy_score(target, prediction)
    ),
    "balanced_accuracy": float(
        balanced_accuracy_score(target, prediction)
    ),
    "precision": float(
        precision_score(
            target,
            prediction,
            zero_division=0,
        )
    ),
    "recall": float(
        recall_score(
            target,
            prediction,
            zero_division=0,
        )
    ),
    "f1": float(
        f1_score(
            target,
            prediction,
            zero_division=0,
        )
    ),
    "roc_auc": float(
        roc_auc_score(target, probability)
    ),
    "average_precision": float(
        average_precision_score(target, probability)
    ),
    "true_negative": int(tn),
    "false_positive": int(fp),
    "false_negative": int(fn),
    "true_positive": int(tp),
}

# 3. Wafer별 예측 결과를 저장한다.
result = test_df[
    [
        "timestamp",
        "wafer_id",
        "lot_id",
        "recipe_id",
        "tool_id",
        "defect_flag",
    ]
].copy()

result["defect_probability"] = probability
result["predicted_defect"] = prediction
result["prediction_correct"] = (
    result["defect_flag"]
    == result["predicted_defect"]
)

result.to_csv(
    PREDICTION_PATH,
    index=False,
    encoding="utf-8-sig",
)

METRICS_PATH.write_text(
    json.dumps(metrics, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print(json.dumps(metrics, ensure_ascii=False, indent=2))
print(f"[완료] 예측: {PREDICTION_PATH}")
print(f"[완료] 지표: {METRICS_PATH}")
