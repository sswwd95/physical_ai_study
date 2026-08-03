# 실습 145 — linear_coefficients

## 1. 학습 목표
선형 회귀 계수로 수율에 영향을 주는 공정 변수를 해석합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
실습 144 모델을 학습한 뒤 feature_names_out과 회귀계수를 연결하라.
절댓값이 큰 상위 15개 특징을 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage08
python examples\ex145_linear_coefficients.py
```

## 4. 예상 결과
수율에 대한 특징별 선형 영향 방향과 크기가 출력됩니다.

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
| 16 | `from sklearn.linear_model import LinearRegression` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 17 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 18 | `from sklearn.pipeline import Pipeline` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 19 | `from sklearn.preprocessing import OneHotEncoder, StandardScaler` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
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
| 40 | `x_train, x_test, y_train, y_test = train_test_split(` | 학습용 데이터와 평가용 데이터를 분리합니다. |
| 41 | `    x, y, test_size=0.25, random_state=42` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `)` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 43 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 44 | `preprocessor = ColumnTransformer([` | 숫자형과 범주형 컬럼의 전처리를 하나로 묶습니다. |
| 45 | `    ("num", StandardScaler(), numeric_features),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 46 | `    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 47 | `])` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 48 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 49 | `model = Pipeline([` | 전처리와 회귀 모델을 하나의 파이프라인으로 연결합니다. |
| 50 | `    ("preprocess", preprocessor),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 51 | `    ("regressor", LinearRegression()),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 52 | `])` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 53 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 54 | `model.fit(x_train, y_train)` | 학습 데이터로 전처리기와 회귀 모델을 학습합니다. |
| 55 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 56 | `feature_names = model.named_steps["preprocess"].get_feature_names_out()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 57 | `coefficients = model.named_steps["regressor"].coef_` | 계산 결과나 설정값을 변수에 저장합니다. |
| 58 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 59 | `coefficient_df = pd.DataFrame({` | 계산 결과나 설정값을 변수에 저장합니다. |
| 60 | `    "feature": feature_names,` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 61 | `    "coefficient": coefficients,` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 62 | `})` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 63 | `coefficient_df["absolute_coefficient"] = coefficient_df["coefficient"].abs()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 64 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 65 | `top_df = coefficient_df.sort_values(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 66 | `    "absolute_coefficient",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 67 | `    ascending=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 68 | `).head(15)` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 69 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 70 | `print(top_df.round(4))` | 실행 결과를 콘솔에 출력합니다. |
| 71 | `top_df.to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 72 | `    OUTPUT_DIR / "ex145_linear_coefficients.csv",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 73 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 74 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 75 | `)` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 수율 라벨이 어떤 검사 시점과 기준으로 계산되었는가?
2. LOT·레시피·챔버 정보가 누수 없이 분할되었는가?
3. 평균 오차뿐 아니라 저수율 구간의 오차를 별도로 확인해야 하는가?