# 실습 155 — low_yield_segment_error

## 1. 학습 목표
저수율 구간에서 모델 오차를 별도로 평가합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
RandomForestRegressor 예측 결과에서 실제 수율 92% 미만을 low_yield로 정의하라.
전체 MAE와 저수율 MAE, 고수율 MAE를 비교해 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage08
python examples\ex155_low_yield_segment_error.py
```

## 4. 예상 결과
전체와 저수율 구간의 예측오차가 별도로 비교됩니다.

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
| 17 | `from sklearn.metrics import mean_absolute_error` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 18 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 19 | `from sklearn.pipeline import Pipeline` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 20 | `from sklearn.preprocessing import OneHotEncoder` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 21 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 22 | `sensor_df = pd.read_csv(DATA_FILE)` | 수율 예측용 CSV를 DataFrame으로 읽습니다. |
| 23 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 24 | `x = sensor_df.drop(columns=["timestamp", "lot_id", "yield_percent"])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `y = sensor_df["yield_percent"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 27 | `x_train, x_test, y_train, y_test = train_test_split(` | 학습용 데이터와 평가용 데이터를 분리합니다. |
| 28 | `    x, y, test_size=0.25, random_state=42` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `)` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 30 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 31 | `numeric_features = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `    "temp_mean_c",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 33 | `    "temp_std_c",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 34 | `    "pressure_mean_pa",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 35 | `    "pressure_std_pa",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 36 | `    "rf_power_mean_w",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 37 | `    "gas_flow_mean_sccm",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 38 | `    "vibration_rms_g",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 39 | `    "particle_mean",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 40 | `    "downtime_min",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 41 | `    "maintenance_age_hours",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 42 | `]` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 43 | `categorical_features = ["recipe", "chamber_id"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 44 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 45 | `preprocessor = ColumnTransformer([` | 숫자형과 범주형 컬럼의 전처리를 하나로 묶습니다. |
| 46 | `    ("num", "passthrough", numeric_features),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 47 | `    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 48 | `])` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 49 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 50 | `model = Pipeline([` | 전처리와 회귀 모델을 하나의 파이프라인으로 연결합니다. |
| 51 | `    ("preprocess", preprocessor),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 52 | `    (` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 53 | `        "regressor",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 54 | `        RandomForestRegressor(` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 55 | `            n_estimators=400,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 56 | `            random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 57 | `            n_jobs=-1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 58 | `        ),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 59 | `    ),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 60 | `])` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 61 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 62 | `model.fit(x_train, y_train)` | 학습 데이터로 전처리기와 회귀 모델을 학습합니다. |
| 63 | `prediction = model.predict(x_test)` | 학습된 모델로 수율을 예측합니다. |
| 64 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 65 | `low_mask = y_test < 92.0` | 계산 결과나 설정값을 변수에 저장합니다. |
| 66 | `high_mask = ~low_mask` | 계산 결과나 설정값을 변수에 저장합니다. |
| 67 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 68 | `summary_df = pd.DataFrame([` | 계산 결과나 설정값을 변수에 저장합니다. |
| 69 | `    {` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 70 | `        "segment": "all",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 71 | `        "row_count": len(y_test),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 72 | `        "mae": mean_absolute_error(y_test, prediction),` | 평균 절대 오차를 계산합니다. |
| 73 | `    },` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 74 | `    {` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 75 | `        "segment": "low_yield",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 76 | `        "row_count": int(low_mask.sum()),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 77 | `        "mae": (` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 78 | `            mean_absolute_error(y_test[low_mask], prediction[low_mask])` | 평균 절대 오차를 계산합니다. |
| 79 | `            if low_mask.any()` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 80 | `            else np.nan` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 81 | `        ),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 82 | `    },` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 83 | `    {` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 84 | `        "segment": "normal_yield",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 85 | `        "row_count": int(high_mask.sum()),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 86 | `        "mae": mean_absolute_error(y_test[high_mask], prediction[high_mask]),` | 평균 절대 오차를 계산합니다. |
| 87 | `    },` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 88 | `])` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 89 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 90 | `print(summary_df.round(4))` | 실행 결과를 콘솔에 출력합니다. |
| 91 | `summary_df.to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 92 | `    OUTPUT_DIR / "ex155_segment_error.csv",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 93 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 94 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 95 | `)` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 수율 라벨이 어떤 검사 시점과 기준으로 계산되었는가?
2. LOT·레시피·챔버 정보가 누수 없이 분할되었는가?
3. 평균 오차뿐 아니라 저수율 구간의 오차를 별도로 확인해야 하는가?