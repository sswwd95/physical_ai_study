# 실습 135 — confusion_matrix_table

## 1. 학습 목표
혼동행렬을 라벨이 있는 표로 만들어 오분류 방향을 분석합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
RandomForest 예측으로 confusion_matrix를 계산하라.
행은 actual_, 열은 predicted_ 접두사를 붙인 DataFrame으로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage07
python examples\ex135_confusion_matrix_table.py
```

## 4. 예상 결과
어떤 불량 유형이 어떤 클래스로 잘못 분류되는지 표로 확인할 수 있습니다.

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
| 15 | `from sklearn.compose import ColumnTransformer` | 필요한 라이브러리나 모델을 불러옵니다. |
| 16 | `from sklearn.ensemble import RandomForestClassifier` | 필요한 라이브러리나 모델을 불러옵니다. |
| 17 | `from sklearn.metrics import confusion_matrix` | 필요한 라이브러리나 모델을 불러옵니다. |
| 18 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리나 모델을 불러옵니다. |
| 19 | `from sklearn.pipeline import Pipeline` | 필요한 라이브러리나 모델을 불러옵니다. |
| 20 | `from sklearn.preprocessing import OneHotEncoder` | 필요한 라이브러리나 모델을 불러옵니다. |
| 21 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 22 | `sensor_df = pd.read_csv(DATA_FILE)` | 다중 불량 유형 CSV를 DataFrame으로 읽습니다. |
| 23 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 24 | `x = sensor_df.drop(columns=["timestamp", "lot_id", "defect_type"])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `y = sensor_df["defect_type"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 27 | `numeric_features = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `    "chamber_temp_c",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 29 | `    "chamber_pressure_pa",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 30 | `    "rf_power_w",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 31 | `    "gas_flow_sccm",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 32 | `    "vibration_g",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 33 | `    "particle_count",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 34 | `    "etch_rate_nm_min",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 35 | `    "uniformity_percent",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 36 | `]` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 37 | `categorical_features = ["recipe", "chamber_id"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 38 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 39 | `x_train, x_test, y_train, y_test = train_test_split(` | 학습용과 평가용 데이터를 분리합니다. |
| 40 | `    x, y, test_size=0.25, random_state=42, stratify=y` | 계산 결과나 설정값을 변수에 저장합니다. |
| 41 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 42 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 43 | `preprocessor = ColumnTransformer([` | 계산 결과나 설정값을 변수에 저장합니다. |
| 44 | `    ("num", "passthrough", numeric_features),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 45 | `    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 46 | `])` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 47 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 48 | `model = Pipeline([` | 계산 결과나 설정값을 변수에 저장합니다. |
| 49 | `    ("preprocess", preprocessor),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 50 | `    (` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 51 | `        "classifier",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 52 | `        RandomForestClassifier(` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 53 | `            n_estimators=300,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 54 | `            class_weight="balanced",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 55 | `            random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 56 | `            n_jobs=-1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 57 | `        ),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 58 | `    ),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 59 | `])` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 60 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 61 | `model.fit(x_train, y_train)` | 학습 데이터로 전처리기와 모델을 학습합니다. |
| 62 | `y_pred = model.predict(x_test)` | 학습된 모델로 불량 유형을 예측합니다. |
| 63 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 64 | `labels = model.named_steps["classifier"].classes_` | 계산 결과나 설정값을 변수에 저장합니다. |
| 65 | `matrix = confusion_matrix(y_test, y_pred, labels=labels)` | 실제 클래스와 예측 클래스의 조합을 표로 계산합니다. |
| 66 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 67 | `matrix_df = pd.DataFrame(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 68 | `    matrix,` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 69 | `    index=[f"actual_{label}" for label in labels],` | 계산 결과나 설정값을 변수에 저장합니다. |
| 70 | `    columns=[f"predicted_{label}" for label in labels],` | 계산 결과나 설정값을 변수에 저장합니다. |
| 71 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 72 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 73 | `print(matrix_df)` | 실행 결과를 콘솔에 출력합니다. |
| 74 | `matrix_df.to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 75 | `    OUTPUT_DIR / "ex135_confusion_matrix.csv",` | 실제 클래스와 예측 클래스의 조합을 표로 계산합니다. |
| 76 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 77 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 가장 희소한 불량 유형의 재현율이 낮으면 어떤 위험이 있는가?
2. macro F1과 weighted F1 중 어떤 지표가 더 적합한가?
3. 클래스 확률이 낮을 때 보류 또는 재검사 정책을 어떻게 설계할 것인가?