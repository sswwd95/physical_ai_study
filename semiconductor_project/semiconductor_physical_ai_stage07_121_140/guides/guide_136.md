# 실습 136 — probability_calibration

## 1. 학습 목표
CalibratedClassifierCV로 다중 클래스 예측확률을 보정합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
RandomForest Pipeline을 CalibratedClassifierCV(method='sigmoid', cv=3)로 감싸 학습하라.
평가 데이터의 log_loss와 각 클래스 평균 예측확률을 출력하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage07
python examples\ex136_probability_calibration.py
```

## 4. 예상 결과
보정된 다중 클래스 확률의 log loss와 평균 확률이 출력됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 모델을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 모델을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 모델을 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "semiconductor_multiclass_defects.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError(` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 12 | `        "data/semiconductor_multiclass_defects.csv 파일이 없습니다."` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 13 | `    )` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 14 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 15 | `from sklearn.calibration import CalibratedClassifierCV` | 필요한 라이브러리나 모델을 불러옵니다. |
| 16 | `from sklearn.compose import ColumnTransformer` | 필요한 라이브러리나 모델을 불러옵니다. |
| 17 | `from sklearn.ensemble import RandomForestClassifier` | 필요한 라이브러리나 모델을 불러옵니다. |
| 18 | `from sklearn.metrics import log_loss` | 필요한 라이브러리나 모델을 불러옵니다. |
| 19 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리나 모델을 불러옵니다. |
| 20 | `from sklearn.pipeline import Pipeline` | 필요한 라이브러리나 모델을 불러옵니다. |
| 21 | `from sklearn.preprocessing import OneHotEncoder` | 필요한 라이브러리나 모델을 불러옵니다. |
| 22 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 23 | `sensor_df = pd.read_csv(DATA_FILE)` | 다중 불량 유형 CSV를 DataFrame으로 읽습니다. |
| 24 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 25 | `x = sensor_df.drop(columns=["timestamp", "lot_id", "defect_type"])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `y = sensor_df["defect_type"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 28 | `numeric_features = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `    "chamber_temp_c",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 30 | `    "chamber_pressure_pa",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 31 | `    "rf_power_w",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 32 | `    "gas_flow_sccm",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 33 | `    "vibration_g",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 34 | `    "particle_count",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 35 | `    "etch_rate_nm_min",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 36 | `    "uniformity_percent",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 37 | `]` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 38 | `categorical_features = ["recipe", "chamber_id"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 39 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 40 | `x_train, x_test, y_train, y_test = train_test_split(` | 학습용과 평가용 데이터를 분리합니다. |
| 41 | `    x, y, test_size=0.25, random_state=42, stratify=y` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 43 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 44 | `preprocessor = ColumnTransformer([` | 계산 결과나 설정값을 변수에 저장합니다. |
| 45 | `    ("num", "passthrough", numeric_features),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 46 | `    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 47 | `])` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 48 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 49 | `base_pipeline = Pipeline([` | 계산 결과나 설정값을 변수에 저장합니다. |
| 50 | `    ("preprocess", preprocessor),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 51 | `    (` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 52 | `        "classifier",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 53 | `        RandomForestClassifier(` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 54 | `            n_estimators=300,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 55 | `            class_weight="balanced",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 56 | `            random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 57 | `            n_jobs=-1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 58 | `        ),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 59 | `    ),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 60 | `])` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 61 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 62 | `calibrated_model = CalibratedClassifierCV(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 63 | `    estimator=base_pipeline,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 64 | `    method="sigmoid",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 65 | `    cv=3,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 66 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 67 | `calibrated_model.fit(x_train, y_train)` | 학습 데이터로 전처리기와 모델을 학습합니다. |
| 68 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 69 | `probability = calibrated_model.predict_proba(x_test)` | 각 불량 유형에 속할 확률을 계산합니다. |
| 70 | `print("Log loss:", round(log_loss(y_test, probability), 4))` | 실행 결과를 콘솔에 출력합니다. |
| 71 | `print("클래스 순서:", calibrated_model.classes_)` | 실행 결과를 콘솔에 출력합니다. |
| 72 | `print(` | 실행 결과를 콘솔에 출력합니다. |
| 73 | `    "평균 예측확률:",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 74 | `    np.round(probability.mean(axis=0), 4),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 75 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 가장 희소한 불량 유형의 재현율이 낮으면 어떤 위험이 있는가?
2. macro F1과 weighted F1 중 어떤 지표가 더 적합한가?
3. 클래스 확률이 낮을 때 보류 또는 재검사 정책을 어떻게 설계할 것인가?