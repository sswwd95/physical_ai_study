# 실습 111 — random_forest_importance

## 1. 학습 목표
Random Forest 특징 중요도로 불량 판정에 중요한 센서를 확인합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
실습 110과 같은 RandomForest를 학습하고 feature_importances_를 특징 이름과 연결하라.
중요도가 높은 상위 15개를 출력하고 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage06
python examples\ex111_random_forest_importance.py
```

## 4. 예상 결과
불량 분류에 기여한 센서와 범주형 조건의 중요도가 출력됩니다.

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
| 21 | `sensor_df = pd.read_csv(DATA_FILE)` | 불량 분류용 CSV를 DataFrame으로 읽습니다. |
| 22 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 23 | `x = sensor_df.drop(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `    columns=["timestamp", "lot_id", "defect", "defect_type"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 26 | `y = sensor_df["defect"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 28 | `numeric_features = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `    "chamber_temp_c",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 30 | `    "chamber_pressure_pa",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 31 | `    "rf_power_w",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 32 | `    "gas_flow_sccm",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 33 | `    "vibration_g",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 34 | `    "particle_count",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 35 | `    "etch_rate_nm_min",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 36 | `    "uniformity_percent",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 37 | `]` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 38 | `categorical_features = ["recipe", "chamber_id"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 39 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 40 | `x_train, x_test, y_train, y_test = train_test_split(` | 학습용 데이터와 평가용 데이터를 분리합니다. |
| 41 | `    x, y, test_size=0.25, random_state=42, stratify=y` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 43 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 44 | `preprocessor = ColumnTransformer([` | 숫자형과 범주형 컬럼의 전처리를 하나로 묶습니다. |
| 45 | `    ("num", "passthrough", numeric_features),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 46 | `    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 47 | `])` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 48 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 49 | `model = Pipeline([` | 전처리와 모델 학습 과정을 하나의 파이프라인으로 연결합니다. |
| 50 | `    ("preprocess", preprocessor),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 51 | `    (` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 52 | `        "classifier",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 53 | `        RandomForestClassifier(` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 54 | `            n_estimators=300,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 55 | `            max_depth=8,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 56 | `            min_samples_leaf=5,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 57 | `            random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 58 | `            n_jobs=-1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 59 | `        ),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 60 | `    ),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 61 | `])` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 62 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 63 | `model.fit(x_train, y_train)` | 학습 데이터로 전처리 기준과 분류 모델을 학습합니다. |
| 64 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 65 | `feature_names = model.named_steps["preprocess"].get_feature_names_out()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 66 | `importance = model.named_steps["classifier"].feature_importances_` | 계산 결과나 설정값을 변수에 저장합니다. |
| 67 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 68 | `importance_df = pd.DataFrame({` | 계산 결과나 설정값을 변수에 저장합니다. |
| 69 | `    "feature": feature_names,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 70 | `    "importance": importance,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 71 | `}).sort_values("importance", ascending=False)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 72 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 73 | `print(importance_df.head(15).round(4))` | 실행 결과를 콘솔에 출력합니다. |
| 74 | `importance_df.to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 75 | `    OUTPUT_DIR / "ex111_random_forest_importance.csv",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 76 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 77 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 78 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 불량 라벨은 어떤 검사 장비와 판정 절차에서 생성되었는가?
2. LOT 단위 데이터 누수가 발생하지 않도록 어떻게 분할할 것인가?
3. 불량 미탐지와 정상 오탐 중 어느 비용이 더 큰가?