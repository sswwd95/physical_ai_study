# 실습 110 — random_forest_basic

## 1. 학습 목표
Random Forest로 여러 결정트리의 예측을 결합합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
RandomForestClassifier를 n_estimators=300, max_depth=8, min_samples_leaf=5,
random_state=42, n_jobs=-1로 학습하라. accuracy, precision, recall, f1을 출력하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage06
python examples\ex110_random_forest_basic.py
```

## 4. 예상 결과
여러 트리를 결합한 Random Forest의 분류 성능이 출력됩니다.

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
| 17 | `from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score` | 필요한 라이브러리나 모델을 불러옵니다. |
| 18 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리나 모델을 불러옵니다. |
| 19 | `from sklearn.pipeline import Pipeline` | 필요한 라이브러리나 모델을 불러옵니다. |
| 20 | `from sklearn.preprocessing import OneHotEncoder` | 필요한 라이브러리나 모델을 불러옵니다. |
| 21 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 22 | `sensor_df = pd.read_csv(DATA_FILE)` | 불량 분류용 CSV를 DataFrame으로 읽습니다. |
| 23 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 24 | `x = sensor_df.drop(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `    columns=["timestamp", "lot_id", "defect", "defect_type"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 27 | `y = sensor_df["defect"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 29 | `numeric_features = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `    "chamber_temp_c",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 31 | `    "chamber_pressure_pa",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 32 | `    "rf_power_w",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 33 | `    "gas_flow_sccm",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 34 | `    "vibration_g",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 35 | `    "particle_count",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 36 | `    "etch_rate_nm_min",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 37 | `    "uniformity_percent",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 38 | `]` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 39 | `categorical_features = ["recipe", "chamber_id"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 40 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 41 | `x_train, x_test, y_train, y_test = train_test_split(` | 학습용 데이터와 평가용 데이터를 분리합니다. |
| 42 | `    x, y, test_size=0.25, random_state=42, stratify=y` | 계산 결과나 설정값을 변수에 저장합니다. |
| 43 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 44 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 45 | `preprocessor = ColumnTransformer([` | 숫자형과 범주형 컬럼의 전처리를 하나로 묶습니다. |
| 46 | `    ("num", "passthrough", numeric_features),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 47 | `    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 48 | `])` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 49 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 50 | `model = Pipeline([` | 전처리와 모델 학습 과정을 하나의 파이프라인으로 연결합니다. |
| 51 | `    ("preprocess", preprocessor),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 52 | `    (` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 53 | `        "classifier",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 54 | `        RandomForestClassifier(` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 55 | `            n_estimators=300,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 56 | `            max_depth=8,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 57 | `            min_samples_leaf=5,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 58 | `            random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 59 | `            n_jobs=-1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 60 | `        ),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 61 | `    ),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 62 | `])` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 63 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 64 | `model.fit(x_train, y_train)` | 학습 데이터로 전처리 기준과 분류 모델을 학습합니다. |
| 65 | `y_pred = model.predict(x_test)` | 학습된 모델로 정상·불량 클래스를 예측합니다. |
| 66 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 67 | `print("Accuracy:", round(accuracy_score(y_test, y_pred), 4))` | 실행 결과를 콘솔에 출력합니다. |
| 68 | `print("Precision:", round(precision_score(y_test, y_pred, zero_division=0), 4))` | 실행 결과를 콘솔에 출력합니다. |
| 69 | `print("Recall:", round(recall_score(y_test, y_pred, zero_division=0), 4))` | 실행 결과를 콘솔에 출력합니다. |
| 70 | `print("F1:", round(f1_score(y_test, y_pred, zero_division=0), 4))` | 실행 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 불량 라벨은 어떤 검사 장비와 판정 절차에서 생성되었는가?
2. LOT 단위 데이터 누수가 발생하지 않도록 어떻게 분할할 것인가?
3. 불량 미탐지와 정상 오탐 중 어느 비용이 더 큰가?