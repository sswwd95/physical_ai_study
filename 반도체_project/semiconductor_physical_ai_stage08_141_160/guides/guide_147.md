# 실습 147 — lasso_regression

## 1. 학습 목표
Lasso 정규화로 중요하지 않은 특징의 계수를 0에 가깝게 만듭니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
Lasso(alpha=0.01, max_iter=5000)를 학습하라.
0이 아닌 계수 개수와 MAE, RMSE, R²를 출력하고 전체 계수를 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage08
python examples\ex147_lasso_regression.py
```

## 4. 예상 결과
Lasso의 선택된 특징 수와 회귀 성능이 출력됩니다.

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
| 16 | `from sklearn.linear_model import Lasso` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 17 | `from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 18 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 19 | `from sklearn.pipeline import Pipeline` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 20 | `from sklearn.preprocessing import OneHotEncoder, StandardScaler` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 21 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 22 | `sensor_df = pd.read_csv(DATA_FILE)` | 수율 예측용 CSV를 DataFrame으로 읽습니다. |
| 23 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 24 | `x = sensor_df.drop(columns=["timestamp", "lot_id", "yield_percent"])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `y = sensor_df["yield_percent"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 27 | `numeric_features = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `    "temp_mean_c",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 29 | `    "temp_std_c",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 30 | `    "pressure_mean_pa",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 31 | `    "pressure_std_pa",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 32 | `    "rf_power_mean_w",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 33 | `    "gas_flow_mean_sccm",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 34 | `    "vibration_rms_g",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 35 | `    "particle_mean",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 36 | `    "downtime_min",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 37 | `    "maintenance_age_hours",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 38 | `]` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 39 | `categorical_features = ["recipe", "chamber_id"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 40 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 41 | `x_train, x_test, y_train, y_test = train_test_split(` | 학습용 데이터와 평가용 데이터를 분리합니다. |
| 42 | `    x, y, test_size=0.25, random_state=42` | 계산 결과나 설정값을 변수에 저장합니다. |
| 43 | `)` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 44 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 45 | `preprocessor = ColumnTransformer([` | 숫자형과 범주형 컬럼의 전처리를 하나로 묶습니다. |
| 46 | `    ("num", StandardScaler(), numeric_features),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 47 | `    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 48 | `])` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 49 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 50 | `model = Pipeline([` | 전처리와 회귀 모델을 하나의 파이프라인으로 연결합니다. |
| 51 | `    ("preprocess", preprocessor),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 52 | `    ("regressor", Lasso(alpha=0.01, max_iter=5000)),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 53 | `])` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 54 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 55 | `model.fit(x_train, y_train)` | 학습 데이터로 전처리기와 회귀 모델을 학습합니다. |
| 56 | `prediction = model.predict(x_test)` | 학습된 모델로 수율을 예측합니다. |
| 57 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 58 | `feature_names = model.named_steps["preprocess"].get_feature_names_out()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 59 | `coefficients = model.named_steps["regressor"].coef_` | 계산 결과나 설정값을 변수에 저장합니다. |
| 60 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 61 | `coefficient_df = pd.DataFrame({` | 계산 결과나 설정값을 변수에 저장합니다. |
| 62 | `    "feature": feature_names,` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 63 | `    "coefficient": coefficients,` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 64 | `})` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 65 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 66 | `print("0이 아닌 계수 수:", int((coefficients != 0).sum()))` | 실행 결과를 콘솔에 출력합니다. |
| 67 | `print("MAE:", round(mean_absolute_error(y_test, prediction), 4))` | 평균 절대 오차를 계산합니다. |
| 68 | `print("RMSE:", round(mean_squared_error(y_test, prediction) ** 0.5, 4))` | 제곱 오차를 이용한 RMSE 계산에 사용합니다. |
| 69 | `print("R2:", round(r2_score(y_test, prediction), 4))` | 모델이 수율 변동을 얼마나 설명하는지 R²를 계산합니다. |
| 70 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 71 | `coefficient_df.to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 72 | `    OUTPUT_DIR / "ex147_lasso_coefficients.csv",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 73 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 74 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 75 | `)` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 수율 라벨이 어떤 검사 시점과 기준으로 계산되었는가?
2. LOT·레시피·챔버 정보가 누수 없이 분할되었는가?
3. 평균 오차뿐 아니라 저수율 구간의 오차를 별도로 확인해야 하는가?