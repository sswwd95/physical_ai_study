# 실습 113 — manual_oversampling

## 1. 학습 목표
학습 데이터에서 불량 샘플을 단순 복제해 클래스 균형을 맞춥니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
외부 라이브러리 없이 pandas로 불량 클래스 행을 복원추출하여 정상 클래스 수와 같게 만들라.
오버샘플링 전후 클래스 건수를 출력하고 LogisticRegression으로 성능을 평가하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage06
python examples\ex113_manual_oversampling.py
```

## 4. 예상 결과
학습 데이터의 클래스 균형이 맞춰지고 평가 성능이 출력됩니다.

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
| 16 | `from sklearn.linear_model import LogisticRegression` | 필요한 라이브러리나 모델을 불러옵니다. |
| 17 | `from sklearn.metrics import precision_score, recall_score, f1_score` | 필요한 라이브러리나 모델을 불러옵니다. |
| 18 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리나 모델을 불러옵니다. |
| 19 | `from sklearn.pipeline import Pipeline` | 필요한 라이브러리나 모델을 불러옵니다. |
| 20 | `from sklearn.preprocessing import OneHotEncoder, StandardScaler` | 필요한 라이브러리나 모델을 불러옵니다. |
| 21 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 22 | `sensor_df = pd.read_csv(DATA_FILE)` | 불량 분류용 CSV를 DataFrame으로 읽습니다. |
| 23 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 24 | `x = sensor_df.drop(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `    columns=["timestamp", "lot_id", "defect", "defect_type"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 27 | `y = sensor_df["defect"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 29 | `x_train, x_test, y_train, y_test = train_test_split(` | 학습용 데이터와 평가용 데이터를 분리합니다. |
| 30 | `    x, y, test_size=0.25, random_state=42, stratify=y` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 32 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 33 | `train_df = x_train.copy()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 34 | `train_df["defect"] = y_train.values` | 계산 결과나 설정값을 변수에 저장합니다. |
| 35 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 36 | `normal_df = train_df.loc[train_df["defect"] == 0]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 37 | `defect_df = train_df.loc[train_df["defect"] == 1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 38 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 39 | `defect_oversampled = defect_df.sample(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 40 | `    n=len(normal_df),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 41 | `    replace=True,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `    random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 43 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 44 | `balanced_df = pd.concat(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 45 | `    [normal_df, defect_oversampled],` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 46 | `    ignore_index=True,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 47 | `).sample(frac=1, random_state=42)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 48 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 49 | `x_train_balanced = balanced_df.drop(columns=["defect"])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 50 | `y_train_balanced = balanced_df["defect"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 51 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 52 | `print("오버샘플링 전:")` | 실행 결과를 콘솔에 출력합니다. |
| 53 | `print(y_train.value_counts())` | 실행 결과를 콘솔에 출력합니다. |
| 54 | `print("\n오버샘플링 후:")` | 실행 결과를 콘솔에 출력합니다. |
| 55 | `print(y_train_balanced.value_counts())` | 실행 결과를 콘솔에 출력합니다. |
| 56 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 57 | `numeric_features = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 58 | `    "chamber_temp_c",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 59 | `    "chamber_pressure_pa",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 60 | `    "rf_power_w",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 61 | `    "gas_flow_sccm",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 62 | `    "vibration_g",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 63 | `    "particle_count",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 64 | `    "etch_rate_nm_min",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 65 | `    "uniformity_percent",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 66 | `]` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 67 | `categorical_features = ["recipe", "chamber_id"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 68 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 69 | `preprocessor = ColumnTransformer([` | 숫자형과 범주형 컬럼의 전처리를 하나로 묶습니다. |
| 70 | `    ("num", StandardScaler(), numeric_features),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 71 | `    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 72 | `])` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 73 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 74 | `model = Pipeline([` | 전처리와 모델 학습 과정을 하나의 파이프라인으로 연결합니다. |
| 75 | `    ("preprocess", preprocessor),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 76 | `    ("classifier", LogisticRegression(max_iter=1000, random_state=42)),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 77 | `])` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 78 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 79 | `model.fit(x_train_balanced, y_train_balanced)` | 학습 데이터로 전처리 기준과 분류 모델을 학습합니다. |
| 80 | `y_pred = model.predict(x_test)` | 학습된 모델로 정상·불량 클래스를 예측합니다. |
| 81 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 82 | `print("Precision:", round(precision_score(y_test, y_pred, zero_division=0), 4))` | 실행 결과를 콘솔에 출력합니다. |
| 83 | `print("Recall:", round(recall_score(y_test, y_pred, zero_division=0), 4))` | 실행 결과를 콘솔에 출력합니다. |
| 84 | `print("F1:", round(f1_score(y_test, y_pred, zero_division=0), 4))` | 실행 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 불량 라벨은 어떤 검사 장비와 판정 절차에서 생성되었는가?
2. LOT 단위 데이터 누수가 발생하지 않도록 어떻게 분할할 것인가?
3. 불량 미탐지와 정상 오탐 중 어느 비용이 더 큰가?