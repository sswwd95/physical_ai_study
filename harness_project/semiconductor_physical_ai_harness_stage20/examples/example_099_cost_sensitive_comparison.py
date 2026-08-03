"""
반도체 Physical AI 하네스 엔지니어링 실습 096~100
Windows 10 / Anaconda / Pandas / scikit-learn
불균형 데이터 처리와 001~100 통합 미니 프로젝트
"""

from pathlib import Path
import json
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import (
    average_precision_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "imbalanced_wafer_quality.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "cost_sensitive_model_comparison.csv"
MODEL_PATH = PROJECT_ROOT / "models" / "selected_cost_sensitive_model.joblib"
META_PATH = PROJECT_ROOT / "outputs" / "selected_cost_sensitive_model.json"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])
df = df.sort_values("timestamp").reset_index(drop=True)

split_index = int(len(df) * 0.70)
train_df = df.iloc[:split_index].copy()
test_df = df.iloc[split_index:].copy()

numeric_features = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]
categorical_features = ["recipe_id", "tool_id"]
feature_columns = numeric_features + categorical_features

preprocessor = ColumnTransformer([
    (
        "numeric",
        Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
        ]),
        numeric_features,
    ),
    (
        "categorical",
        Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            (
                "onehot",
                OneHotEncoder(
                    handle_unknown="ignore",
                    drop="first",
                ),
            ),
        ]),
        categorical_features,
    ),
])

class_weight_options = {
    "none": None,
    "balanced": "balanced",
    "defect_weight_5": {0: 1.0, 1: 5.0},
    "defect_weight_10": {0: 1.0, 1: 10.0},
}

rows = []
models = {}

for name, class_weight in class_weight_options.items():
    model = Pipeline([
        ("preprocessor", preprocessor),
        (
            "classifier",
            RandomForestClassifier(
                n_estimators=250,
                max_depth=10,
                min_samples_leaf=8,
                class_weight=class_weight,
                random_state=42,
                n_jobs=-1,
            ),
        ),
    ])

    model.fit(
        train_df[feature_columns],
        train_df["defect_flag"],
    )

    probability = model.predict_proba(
        test_df[feature_columns]
    )[:, 1]
    prediction = (probability >= 0.5).astype(int)

    fn = int(
        (
            (test_df["defect_flag"] == 1)
            & (prediction == 0)
        ).sum()
    )
    fp = int(
        (
            (test_df["defect_flag"] == 0)
            & (prediction == 1)
        ).sum()
    )

    weighted_cost = 5 * fn + fp

    rows.append({
        "setting": name,
        "precision": float(
            precision_score(
                test_df["defect_flag"],
                prediction,
                zero_division=0,
            )
        ),
        "recall": float(
            recall_score(
                test_df["defect_flag"],
                prediction,
                zero_division=0,
            )
        ),
        "f1": float(
            f1_score(
                test_df["defect_flag"],
                prediction,
                zero_division=0,
            )
        ),
        "roc_auc": float(
            roc_auc_score(
                test_df["defect_flag"],
                probability,
            )
        ),
        "average_precision": float(
            average_precision_score(
                test_df["defect_flag"],
                probability,
            )
        ),
        "false_negative": fn,
        "false_positive": fp,
        "weighted_cost": weighted_cost,
    })

    models[name] = model

result = pd.DataFrame(rows)

selected = (
    result.sort_values(
        ["weighted_cost", "average_precision"],
        ascending=[True, False],
    )
    .iloc[0]
)

selected_name = str(selected["setting"])
selected_model = models[selected_name]

joblib.dump(selected_model, MODEL_PATH)

result["selected"] = (
    result["setting"] == selected_name
)

result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

metadata = {
    "selected_setting": selected_name,
    "selected_weighted_cost": int(selected["weighted_cost"]),
    "selected_recall": float(selected["recall"]),
    "selected_precision": float(selected["precision"]),
    "cost_rule": "5*false_negative + 1*false_positive",
}

META_PATH.write_text(
    json.dumps(metadata, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print(result.round(5))
print()
print(json.dumps(metadata, ensure_ascii=False, indent=2))
print(f"[완료] 선택 모델: {MODEL_PATH}")
