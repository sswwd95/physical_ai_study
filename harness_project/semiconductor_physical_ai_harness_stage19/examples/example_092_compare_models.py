"""
반도체 Physical AI 하네스 엔지니어링 실습 091~095
Windows 10 / Anaconda / Pandas / scikit-learn
Decision Tree, Random Forest, 확률 보정, 특징 중요도
"""

from pathlib import Path
import json
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    average_precision_score,
    balanced_accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

PROJECT_ROOT = Path(__file__).resolve().parents[1]
TRAIN_PATH = PROJECT_ROOT / "outputs" / "train_tree_data.csv"
TEST_PATH = PROJECT_ROOT / "outputs" / "test_tree_data.csv"
TREE_PATH = PROJECT_ROOT / "models" / "decision_tree_model.joblib"
RF_PATH = PROJECT_ROOT / "models" / "random_forest_model.joblib"
LOGISTIC_PATH = PROJECT_ROOT / "models" / "comparison_logistic_model.joblib"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "model_comparison.csv"

train_df = pd.read_csv(TRAIN_PATH, parse_dates=["timestamp"])
test_df = pd.read_csv(TEST_PATH, parse_dates=["timestamp"])

numeric_features = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]
categorical_features = ["recipe_id", "tool_id"]
feature_columns = numeric_features + categorical_features
target = test_df["defect_flag"]

# 1. 비교 기준인 로지스틱 회귀를 같은 데이터 분할로 학습한다.
logistic_preprocessor = ColumnTransformer(
    transformers=[
        (
            "numeric",
            Pipeline([
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler()),
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
    ]
)

logistic_model = Pipeline([
    ("preprocessor", logistic_preprocessor),
    (
        "classifier",
        LogisticRegression(
            max_iter=2000,
            class_weight="balanced",
            random_state=42,
        ),
    ),
])

logistic_model.fit(
    train_df[feature_columns],
    train_df["defect_flag"],
)
joblib.dump(logistic_model, LOGISTIC_PATH)

models = {
    "LogisticRegression": logistic_model,
    "DecisionTree": joblib.load(TREE_PATH),
    "RandomForest": joblib.load(RF_PATH),
}

rows = []

# 2. 동일 테스트셋과 임계값 0.5에서 성능을 비교한다.
for model_name, model in models.items():
    probability = model.predict_proba(
        test_df[feature_columns]
    )[:, 1]
    prediction = (probability >= 0.5).astype(int)

    rows.append({
        "model": model_name,
        "accuracy": float(accuracy_score(target, prediction)),
        "balanced_accuracy": float(
            balanced_accuracy_score(target, prediction)
        ),
        "precision": float(
            precision_score(target, prediction, zero_division=0)
        ),
        "recall": float(
            recall_score(target, prediction, zero_division=0)
        ),
        "f1": float(
            f1_score(target, prediction, zero_division=0)
        ),
        "roc_auc": float(
            roc_auc_score(target, probability)
        ),
        "average_precision": float(
            average_precision_score(target, probability)
        ),
    })

result = pd.DataFrame(rows)
result["rank_by_average_precision"] = (
    result["average_precision"]
    .rank(ascending=False, method="min")
    .astype(int)
)

result = result.sort_values(
    ["rank_by_average_precision", "roc_auc"],
    ascending=[True, False],
).reset_index(drop=True)

result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print(result.round(5))
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
