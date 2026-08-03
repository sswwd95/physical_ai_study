# 실습 140 — automated_multiclass_report

## 1. 학습 목표
모델 비교, 클래스별 지표, 혼동행렬, 예측, 오분류를 Excel 보고서로 자동 생성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
LogisticRegression, RandomForest, HistGradientBoosting을 학습하라.
model_metrics, class_metrics, confusion_matrix, predictions, misclassified_rows,
feature_importance 시트의 Excel 보고서를 생성하고 모델 비교 CSV도 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage07
python examples\ex140_automated_multiclass_report.py
```

## 4. 예상 결과
다중 클래스 모델 비교와 오류 분석이 포함된 Excel 보고서가 생성됩니다.

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
| 16 | `from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier` | 필요한 라이브러리나 모델을 불러옵니다. |
| 17 | `from sklearn.linear_model import LogisticRegression` | 필요한 라이브러리나 모델을 불러옵니다. |
| 18 | `from sklearn.metrics import (` | 필요한 라이브러리나 모델을 불러옵니다. |
| 19 | `    accuracy_score,` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 20 | `    classification_report,` | 클래스별 정밀도·재현율·F1을 요약합니다. |
| 21 | `    confusion_matrix,` | 실제 클래스와 예측 클래스의 조합을 표로 계산합니다. |
| 22 | `    f1_score,` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 23 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 24 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리나 모델을 불러옵니다. |
| 25 | `from sklearn.pipeline import Pipeline` | 필요한 라이브러리나 모델을 불러옵니다. |
| 26 | `from sklearn.preprocessing import OneHotEncoder, StandardScaler` | 필요한 라이브러리나 모델을 불러옵니다. |
| 27 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 28 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | 다중 불량 유형 CSV를 DataFrame으로 읽습니다. |
| 29 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 30 | `feature_columns = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `    "recipe",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 32 | `    "chamber_id",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 33 | `    "chamber_temp_c",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 34 | `    "chamber_pressure_pa",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 35 | `    "rf_power_w",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 36 | `    "gas_flow_sccm",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 37 | `    "vibration_g",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 38 | `    "particle_count",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 39 | `    "etch_rate_nm_min",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 40 | `    "uniformity_percent",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 41 | `]` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 42 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 43 | `x = sensor_df[feature_columns]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 44 | `y = sensor_df["defect_type"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 45 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 46 | `train_index, test_index = train_test_split(` | 학습용과 평가용 데이터를 분리합니다. |
| 47 | `    np.arange(len(sensor_df)),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 48 | `    test_size=0.25,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 49 | `    random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 50 | `    stratify=y,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 51 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 52 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 53 | `x_train = x.iloc[train_index]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 54 | `x_test = x.iloc[test_index]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 55 | `y_train = y.iloc[train_index]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 56 | `y_test = y.iloc[test_index]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 57 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 58 | `numeric_features = feature_columns[2:]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 59 | `categorical_features = feature_columns[:2]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 60 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 61 | `linear_pre = ColumnTransformer([` | 계산 결과나 설정값을 변수에 저장합니다. |
| 62 | `    ("num", StandardScaler(), numeric_features),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 63 | `    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 64 | `])` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 65 | `tree_pre = ColumnTransformer([` | 계산 결과나 설정값을 변수에 저장합니다. |
| 66 | `    ("num", "passthrough", numeric_features),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 67 | `    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 68 | `])` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 69 | `dense_pre = ColumnTransformer([` | 계산 결과나 설정값을 변수에 저장합니다. |
| 70 | `    ("num", "passthrough", numeric_features),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 71 | `    ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_features),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 72 | `])` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 73 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 74 | `models = {` | 계산 결과나 설정값을 변수에 저장합니다. |
| 75 | `    "LogisticRegression": Pipeline([` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 76 | `        ("preprocess", linear_pre),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 77 | `        (` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 78 | `            "classifier",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 79 | `            LogisticRegression(` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 80 | `                max_iter=2000,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 81 | `                class_weight="balanced",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 82 | `                random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 83 | `            ),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 84 | `        ),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 85 | `    ]),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 86 | `    "RandomForest": Pipeline([` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 87 | `        ("preprocess", tree_pre),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 88 | `        (` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 89 | `            "classifier",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 90 | `            RandomForestClassifier(` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 91 | `                n_estimators=400,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 92 | `                max_depth=10,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 93 | `                min_samples_leaf=4,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 94 | `                class_weight="balanced",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 95 | `                random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 96 | `                n_jobs=-1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 97 | `            ),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 98 | `        ),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 99 | `    ]),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 100 | `    "HistGradientBoosting": Pipeline([` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 101 | `        ("preprocess", dense_pre),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 102 | `        (` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 103 | `            "classifier",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 104 | `            HistGradientBoostingClassifier(` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 105 | `                max_iter=200,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 106 | `                learning_rate=0.08,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 107 | `                max_depth=6,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 108 | `                random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 109 | `            ),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 110 | `        ),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 111 | `    ]),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 112 | `}` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 113 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 114 | `metric_rows = []` | 계산 결과나 설정값을 변수에 저장합니다. |
| 115 | `prediction_df = sensor_df.iloc[test_index][` | 계산 결과나 설정값을 변수에 저장합니다. |
| 116 | `    ["timestamp", "lot_id", "recipe", "chamber_id", "defect_type"]` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 117 | `].copy()` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 118 | `prediction_df = prediction_df.rename(columns={"defect_type": "actual_class"})` | 계산 결과나 설정값을 변수에 저장합니다. |
| 119 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 120 | `best_model_name = None` | 계산 결과나 설정값을 변수에 저장합니다. |
| 121 | `best_macro_f1 = -1` | 계산 결과나 설정값을 변수에 저장합니다. |
| 122 | `best_model = None` | 계산 결과나 설정값을 변수에 저장합니다. |
| 123 | `best_prediction = None` | 계산 결과나 설정값을 변수에 저장합니다. |
| 124 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 125 | `for model_name, model in models.items():` | 여러 클래스·모델·설정에 같은 작업을 반복합니다. |
| 126 | `    model.fit(x_train, y_train)` | 학습 데이터로 전처리기와 모델을 학습합니다. |
| 127 | `    prediction = model.predict(x_test)` | 학습된 모델로 불량 유형을 예측합니다. |
| 128 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 129 | `    macro_f1 = f1_score(y_test, prediction, average="macro")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 130 | `    metric_rows.append({` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 131 | `        "model": model_name,` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 132 | `        "accuracy": accuracy_score(y_test, prediction),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 133 | `        "macro_f1": macro_f1,` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 134 | `        "weighted_f1": f1_score(y_test, prediction, average="weighted"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 135 | `    })` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 136 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 137 | `    prediction_df[f"{model_name}_prediction"] = prediction` | 계산 결과나 설정값을 변수에 저장합니다. |
| 138 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 139 | `    if macro_f1 > best_macro_f1:` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 140 | `        best_macro_f1 = macro_f1` | 계산 결과나 설정값을 변수에 저장합니다. |
| 141 | `        best_model_name = model_name` | 계산 결과나 설정값을 변수에 저장합니다. |
| 142 | `        best_model = model` | 계산 결과나 설정값을 변수에 저장합니다. |
| 143 | `        best_prediction = prediction` | 계산 결과나 설정값을 변수에 저장합니다. |
| 144 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 145 | `metrics_df = pd.DataFrame(metric_rows).sort_values("macro_f1", ascending=False)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 146 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 147 | `class_report = classification_report(` | 클래스별 정밀도·재현율·F1을 요약합니다. |
| 148 | `    y_test,` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 149 | `    best_prediction,` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 150 | `    output_dict=True,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 151 | `    zero_division=0,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 152 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 153 | `class_metrics_df = pd.DataFrame(class_report).T` | 계산 결과나 설정값을 변수에 저장합니다. |
| 154 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 155 | `labels = best_model.classes_` | 계산 결과나 설정값을 변수에 저장합니다. |
| 156 | `matrix_df = pd.DataFrame(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 157 | `    confusion_matrix(y_test, best_prediction, labels=labels),` | 실제 클래스와 예측 클래스의 조합을 표로 계산합니다. |
| 158 | `    index=[f"actual_{label}" for label in labels],` | 계산 결과나 설정값을 변수에 저장합니다. |
| 159 | `    columns=[f"predicted_{label}" for label in labels],` | 계산 결과나 설정값을 변수에 저장합니다. |
| 160 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 161 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 162 | `prediction_df["best_model"] = best_model_name` | 계산 결과나 설정값을 변수에 저장합니다. |
| 163 | `prediction_df["best_prediction"] = best_prediction` | 계산 결과나 설정값을 변수에 저장합니다. |
| 164 | `misclassified_df = prediction_df.loc[` | 계산 결과나 설정값을 변수에 저장합니다. |
| 165 | `    prediction_df["actual_class"] != prediction_df["best_prediction"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 166 | `].copy()` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 167 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 168 | `if best_model_name == "RandomForest":` | 계산 결과나 설정값을 변수에 저장합니다. |
| 169 | `    feature_names = best_model.named_steps["preprocess"].get_feature_names_out()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 170 | `    importance = best_model.named_steps["classifier"].feature_importances_` | 계산 결과나 설정값을 변수에 저장합니다. |
| 171 | `    importance_df = pd.DataFrame({` | 계산 결과나 설정값을 변수에 저장합니다. |
| 172 | `        "feature": feature_names,` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 173 | `        "importance": importance,` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 174 | `    }).sort_values("importance", ascending=False)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 175 | `else:` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 176 | `    importance_df = pd.DataFrame({` | 계산 결과나 설정값을 변수에 저장합니다. |
| 177 | `        "feature": [],` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 178 | `        "importance": [],` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 179 | `    })` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 180 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 181 | `excel_file = OUTPUT_DIR / "ex140_multiclass_report.xlsx"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 182 | `with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:` | 계산 결과나 설정값을 변수에 저장합니다. |
| 183 | `    metrics_df.to_excel(writer, sheet_name="model_metrics", index=False)` | 결과를 Excel 보고서로 저장합니다. |
| 184 | `    class_metrics_df.to_excel(writer, sheet_name="class_metrics")` | 결과를 Excel 보고서로 저장합니다. |
| 185 | `    matrix_df.to_excel(writer, sheet_name="confusion_matrix")` | 실제 클래스와 예측 클래스의 조합을 표로 계산합니다. |
| 186 | `    prediction_df.to_excel(writer, sheet_name="predictions", index=False)` | 결과를 Excel 보고서로 저장합니다. |
| 187 | `    misclassified_df.to_excel(writer, sheet_name="misclassified_rows", index=False)` | 결과를 Excel 보고서로 저장합니다. |
| 188 | `    importance_df.to_excel(writer, sheet_name="feature_importance", index=False)` | 결과를 Excel 보고서로 저장합니다. |
| 189 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 190 | `metrics_df.to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 191 | `    OUTPUT_DIR / "ex140_model_metrics.csv",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 192 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 193 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 194 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 195 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 196 | `print(metrics_df.round(4))` | 실행 결과를 콘솔에 출력합니다. |
| 197 | `print("최고 모델:", best_model_name)` | 실행 결과를 콘솔에 출력합니다. |
| 198 | `print("보고서 저장:", excel_file)` | 실행 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 가장 희소한 불량 유형의 재현율이 낮으면 어떤 위험이 있는가?
2. macro F1과 weighted F1 중 어떤 지표가 더 적합한가?
3. 클래스 확률이 낮을 때 보류 또는 재검사 정책을 어떻게 설계할 것인가?