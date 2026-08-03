"""
반도체 Physical AI 하네스 엔지니어링 실습 041~045
Windows 10 / Anaconda / Pandas / scikit-learn
스케일링, 파생 변수, 전처리 파이프라인
"""

from pathlib import Path
import json
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import RobustScaler
from sklearn.impute import SimpleImputer

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "equipment_sensor_log.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "preprocessed_sensor_features.csv"
META_PATH = PROJECT_ROOT / "outputs" / "preprocessing_metadata.json"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])
df = df.sort_values("timestamp").reset_index(drop=True)

# 1. 파생 변수를 먼저 만든다.
df["temperature_delta"] = df["temperature_c"].diff()
df["pressure_delta"] = df["pressure_kpa"].diff()
df["mechanical_load_index"] = (
    df["vibration_rms"] * df["motor_current_a"]
)
df["temperature_ma30"] = (
    df["temperature_c"]
    .rolling(window=30, min_periods=5)
    .mean()
)
df["vibration_std30"] = (
    df["vibration_rms"]
    .rolling(window=30, min_periods=5)
    .std()
)

feature_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
    "temperature_delta",
    "pressure_delta",
    "mechanical_load_index",
    "temperature_ma30",
    "vibration_std30",
]

# 2. 결측값 중앙값 대체와 Robust Scaling을 연결한다.
numeric_pipeline = Pipeline(
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

preprocessor = ColumnTransformer(
    transformers=[
        (
            "numeric",
            numeric_pipeline,
            feature_columns,
        )
    ],
    remainder="drop",
    verbose_feature_names_out=False,
)

# 3. 전체 파이프라인을 학습하고 변환한다.
processed_values = preprocessor.fit_transform(df)

output_columns = list(
    preprocessor.get_feature_names_out()
)

processed_df = pd.DataFrame(
    processed_values,
    columns=output_columns,
)

# 4. 추적용 메타데이터를 다시 결합한다.
processed_df.insert(0, "recipe_id", df["recipe_id"])
processed_df.insert(0, "lot_id", df["lot_id"])
processed_df.insert(0, "timestamp", df["timestamp"])

processed_df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

# 5. 입력 특징과 처리 단계를 메타데이터로 저장한다.
metadata = {
    "input_rows": len(df),
    "feature_columns": feature_columns,
    "output_feature_columns": output_columns,
    "steps": [
        "feature_engineering",
        "median_imputation",
        "robust_scaling",
    ],
    "remaining_missing_values": int(
        processed_df[output_columns]
        .isna()
        .sum()
        .sum()
    ),
}

META_PATH.write_text(
    json.dumps(metadata, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print("[전처리 파이프라인 완료]")
print("입력 행:", len(df))
print("출력 특징 수:", len(output_columns))
print("남은 결측값:", metadata["remaining_missing_values"])
print(f"[완료] 데이터: {OUTPUT_PATH}")
print(f"[완료] 메타데이터: {META_PATH}")
