"""
반도체 Physical AI 하네스 엔지니어링 실습 046~050
Windows 10 / Anaconda / Pandas / scikit-learn
시계열 분할, 누출 방지, 전처리 재사용, 품질 리포트
"""

from pathlib import Path
import json
import joblib
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler

PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = PROJECT_ROOT / "outputs"
MODEL_DIR = PROJECT_ROOT / "models"
MODEL_DIR.mkdir(parents=True, exist_ok=True)

TRAIN_PATH = OUTPUT_DIR / "train.csv"
TEST_PATH = OUTPUT_DIR / "test.csv"
MODEL_PATH = MODEL_DIR / "sensor_preprocessor.joblib"
META_PATH = MODEL_DIR / "sensor_preprocessor_metadata.json"
TRANSFORMED_PATH = OUTPUT_DIR / "test_transformed.csv"

feature_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

train_df = pd.read_csv(TRAIN_PATH)
test_df = pd.read_csv(TEST_PATH)

# 1. 학습 데이터에서만 전처리 파이프라인을 fit한다.
preprocessor = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="median"),
        ),
        (
            "scaler",
            RobustScaler(),
        ),
    ]
)

preprocessor.fit(train_df[feature_columns])

# 2. 학습된 전처리 객체를 저장한다.
joblib.dump(preprocessor, MODEL_PATH)

# 3. 저장 파일을 다시 읽어 운영 상황을 모사한다.
restored = joblib.load(MODEL_PATH)

# 4. 테스트 데이터에는 transform만 적용한다.
transformed = restored.transform(
    test_df[feature_columns]
)

transformed_df = pd.DataFrame(
    transformed,
    columns=[
        f"{column}_processed"
        for column in feature_columns
    ],
)

transformed_df.insert(
    0,
    "timestamp",
    test_df["timestamp"],
)

transformed_df.to_csv(
    TRANSFORMED_PATH,
    index=False,
    encoding="utf-8-sig",
)

metadata = {
    "feature_columns": feature_columns,
    "fit_dataset": "train.csv",
    "transform_dataset": "test.csv",
    "pipeline_steps": [
        "median_imputation",
        "robust_scaling",
    ],
    "model_path": str(MODEL_PATH),
}

META_PATH.write_text(
    json.dumps(metadata, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print("[완료] 전처리 객체 저장·복원 성공")
print("모델:", MODEL_PATH)
print("변환 결과:", TRANSFORMED_PATH)
