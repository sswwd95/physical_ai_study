"""
반도체 Physical AI 하네스 엔지니어링 실습 086~090
Windows 10 / Anaconda / Pandas / scikit-learn
로지스틱 회귀 기반 불량 예측
"""

from pathlib import Path
import json
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "wafer_defect_modeling.csv"
MODEL_PATH = PROJECT_ROOT / "models" / "logistic_defect_model.joblib"
META_PATH = PROJECT_ROOT / "outputs" / "logistic_model_metadata.json"
TRAIN_PATH = PROJECT_ROOT / "outputs" / "train_modeling_data.csv"
TEST_PATH = PROJECT_ROOT / "outputs" / "test_modeling_data.csv"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])
df = df.sort_values("timestamp").reset_index(drop=True)

numeric_features = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

categorical_features = [
    "recipe_id",
    "tool_id",
]

target_column = "defect_flag"

# 1. 시간 순서를 유지해 학습 70%, 테스트 30%로 분할한다.
split_index = int(len(df) * 0.70)

train_df = df.iloc[:split_index].copy()
test_df = df.iloc[split_index:].copy()

train_df.to_csv(
    TRAIN_PATH,
    index=False,
    encoding="utf-8-sig",
)
test_df.to_csv(
    TEST_PATH,
    index=False,
    encoding="utf-8-sig",
)

# 2. 숫자형·범주형 전처리 파이프라인을 정의한다.
numeric_pipeline = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="median"),
        ),
        (
            "scaler",
            StandardScaler(),
        ),
    ]
)

categorical_pipeline = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="most_frequent"),
        ),
        (
            "onehot",
            OneHotEncoder(
                handle_unknown="ignore",
                drop="first",
            ),
        ),
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        (
            "numeric",
            numeric_pipeline,
            numeric_features,
        ),
        (
            "categorical",
            categorical_pipeline,
            categorical_features,
        ),
    ],
    remainder="drop",
)

# 3. 로지스틱 회귀를 전체 파이프라인에 연결한다.
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "classifier",
            LogisticRegression(
                max_iter=2000,
                class_weight="balanced",
                random_state=42,
            ),
        ),
    ]
)

feature_columns = numeric_features + categorical_features

model.fit(
    train_df[feature_columns],
    train_df[target_column],
)

# 4. 학습 모델과 특징 계약을 저장한다.
joblib.dump(model, MODEL_PATH)

metadata = {
    "train_rows": len(train_df),
    "test_rows": len(test_df),
    "numeric_features": numeric_features,
    "categorical_features": categorical_features,
    "target_column": target_column,
    "split_strategy": "time_order_70_30",
    "classifier": "LogisticRegression",
    "class_weight": "balanced",
}

META_PATH.write_text(
    json.dumps(metadata, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print(json.dumps(metadata, ensure_ascii=False, indent=2))
print(f"[완료] 모델: {MODEL_PATH}")
print(f"[완료] 메타데이터: {META_PATH}")
