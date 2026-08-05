# 실습 120 — automated_classification_report

## 1. 학습 목표
모델별 성능, 혼동행렬, 예측 결과, 특징 중요도를 Excel 보고서로 자동 생성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
LogisticRegression, DecisionTree, RandomForest를 학습하라.
model_metrics, confusion_matrices, predictions, feature_importance 네 시트의 Excel 보고서를 만들고
모델별 accuracy, precision, recall, f1, roc_auc, pr_auc를 CSV로도 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage06
python examples\ex120_automated_classification_report.py
```

## 4. 예상 결과
세 분류 모델의 성능·혼동행렬·예측·특징 중요도가 Excel 보고서로 저장됩니다.

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
| 18 | `from sklearn.metrics import (` | 필요한 라이브러리나 모델을 불러옵니다. |
| 19 | `    accuracy_score,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 20 | `    average_precision_score,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 21 | `    confusion_matrix,` | 정상·불량 예측의 네 가지 경우를 표로 계산합니다. |
| 22 | `    f1_score,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 23 | `    precision_score,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 24 | `    recall_score,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 25 | `    roc_auc_score,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 26 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 27 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리나 모델을 불러옵니다. |
| 28 | `from sklearn.pipeline import Pipeline` | 필요한 라이브러리나 모델을 불러옵니다. |
| 29 | `from sklearn.preprocessing import OneHotEncoder, StandardScaler` | 필요한 라이브러리나 모델을 불러옵니다. |
| 30 | `from sklearn.tree import DecisionTreeClassifier` | 필요한 라이브러리나 모델을 불러옵니다. |
| 31 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 32 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | 불량 분류용 CSV를 DataFrame으로 읽습니다. |
| 33 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 34 | `feature_columns = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 35 | `    "recipe",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 36 | `    "chamber_id",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 37 | `    "chamber_temp_c",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 38 | `    "chamber_pressure_pa",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 39 | `    "rf_power_w",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 40 | `    "gas_flow_sccm",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 41 | `    "vibration_g",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 42 | `    "particle_count",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 43 | `    "etch_rate_nm_min",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 44 | `    "uniformity_percent",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 45 | `]` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 46 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 47 | `x = sensor_df[feature_columns]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 48 | `y = sensor_df["defect"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 49 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 50 | `train_index, test_index = train_test_split(` | 학습용 데이터와 평가용 데이터를 분리합니다. |
| 51 | `    np.arange(len(sensor_df)),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 52 | `    test_size=0.25,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 53 | `    random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 54 | `    stratify=y,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 55 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 56 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 57 | `x_train = x.iloc[train_index]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 58 | `x_test = x.iloc[test_index]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 59 | `y_train = y.iloc[train_index]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 60 | `y_test = y.iloc[test_index]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 61 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 62 | `numeric_features = feature_columns[2:]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 63 | `categorical_features = feature_columns[:2]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 64 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 65 | `linear_preprocessor = ColumnTransformer([` | 숫자형과 범주형 컬럼의 전처리를 하나로 묶습니다. |
| 66 | `    ("num", StandardScaler(), numeric_features),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 67 | `    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 68 | `])` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 69 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 70 | `tree_preprocessor = ColumnTransformer([` | 숫자형과 범주형 컬럼의 전처리를 하나로 묶습니다. |
| 71 | `    ("num", "passthrough", numeric_features),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 72 | `    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 73 | `])` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 74 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 75 | `models = {` | 계산 결과나 설정값을 변수에 저장합니다. |
| 76 | `    "LogisticRegression": Pipeline([` | 전처리와 모델 학습 과정을 하나의 파이프라인으로 연결합니다. |
| 77 | `        ("preprocess", linear_preprocessor),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 78 | `        (` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 79 | `            "classifier",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 80 | `            LogisticRegression(` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 81 | `                max_iter=1000,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 82 | `                class_weight="balanced",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 83 | `                random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 84 | `            ),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 85 | `        ),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 86 | `    ]),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 87 | `    "DecisionTree": Pipeline([` | 전처리와 모델 학습 과정을 하나의 파이프라인으로 연결합니다. |
| 88 | `        ("preprocess", tree_preprocessor),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 89 | `        (` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 90 | `            "classifier",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 91 | `            DecisionTreeClassifier(` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 92 | `                max_depth=5,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 93 | `                min_samples_leaf=10,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 94 | `                class_weight="balanced",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 95 | `                random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 96 | `            ),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 97 | `        ),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 98 | `    ]),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 99 | `    "RandomForest": Pipeline([` | 전처리와 모델 학습 과정을 하나의 파이프라인으로 연결합니다. |
| 100 | `        ("preprocess", tree_preprocessor),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 101 | `        (` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 102 | `            "classifier",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 103 | `            RandomForestClassifier(` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 104 | `                n_estimators=300,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 105 | `                max_depth=8,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 106 | `                min_samples_leaf=5,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 107 | `                class_weight="balanced",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 108 | `                random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 109 | `                n_jobs=-1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 110 | `            ),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 111 | `        ),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 112 | `    ]),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 113 | `}` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 114 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 115 | `metric_rows = []` | 계산 결과나 설정값을 변수에 저장합니다. |
| 116 | `confusion_rows = []` | 계산 결과나 설정값을 변수에 저장합니다. |
| 117 | `prediction_df = sensor_df.iloc[test_index][` | 계산 결과나 설정값을 변수에 저장합니다. |
| 118 | `    ["timestamp", "lot_id", "recipe", "chamber_id", "defect"]` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 119 | `].copy()` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 120 | `prediction_df = prediction_df.rename(columns={"defect": "actual_defect"})` | 계산 결과나 설정값을 변수에 저장합니다. |
| 121 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 122 | `for model_name, model in models.items():` | 여러 설정이나 모델을 같은 방식으로 반복 평가합니다. |
| 123 | `    model.fit(x_train, y_train)` | 학습 데이터로 전처리 기준과 분류 모델을 학습합니다. |
| 124 | `    probability = model.predict_proba(x_test)[:, 1]` | 각 행이 불량일 확률을 계산합니다. |
| 125 | `    prediction = (probability >= 0.5).astype(int)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 126 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 127 | `    metric_rows.append({` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 128 | `        "model": model_name,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 129 | `        "accuracy": accuracy_score(y_test, prediction),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 130 | `        "precision": precision_score(y_test, prediction, zero_division=0),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 131 | `        "recall": recall_score(y_test, prediction, zero_division=0),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 132 | `        "f1": f1_score(y_test, prediction, zero_division=0),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 133 | `        "roc_auc": roc_auc_score(y_test, probability),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 134 | `        "pr_auc": average_precision_score(y_test, probability),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 135 | `    })` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 136 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 137 | `    tn, fp, fn, tp = confusion_matrix(y_test, prediction).ravel()` | 정상·불량 예측의 네 가지 경우를 표로 계산합니다. |
| 138 | `    confusion_rows.append({` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 139 | `        "model": model_name,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 140 | `        "tn": tn,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 141 | `        "fp": fp,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 142 | `        "fn": fn,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 143 | `        "tp": tp,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 144 | `    })` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 145 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 146 | `    prediction_df[f"{model_name}_probability"] = probability` | 계산 결과나 설정값을 변수에 저장합니다. |
| 147 | `    prediction_df[f"{model_name}_prediction"] = prediction` | 계산 결과나 설정값을 변수에 저장합니다. |
| 148 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 149 | `metrics_df = pd.DataFrame(metric_rows).sort_values("f1", ascending=False)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 150 | `confusion_df = pd.DataFrame(confusion_rows)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 151 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 152 | `rf_model = models["RandomForest"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 153 | `rf_feature_names = rf_model.named_steps["preprocess"].get_feature_names_out()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 154 | `rf_importance = rf_model.named_steps["classifier"].feature_importances_` | 계산 결과나 설정값을 변수에 저장합니다. |
| 155 | `importance_df = pd.DataFrame({` | 계산 결과나 설정값을 변수에 저장합니다. |
| 156 | `    "feature": rf_feature_names,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 157 | `    "importance": rf_importance,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 158 | `}).sort_values("importance", ascending=False)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 159 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 160 | `excel_file = OUTPUT_DIR / "ex120_classification_report.xlsx"` | 정밀도·재현율·F1을 클래스별로 요약합니다. |
| 161 | `with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:` | 계산 결과나 설정값을 변수에 저장합니다. |
| 162 | `    metrics_df.to_excel(writer, sheet_name="model_metrics", index=False)` | 결과를 Excel 보고서로 저장합니다. |
| 163 | `    confusion_df.to_excel(writer, sheet_name="confusion_matrices", index=False)` | 결과를 Excel 보고서로 저장합니다. |
| 164 | `    prediction_df.to_excel(writer, sheet_name="predictions", index=False)` | 결과를 Excel 보고서로 저장합니다. |
| 165 | `    importance_df.to_excel(writer, sheet_name="feature_importance", index=False)` | 결과를 Excel 보고서로 저장합니다. |
| 166 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 167 | `metrics_df.to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 168 | `    OUTPUT_DIR / "ex120_model_metrics.csv",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 169 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 170 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 171 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 172 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 173 | `print(metrics_df.round(4))` | 실행 결과를 콘솔에 출력합니다. |
| 174 | `print("보고서 저장:", excel_file)` | 실행 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 불량 라벨은 어떤 검사 장비와 판정 절차에서 생성되었는가?
2. LOT 단위 데이터 누수가 발생하지 않도록 어떻게 분할할 것인가?
3. 불량 미탐지와 정상 오탐 중 어느 비용이 더 큰가?