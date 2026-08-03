# 실습 133 — stratified_cross_validation

## 1. 학습 목표
StratifiedKFold로 다중 클래스 모델 성능의 변동성을 평가합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
RandomForest Pipeline에 StratifiedKFold 5분할과 cross_validate를 적용하라.
accuracy, f1_macro, f1_weighted를 계산하고 fold별 결과와 평균·표준편차를 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage07
python examples\ex133_stratified_cross_validation.py
```

## 4. 예상 결과
5개 fold의 다중 클래스 성능과 평균·표준편차가 저장됩니다.

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
| 17 | `from sklearn.model_selection import StratifiedKFold, cross_validate` | 필요한 라이브러리나 모델을 불러옵니다. |
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
| 38 | `preprocessor = ColumnTransformer([` | 계산 결과나 설정값을 변수에 저장합니다. |
| 39 | `    ("num", "passthrough", numeric_features),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 40 | `    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 41 | `])` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 42 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 43 | `model = Pipeline([` | 계산 결과나 설정값을 변수에 저장합니다. |
| 44 | `    ("preprocess", preprocessor),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 45 | `    (` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 46 | `        "classifier",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 47 | `        RandomForestClassifier(` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 48 | `            n_estimators=300,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 49 | `            class_weight="balanced",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 50 | `            random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 51 | `            n_jobs=-1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 52 | `        ),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 53 | `    ),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 54 | `])` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 55 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 56 | `cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 57 | `scores = cross_validate(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 58 | `    model,` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 59 | `    x,` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 60 | `    y,` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 61 | `    cv=cv,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 62 | `    scoring=["accuracy", "f1_macro", "f1_weighted"],` | 계산 결과나 설정값을 변수에 저장합니다. |
| 63 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 64 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 65 | `fold_df = pd.DataFrame({` | 계산 결과나 설정값을 변수에 저장합니다. |
| 66 | `    "fold": np.arange(1, 6),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 67 | `    "accuracy": scores["test_accuracy"],` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 68 | `    "macro_f1": scores["test_f1_macro"],` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 69 | `    "weighted_f1": scores["test_f1_weighted"],` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 70 | `})` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 71 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 72 | `summary_df = pd.DataFrame([` | 계산 결과나 설정값을 변수에 저장합니다. |
| 73 | `    {` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 74 | `        "fold": "mean",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 75 | `        "accuracy": fold_df["accuracy"].mean(),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 76 | `        "macro_f1": fold_df["macro_f1"].mean(),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 77 | `        "weighted_f1": fold_df["weighted_f1"].mean(),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 78 | `    },` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 79 | `    {` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 80 | `        "fold": "std",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 81 | `        "accuracy": fold_df["accuracy"].std(),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 82 | `        "macro_f1": fold_df["macro_f1"].std(),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 83 | `        "weighted_f1": fold_df["weighted_f1"].std(),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 84 | `    },` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 85 | `])` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 86 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 87 | `result_df = pd.concat([fold_df, summary_df], ignore_index=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 88 | `print(result_df.round(4))` | 실행 결과를 콘솔에 출력합니다. |
| 89 | `result_df.to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 90 | `    OUTPUT_DIR / "ex133_multiclass_cv.csv",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 91 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 92 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 93 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 가장 희소한 불량 유형의 재현율이 낮으면 어떤 위험이 있는가?
2. macro F1과 weighted F1 중 어떤 지표가 더 적합한가?
3. 클래스 확률이 낮을 때 보류 또는 재검사 정책을 어떻게 설계할 것인가?