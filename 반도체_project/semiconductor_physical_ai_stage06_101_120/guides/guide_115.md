# 실습 115 — confusion_matrix_analysis

## 1. 학습 목표
혼동행렬로 정상 오탐과 불량 미탐을 구분합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
RandomForest 모델의 confusion_matrix를 계산하라.
TN, FP, FN, TP를 한 행의 DataFrame으로 만들고 specificity, false_negative_rate를 함께 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage06
python examples\ex115_confusion_matrix_analysis.py
```

## 4. 예상 결과
정상 오탐과 불량 미탐을 분리한 혼동행렬 지표가 생성됩니다.

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
| 17 | `from sklearn.metrics import confusion_matrix` | 필요한 라이브러리나 모델을 불러옵니다. |
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
| 56 | `            class_weight="balanced",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 57 | `            random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 58 | `            n_jobs=-1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 59 | `        ),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 60 | `    ),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 61 | `])` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 62 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 63 | `model.fit(x_train, y_train)` | 학습 데이터로 전처리 기준과 분류 모델을 학습합니다. |
| 64 | `y_pred = model.predict(x_test)` | 학습된 모델로 정상·불량 클래스를 예측합니다. |
| 65 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 66 | `tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()` | 정상·불량 예측의 네 가지 경우를 표로 계산합니다. |
| 67 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 68 | `report_df = pd.DataFrame([{` | 계산 결과나 설정값을 변수에 저장합니다. |
| 69 | `    "tn": tn,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 70 | `    "fp": fp,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 71 | `    "fn": fn,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 72 | `    "tp": tp,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 73 | `    "specificity": tn / (tn + fp) if tn + fp else 0,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 74 | `    "false_negative_rate": fn / (fn + tp) if fn + tp else 0,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 75 | `}])` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 76 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 77 | `print(report_df.round(4))` | 실행 결과를 콘솔에 출력합니다. |
| 78 | `report_df.to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 79 | `    OUTPUT_DIR / "ex115_confusion_matrix_analysis.csv",` | 정상·불량 예측의 네 가지 경우를 표로 계산합니다. |
| 80 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 81 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 82 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 불량 라벨은 어떤 검사 장비와 판정 절차에서 생성되었는가?
2. LOT 단위 데이터 누수가 발생하지 않도록 어떻게 분할할 것인가?
3. 불량 미탐지와 정상 오탐 중 어느 비용이 더 큰가?