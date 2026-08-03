# 실습 159 — yield_prediction_output

## 1. 학습 목표
실제 수율·예측 수율·오차·저수율 경보를 포함한 현업 전달 파일을 만듭니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
튜닝된 RandomForestRegressor로 평가 데이터를 예측하라.
timestamp, lot_id, recipe, chamber_id, actual_yield, predicted_yield,
absolute_error, predicted_low_yield를 포함한 CSV를 생성하라.
predicted_low_yield 기준은 92% 미만으로 하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage08
python examples\ex159_yield_prediction_output.py
```

## 4. 예상 결과
저수율 위험 LOT를 우선 정렬한 예측 결과 CSV가 생성됩니다.

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
| 17 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 18 | `from sklearn.pipeline import Pipeline` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 19 | `from sklearn.preprocessing import OneHotEncoder` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 20 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 21 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | 수율 예측용 CSV를 DataFrame으로 읽습니다. |
| 22 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 23 | `feature_columns = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `    "recipe",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 25 | `    "chamber_id",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 26 | `    "temp_mean_c",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 27 | `    "temp_std_c",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 28 | `    "pressure_mean_pa",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 29 | `    "pressure_std_pa",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 30 | `    "rf_power_mean_w",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 31 | `    "gas_flow_mean_sccm",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 32 | `    "vibration_rms_g",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 33 | `    "particle_mean",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 34 | `    "downtime_min",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 35 | `    "maintenance_age_hours",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 36 | `]` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 37 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 38 | `x = sensor_df[feature_columns]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 39 | `y = sensor_df["yield_percent"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 40 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 41 | `train_index, test_index = train_test_split(` | 학습용 데이터와 평가용 데이터를 분리합니다. |
| 42 | `    np.arange(len(sensor_df)),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 43 | `    test_size=0.25,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 44 | `    random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 45 | `)` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 46 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 47 | `preprocessor = ColumnTransformer([` | 숫자형과 범주형 컬럼의 전처리를 하나로 묶습니다. |
| 48 | `    ("num", "passthrough", feature_columns[2:]),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 49 | `    ("cat", OneHotEncoder(handle_unknown="ignore"), feature_columns[:2]),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 50 | `])` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 51 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 52 | `model = Pipeline([` | 전처리와 회귀 모델을 하나의 파이프라인으로 연결합니다. |
| 53 | `    ("preprocess", preprocessor),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 54 | `    (` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 55 | `        "regressor",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 56 | `        RandomForestRegressor(` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 57 | `            n_estimators=400,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 58 | `            max_depth=10,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 59 | `            min_samples_leaf=4,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 60 | `            random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 61 | `            n_jobs=-1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 62 | `        ),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 63 | `    ),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 64 | `])` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 65 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 66 | `model.fit(x.iloc[train_index], y.iloc[train_index])` | 학습 데이터로 전처리기와 회귀 모델을 학습합니다. |
| 67 | `prediction = model.predict(x.iloc[test_index])` | 학습된 모델로 수율을 예측합니다. |
| 68 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 69 | `result_df = sensor_df.iloc[test_index][` | 계산 결과나 설정값을 변수에 저장합니다. |
| 70 | `    ["timestamp", "lot_id", "recipe", "chamber_id"]` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 71 | `].copy()` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 72 | `result_df["actual_yield"] = y.iloc[test_index].to_numpy()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 73 | `result_df["predicted_yield"] = prediction` | 계산 결과나 설정값을 변수에 저장합니다. |
| 74 | `result_df["absolute_error"] = np.abs(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 75 | `    result_df["actual_yield"] - result_df["predicted_yield"]` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 76 | `)` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 77 | `result_df["predicted_low_yield"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 78 | `    result_df["predicted_yield"] < 92.0` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 79 | `)` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 80 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 81 | `result_df = result_df.sort_values("predicted_yield")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 82 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 83 | `print(result_df.head(20).round(3))` | 실행 결과를 콘솔에 출력합니다. |
| 84 | `result_df.to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 85 | `    OUTPUT_DIR / "ex159_yield_predictions.csv",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 86 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 87 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 88 | `)` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 수율 라벨이 어떤 검사 시점과 기준으로 계산되었는가?
2. LOT·레시피·챔버 정보가 누수 없이 분할되었는가?
3. 평균 오차뿐 아니라 저수율 구간의 오차를 별도로 확인해야 하는가?