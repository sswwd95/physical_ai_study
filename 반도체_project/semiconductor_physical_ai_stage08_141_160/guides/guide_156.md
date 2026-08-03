# 실습 156 — cross_validation_regression

## 1. 학습 목표
교차검증으로 회귀 성능의 변동성을 평가합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
RandomForestRegressor Pipeline에 KFold 5분할 cross_validate를 적용하라.
neg_mean_absolute_error, neg_root_mean_squared_error, r2를 계산하고 fold별 결과와 평균을 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage08
python examples\ex156_cross_validation_regression.py
```

## 4. 예상 결과
5개 fold의 MAE·RMSE·R²와 평균이 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "semiconductor_yield_regression.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError(` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 12 | `        "data/semiconductor_yield_regression.csv 파일이 없습니다."` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 13 | `    )` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 14 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 15 | `from sklearn.compose import ColumnTransformer` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 16 | `from sklearn.ensemble import RandomForestRegressor` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 17 | `from sklearn.model_selection import KFold, cross_validate` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 18 | `from sklearn.pipeline import Pipeline` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 19 | `from sklearn.preprocessing import OneHotEncoder` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 20 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 21 | `sensor_df = pd.read_csv(DATA_FILE)` | 수율 예측용 CSV를 DataFrame으로 읽습니다. |
| 22 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 23 | `x = sensor_df.drop(columns=["timestamp", "lot_id", "yield_percent"])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `y = sensor_df["yield_percent"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 26 | `numeric_features = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `    "temp_mean_c",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 28 | `    "temp_std_c",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 29 | `    "pressure_mean_pa",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 30 | `    "pressure_std_pa",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 31 | `    "rf_power_mean_w",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 32 | `    "gas_flow_mean_sccm",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 33 | `    "vibration_rms_g",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 34 | `    "particle_mean",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 35 | `    "downtime_min",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 36 | `    "maintenance_age_hours",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 37 | `]` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 38 | `categorical_features = ["recipe", "chamber_id"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 39 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 40 | `preprocessor = ColumnTransformer([` | 숫자형과 범주형 컬럼의 전처리를 하나로 묶습니다. |
| 41 | `    ("num", "passthrough", numeric_features),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 42 | `    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 43 | `])` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 44 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 45 | `model = Pipeline([` | 전처리와 회귀 모델을 하나의 파이프라인으로 연결합니다. |
| 46 | `    ("preprocess", preprocessor),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 47 | `    (` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 48 | `        "regressor",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 49 | `        RandomForestRegressor(` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 50 | `            n_estimators=300,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 51 | `            random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 52 | `            n_jobs=-1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 53 | `        ),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 54 | `    ),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 55 | `])` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 56 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 57 | `cv = KFold(n_splits=5, shuffle=True, random_state=42)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 58 | `scores = cross_validate(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 59 | `    model,` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 60 | `    x,` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 61 | `    y,` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 62 | `    cv=cv,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 63 | `    scoring=[` | 계산 결과나 설정값을 변수에 저장합니다. |
| 64 | `        "neg_mean_absolute_error",` | 평균 절대 오차를 계산합니다. |
| 65 | `        "neg_root_mean_squared_error",` | 제곱 오차를 이용한 RMSE 계산에 사용합니다. |
| 66 | `        "r2",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 67 | `    ],` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 68 | `)` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 69 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 70 | `fold_df = pd.DataFrame({` | 계산 결과나 설정값을 변수에 저장합니다. |
| 71 | `    "fold": np.arange(1, 6),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 72 | `    "mae": -scores["test_neg_mean_absolute_error"],` | 평균 절대 오차를 계산합니다. |
| 73 | `    "rmse": -scores["test_neg_root_mean_squared_error"],` | 제곱 오차를 이용한 RMSE 계산에 사용합니다. |
| 74 | `    "r2": scores["test_r2"],` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 75 | `})` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 76 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 77 | `summary_df = pd.DataFrame([{` | 계산 결과나 설정값을 변수에 저장합니다. |
| 78 | `    "fold": "mean",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 79 | `    "mae": fold_df["mae"].mean(),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 80 | `    "rmse": fold_df["rmse"].mean(),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 81 | `    "r2": fold_df["r2"].mean(),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 82 | `}])` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 83 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 84 | `result_df = pd.concat([fold_df, summary_df], ignore_index=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 85 | `print(result_df.round(4))` | 실행 결과를 콘솔에 출력합니다. |
| 86 | `result_df.to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 87 | `    OUTPUT_DIR / "ex156_regression_cv.csv",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 88 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 89 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 90 | `)` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 수율 라벨이 어떤 검사 시점과 기준으로 계산되었는가?
2. LOT·레시피·챔버 정보가 누수 없이 분할되었는가?
3. 평균 오차뿐 아니라 저수율 구간의 오차를 별도로 확인해야 하는가?