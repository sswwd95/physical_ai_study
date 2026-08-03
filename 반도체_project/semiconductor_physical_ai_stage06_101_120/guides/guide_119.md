# 실습 119 — defect_prediction_output

## 1. 학습 목표
모델 확률과 예측 결과를 원본 식별정보와 결합해 현업 전달용 파일을 만듭니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
balanced RandomForest를 학습하고 평가 데이터의 defect_probability와 predicted_defect를 계산하라.
timestamp, lot_id, recipe, chamber_id, actual_defect와 함께 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage06
python examples\ex119_defect_prediction_output.py
```

## 4. 예상 결과
평가 LOT의 실제 라벨, 불량확률, 예측 결과가 현업 전달용 CSV로 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 모델을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 모델을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 모델을 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "semiconductor_defect_classification.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError(` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 12 | `        "data/semiconductor_defect_classification.csv 파일이 없습니다."` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 13 | `    )` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 14 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 15 | `from sklearn.compose import ColumnTransformer` | 필요한 라이브러리나 모델을 불러옵니다. |
| 16 | `from sklearn.ensemble import RandomForestClassifier` | 필요한 라이브러리나 모델을 불러옵니다. |
| 17 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리나 모델을 불러옵니다. |
| 18 | `from sklearn.pipeline import Pipeline` | 필요한 라이브러리나 모델을 불러옵니다. |
| 19 | `from sklearn.preprocessing import OneHotEncoder` | 필요한 라이브러리나 모델을 불러옵니다. |
| 20 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 21 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | 불량 분류용 CSV를 DataFrame으로 읽습니다. |
| 22 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 23 | `feature_columns = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `    "recipe",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 25 | `    "chamber_id",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 26 | `    "chamber_temp_c",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 27 | `    "chamber_pressure_pa",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 28 | `    "rf_power_w",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 29 | `    "gas_flow_sccm",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 30 | `    "vibration_g",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 31 | `    "particle_count",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 32 | `    "etch_rate_nm_min",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 33 | `    "uniformity_percent",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 34 | `]` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 35 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 36 | `x = sensor_df[feature_columns]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 37 | `y = sensor_df["defect"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 38 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 39 | `train_index, test_index = train_test_split(` | 학습용 데이터와 평가용 데이터를 분리합니다. |
| 40 | `    np.arange(len(sensor_df)),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 41 | `    test_size=0.25,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `    random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 43 | `    stratify=y,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 44 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 45 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 46 | `x_train = x.iloc[train_index]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 47 | `x_test = x.iloc[test_index]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 48 | `y_train = y.iloc[train_index]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 49 | `y_test = y.iloc[test_index]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 50 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 51 | `numeric_features = feature_columns[2:]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 52 | `categorical_features = feature_columns[:2]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 53 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 54 | `preprocessor = ColumnTransformer([` | 숫자형과 범주형 컬럼의 전처리를 하나로 묶습니다. |
| 55 | `    ("num", "passthrough", numeric_features),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 56 | `    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 57 | `])` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 58 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 59 | `model = Pipeline([` | 전처리와 모델 학습 과정을 하나의 파이프라인으로 연결합니다. |
| 60 | `    ("preprocess", preprocessor),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 61 | `    (` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 62 | `        "classifier",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 63 | `        RandomForestClassifier(` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 64 | `            n_estimators=300,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 65 | `            class_weight="balanced",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 66 | `            random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 67 | `            n_jobs=-1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 68 | `        ),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 69 | `    ),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 70 | `])` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 71 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 72 | `model.fit(x_train, y_train)` | 학습 데이터로 전처리 기준과 분류 모델을 학습합니다. |
| 73 | `probability = model.predict_proba(x_test)[:, 1]` | 각 행이 불량일 확률을 계산합니다. |
| 74 | `prediction = (probability >= 0.4).astype(int)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 75 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 76 | `result_df = sensor_df.iloc[test_index][` | 계산 결과나 설정값을 변수에 저장합니다. |
| 77 | `    ["timestamp", "lot_id", "recipe", "chamber_id"]` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 78 | `].copy()` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 79 | `result_df["actual_defect"] = y_test.to_numpy()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 80 | `result_df["defect_probability"] = probability` | 계산 결과나 설정값을 변수에 저장합니다. |
| 81 | `result_df["predicted_defect"] = prediction` | 계산 결과나 설정값을 변수에 저장합니다. |
| 82 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 83 | `result_df = result_df.sort_values(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 84 | `    "defect_probability",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 85 | `    ascending=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 86 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 87 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 88 | `print(result_df.head(20).round(4))` | 실행 결과를 콘솔에 출력합니다. |
| 89 | `result_df.to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 90 | `    OUTPUT_DIR / "ex119_defect_predictions.csv",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 91 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 92 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 93 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 불량 라벨은 어떤 검사 장비와 판정 절차에서 생성되었는가?
2. LOT 단위 데이터 누수가 발생하지 않도록 어떻게 분할할 것인가?
3. 불량 미탐지와 정상 오탐 중 어느 비용이 더 큰가?