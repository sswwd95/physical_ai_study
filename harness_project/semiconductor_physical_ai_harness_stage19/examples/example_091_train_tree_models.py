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
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "wafer_tree_modeling.csv"
TRAIN_PATH = PROJECT_ROOT / "outputs" / "train_tree_data.csv"
TEST_PATH = PROJECT_ROOT / "outputs" / "test_tree_data.csv"
TREE_MODEL_PATH = PROJECT_ROOT / "models" / "decision_tree_model.joblib"
RF_MODEL_PATH = PROJECT_ROOT / "models" / "random_forest_model.joblib"
META_PATH = PROJECT_ROOT / "outputs" / "tree_model_metadata.json"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])
df = df.sort_values("timestamp").reset_index(drop=True)

numeric_features = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]
categorical_features = ["recipe_id", "tool_id"]
feature_columns = numeric_features + categorical_features
target_column = "defect_flag"

# 1. 시간 순서를 유지해 70/30 분할한다.
split_index = int(len(df) * 0.70)
train_df = df.iloc[:split_index].copy()
test_df = df.iloc[split_index:].copy()

train_df.to_csv(TRAIN_PATH, index=False, encoding="utf-8-sig")
test_df.to_csv(TEST_PATH, index=False, encoding="utf-8-sig")

# 2. 트리 모델용 전처리를 정의한다.
preprocessor = ColumnTransformer(
    transformers=[
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
    ],
    remainder="drop",
)

# 3. Decision Tree와 Random Forest를 학습한다.
decision_tree = Pipeline([
    ("preprocessor", preprocessor),
    (
        "classifier",
        DecisionTreeClassifier(
            max_depth=6,
            min_samples_leaf=20,
            class_weight="balanced",
            random_state=42,
        ),
    ),
])

random_forest = Pipeline([
    ("preprocessor", preprocessor),
    (
        "classifier",
        RandomForestClassifier(
            n_estimators=300,
            max_depth=10,
            min_samples_leaf=8,
            class_weight="balanced_subsample",
            random_state=42,
            n_jobs=-1,
        ),
    ),
])

decision_tree.fit(train_df[feature_columns], train_df[target_column])
random_forest.fit(train_df[feature_columns], train_df[target_column])

joblib.dump(decision_tree, TREE_MODEL_PATH)
joblib.dump(random_forest, RF_MODEL_PATH)

metadata = {
    "train_rows": len(train_df),
    "test_rows": len(test_df),
    "numeric_features": numeric_features,
    "categorical_features": categorical_features,
    "models": {
        "decision_tree": {
            "max_depth": 6,
            "min_samples_leaf": 20,
        },
        "random_forest": {
            "n_estimators": 300,
            "max_depth": 10,
            "min_samples_leaf": 8,
        },
    },
}

META_PATH.write_text(
    json.dumps(metadata, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print(json.dumps(metadata, ensure_ascii=False, indent=2))
print(f"[완료] Decision Tree: {TREE_MODEL_PATH}")
print(f"[완료] Random Forest: {RF_MODEL_PATH}")
