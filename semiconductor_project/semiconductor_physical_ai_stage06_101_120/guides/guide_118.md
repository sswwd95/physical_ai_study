# 실습 118 — cross_validation_f1

## 1. 학습 목표
교차검증으로 한 번의 데이터 분할에 따른 성능 변동을 줄입니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
StratifiedKFold 5분할과 cross_validate를 사용해 balanced LogisticRegression의
precision, recall, f1을 평가하라. 각 fold와 평균·표준편차를 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage06
python examples\ex118_cross_validation_f1.py
```

## 4. 예상 결과
5개 fold의 분류 성능과 평균·표준편차가 출력됩니다.

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
| 17 | `from sklearn.model_selection import StratifiedKFold, cross_validate` | 필요한 라이브러리나 모델을 불러옵니다. |
| 18 | `from sklearn.pipeline import Pipeline` | 필요한 라이브러리나 모델을 불러옵니다. |
| 19 | `from sklearn.preprocessing import OneHotEncoder, StandardScaler` | 필요한 라이브러리나 모델을 불러옵니다. |
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
| 40 | `preprocessor = ColumnTransformer([` | 숫자형과 범주형 컬럼의 전처리를 하나로 묶습니다. |
| 41 | `    ("num", StandardScaler(), numeric_features),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 42 | `    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 43 | `])` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 44 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 45 | `model = Pipeline([` | 전처리와 모델 학습 과정을 하나의 파이프라인으로 연결합니다. |
| 46 | `    ("preprocess", preprocessor),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 47 | `    (` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 48 | `        "classifier",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 49 | `        LogisticRegression(` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 50 | `            max_iter=1000,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 51 | `            class_weight="balanced",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 52 | `            random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 53 | `        ),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 54 | `    ),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 55 | `])` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 56 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 57 | `cv = StratifiedKFold(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 58 | `    n_splits=5,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 59 | `    shuffle=True,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 60 | `    random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 61 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 62 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 63 | `scores = cross_validate(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 64 | `    model,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 65 | `    x,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 66 | `    y,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 67 | `    cv=cv,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 68 | `    scoring=["precision", "recall", "f1"],` | 계산 결과나 설정값을 변수에 저장합니다. |
| 69 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 70 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 71 | `fold_df = pd.DataFrame({` | 계산 결과나 설정값을 변수에 저장합니다. |
| 72 | `    "fold": np.arange(1, 6),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 73 | `    "precision": scores["test_precision"],` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 74 | `    "recall": scores["test_recall"],` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 75 | `    "f1": scores["test_f1"],` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 76 | `})` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 77 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 78 | `summary_df = pd.DataFrame([{` | 계산 결과나 설정값을 변수에 저장합니다. |
| 79 | `    "fold": "mean",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 80 | `    "precision": fold_df["precision"].mean(),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 81 | `    "recall": fold_df["recall"].mean(),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 82 | `    "f1": fold_df["f1"].mean(),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 83 | `}, {` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 84 | `    "fold": "std",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 85 | `    "precision": fold_df["precision"].std(),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 86 | `    "recall": fold_df["recall"].std(),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 87 | `    "f1": fold_df["f1"].std(),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 88 | `}])` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 89 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 90 | `result_df = pd.concat([fold_df, summary_df], ignore_index=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 91 | `print(result_df.round(4))` | 실행 결과를 콘솔에 출력합니다. |
| 92 | `result_df.to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 93 | `    OUTPUT_DIR / "ex118_cross_validation_scores.csv",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 94 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 95 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 96 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 불량 라벨은 어떤 검사 장비와 판정 절차에서 생성되었는가?
2. LOT 단위 데이터 누수가 발생하지 않도록 어떻게 분할할 것인가?
3. 불량 미탐지와 정상 오탐 중 어느 비용이 더 큰가?