# 실습 128 — random_forest_feature_importance

## 1. 학습 목표
Random Forest 특징 중요도를 전체 모델과 클래스 해석에 활용합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
실습 127과 같은 RandomForest를 학습하고 feature_importances_를 특징 이름과 연결하라.
중요도 상위 20개를 출력하고 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage07
python examples\ex128_random_forest_feature_importance.py
```

## 4. 예상 결과
다중 불량 분류에서 중요한 특징 순위가 저장됩니다.

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
| 17 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리나 모델을 불러옵니다. |
| 18 | `from sklearn.pipeline import Pipeline` | 필요한 라이브러리나 모델을 불러옵니다. |
| 19 | `from sklearn.preprocessing import OneHotEncoder` | 필요한 라이브러리나 모델을 불러옵니다. |
| 20 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 21 | `sensor_df = pd.read_csv(DATA_FILE)` | 다중 불량 유형 CSV를 DataFrame으로 읽습니다. |
| 22 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 23 | `x = sensor_df.drop(columns=["timestamp", "lot_id", "defect_type"])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `y = sensor_df["defect_type"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 26 | `numeric_features = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `    "chamber_temp_c",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 28 | `    "chamber_pressure_pa",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 29 | `    "rf_power_w",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 30 | `    "gas_flow_sccm",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 31 | `    "vibration_g",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 32 | `    "particle_count",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 33 | `    "etch_rate_nm_min",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 34 | `    "uniformity_percent",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 35 | `]` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 36 | `categorical_features = ["recipe", "chamber_id"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 37 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 38 | `x_train, x_test, y_train, y_test = train_test_split(` | 학습용과 평가용 데이터를 분리합니다. |
| 39 | `    x, y, test_size=0.25, random_state=42, stratify=y` | 계산 결과나 설정값을 변수에 저장합니다. |
| 40 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 41 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 42 | `preprocessor = ColumnTransformer([` | 계산 결과나 설정값을 변수에 저장합니다. |
| 43 | `    ("num", "passthrough", numeric_features),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 44 | `    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 45 | `])` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 46 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 47 | `model = Pipeline([` | 계산 결과나 설정값을 변수에 저장합니다. |
| 48 | `    ("preprocess", preprocessor),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 49 | `    (` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 50 | `        "classifier",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 51 | `        RandomForestClassifier(` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 52 | `            n_estimators=400,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 53 | `            max_depth=10,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 54 | `            min_samples_leaf=4,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 55 | `            class_weight="balanced",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 56 | `            random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 57 | `            n_jobs=-1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 58 | `        ),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 59 | `    ),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 60 | `])` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 61 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 62 | `model.fit(x_train, y_train)` | 학습 데이터로 전처리기와 모델을 학습합니다. |
| 63 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 64 | `feature_names = model.named_steps["preprocess"].get_feature_names_out()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 65 | `importance = model.named_steps["classifier"].feature_importances_` | 계산 결과나 설정값을 변수에 저장합니다. |
| 66 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 67 | `importance_df = pd.DataFrame({` | 계산 결과나 설정값을 변수에 저장합니다. |
| 68 | `    "feature": feature_names,` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 69 | `    "importance": importance,` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 70 | `}).sort_values("importance", ascending=False)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 71 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 72 | `print(importance_df.head(20).round(4))` | 실행 결과를 콘솔에 출력합니다. |
| 73 | `importance_df.to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 74 | `    OUTPUT_DIR / "ex128_rf_feature_importance.csv",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 75 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 76 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 77 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 가장 희소한 불량 유형의 재현율이 낮으면 어떤 위험이 있는가?
2. macro F1과 weighted F1 중 어떤 지표가 더 적합한가?
3. 클래스 확률이 낮을 때 보류 또는 재검사 정책을 어떻게 설계할 것인가?