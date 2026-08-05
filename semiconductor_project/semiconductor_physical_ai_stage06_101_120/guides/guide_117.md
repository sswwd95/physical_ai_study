# 실습 117 — precision_recall_auc

## 1. 학습 목표
불균형 데이터에 유용한 PR-AUC를 계산합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
LogisticRegression, DecisionTree, RandomForest의 average_precision_score를 계산하라.
모델별 ROC-AUC와 PR-AUC를 함께 비교하여 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage06
python examples\ex117_precision_recall_auc.py
```

## 4. 예상 결과
불량 클래스 중심의 PR-AUC와 ROC-AUC가 함께 비교됩니다.

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
| 17 | `from sklearn.linear_model import LogisticRegression` | 필요한 라이브러리나 모델을 불러옵니다. |
| 18 | `from sklearn.metrics import average_precision_score, roc_auc_score` | 필요한 라이브러리나 모델을 불러옵니다. |
| 19 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리나 모델을 불러옵니다. |
| 20 | `from sklearn.pipeline import Pipeline` | 필요한 라이브러리나 모델을 불러옵니다. |
| 21 | `from sklearn.preprocessing import OneHotEncoder, StandardScaler` | 필요한 라이브러리나 모델을 불러옵니다. |
| 22 | `from sklearn.tree import DecisionTreeClassifier` | 필요한 라이브러리나 모델을 불러옵니다. |
| 23 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 24 | `sensor_df = pd.read_csv(DATA_FILE)` | 불량 분류용 CSV를 DataFrame으로 읽습니다. |
| 25 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 26 | `x = sensor_df.drop(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `    columns=["timestamp", "lot_id", "defect", "defect_type"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 29 | `y = sensor_df["defect"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 31 | `numeric_features = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `    "chamber_temp_c",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 33 | `    "chamber_pressure_pa",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 34 | `    "rf_power_w",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 35 | `    "gas_flow_sccm",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 36 | `    "vibration_g",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 37 | `    "particle_count",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 38 | `    "etch_rate_nm_min",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 39 | `    "uniformity_percent",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 40 | `]` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 41 | `categorical_features = ["recipe", "chamber_id"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 43 | `x_train, x_test, y_train, y_test = train_test_split(` | 학습용 데이터와 평가용 데이터를 분리합니다. |
| 44 | `    x, y, test_size=0.25, random_state=42, stratify=y` | 계산 결과나 설정값을 변수에 저장합니다. |
| 45 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 46 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 47 | `linear_preprocessor = ColumnTransformer([` | 숫자형과 범주형 컬럼의 전처리를 하나로 묶습니다. |
| 48 | `    ("num", StandardScaler(), numeric_features),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 49 | `    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 50 | `])` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 51 | `tree_preprocessor = ColumnTransformer([` | 숫자형과 범주형 컬럼의 전처리를 하나로 묶습니다. |
| 52 | `    ("num", "passthrough", numeric_features),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 53 | `    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 54 | `])` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 55 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 56 | `models = {` | 계산 결과나 설정값을 변수에 저장합니다. |
| 57 | `    "LogisticRegression": Pipeline([` | 전처리와 모델 학습 과정을 하나의 파이프라인으로 연결합니다. |
| 58 | `        ("preprocess", linear_preprocessor),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 59 | `        (` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 60 | `            "classifier",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 61 | `            LogisticRegression(` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 62 | `                max_iter=1000,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 63 | `                class_weight="balanced",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 64 | `                random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 65 | `            ),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 66 | `        ),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 67 | `    ]),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 68 | `    "DecisionTree": Pipeline([` | 전처리와 모델 학습 과정을 하나의 파이프라인으로 연결합니다. |
| 69 | `        ("preprocess", tree_preprocessor),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 70 | `        (` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 71 | `            "classifier",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 72 | `            DecisionTreeClassifier(` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 73 | `                max_depth=5,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 74 | `                class_weight="balanced",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 75 | `                random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 76 | `            ),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 77 | `        ),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 78 | `    ]),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 79 | `    "RandomForest": Pipeline([` | 전처리와 모델 학습 과정을 하나의 파이프라인으로 연결합니다. |
| 80 | `        ("preprocess", tree_preprocessor),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 81 | `        (` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 82 | `            "classifier",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 83 | `            RandomForestClassifier(` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 84 | `                n_estimators=300,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 85 | `                class_weight="balanced",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 86 | `                random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 87 | `                n_jobs=-1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 88 | `            ),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 89 | `        ),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 90 | `    ]),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 91 | `}` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 92 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 93 | `rows = []` | 계산 결과나 설정값을 변수에 저장합니다. |
| 94 | `for name, model in models.items():` | 여러 설정이나 모델을 같은 방식으로 반복 평가합니다. |
| 95 | `    model.fit(x_train, y_train)` | 학습 데이터로 전처리 기준과 분류 모델을 학습합니다. |
| 96 | `    probability = model.predict_proba(x_test)[:, 1]` | 각 행이 불량일 확률을 계산합니다. |
| 97 | `    rows.append({` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 98 | `        "model": name,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 99 | `        "roc_auc": roc_auc_score(y_test, probability),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 100 | `        "pr_auc": average_precision_score(y_test, probability),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 101 | `    })` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 102 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 103 | `result_df = pd.DataFrame(rows).sort_values("pr_auc", ascending=False)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 104 | `print(result_df.round(4))` | 실행 결과를 콘솔에 출력합니다. |
| 105 | `result_df.to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 106 | `    OUTPUT_DIR / "ex117_pr_auc_comparison.csv",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 107 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 108 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 109 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 불량 라벨은 어떤 검사 장비와 판정 절차에서 생성되었는가?
2. LOT 단위 데이터 누수가 발생하지 않도록 어떻게 분할할 것인가?
3. 불량 미탐지와 정상 오탐 중 어느 비용이 더 큰가?