"""
반도체 Physical AI 하네스 엔지니어링 실습 086~090
Windows 10 / Anaconda / Pandas / scikit-learn
로지스틱 회귀 기반 불량 예측
"""

from pathlib import Path
import json
import numpy as np
import pandas as pd
from sklearn.metrics import (
    f1_score,
    precision_score,
    recall_score,
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PREDICTION_PATH = PROJECT_ROOT / "outputs" / "logistic_test_predictions.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "threshold_performance.csv"
BEST_PATH = PROJECT_ROOT / "outputs" / "best_threshold.json"

df = pd.read_csv(PREDICTION_PATH)

target = df["defect_flag"].to_numpy()
probability = df["defect_probability"].to_numpy()

thresholds = np.arange(
    0.10,
    0.91,
    0.05,
)

rows = []

# 1. 여러 임계값에서 precision, recall, F1을 계산한다.
for threshold in thresholds:
    prediction = (
        probability >= threshold
    ).astype(int)

    precision = precision_score(
        target,
        prediction,
        zero_division=0,
    )

    recall = recall_score(
        target,
        prediction,
        zero_division=0,
    )

    f1 = f1_score(
        target,
        prediction,
        zero_division=0,
    )

    # 2. 불량 미탐에 더 큰 비용을 주는 교육용 비용함수를 계산한다.
    false_negative = int(
        ((target == 1) & (prediction == 0)).sum()
    )
    false_positive = int(
        ((target == 0) & (prediction == 1)).sum()
    )

    weighted_cost = (
        5 * false_negative
        + 1 * false_positive
    )

    rows.append(
        {
            "threshold": float(threshold),
            "precision": float(precision),
            "recall": float(recall),
            "f1": float(f1),
            "false_negative": false_negative,
            "false_positive": false_positive,
            "weighted_cost": int(weighted_cost),
        }
    )

result = pd.DataFrame(rows)

# 3. 비용이 가장 낮고, 동률이면 F1이 높은 임계값을 선택한다.
best = (
    result.sort_values(
        ["weighted_cost", "f1"],
        ascending=[True, False],
    )
    .iloc[0]
)

result["selected"] = (
    result["threshold"]
    == best["threshold"]
)

result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

best_summary = {
    "selected_threshold": float(best["threshold"]),
    "precision": float(best["precision"]),
    "recall": float(best["recall"]),
    "f1": float(best["f1"]),
    "false_negative": int(best["false_negative"]),
    "false_positive": int(best["false_positive"]),
    "weighted_cost": int(best["weighted_cost"]),
    "cost_rule": "5*false_negative + 1*false_positive",
}

BEST_PATH.write_text(
    json.dumps(
        best_summary,
        ensure_ascii=False,
        indent=2,
    ),
    encoding="utf-8",
)

print(json.dumps(best_summary, ensure_ascii=False, indent=2))
print(f"[완료] 임계값 비교: {OUTPUT_PATH}")
print(f"[완료] 선택 결과: {BEST_PATH}")
