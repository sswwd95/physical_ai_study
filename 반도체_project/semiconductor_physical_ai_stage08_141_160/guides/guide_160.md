# 실습 160 — automated_yield_report

## 1. 학습 목표
모델 비교, 잔차, 예측, 특징 중요도를 Excel 보고서로 자동 생성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
LinearRegression, Ridge, RandomForestRegressor, GradientBoostingRegressor를 비교하라.
model_metrics, predictions, residual_summary, feature_importance 시트의 Excel 보고서를 만들고
모델별 MAE, RMSE, R²를 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage08
python examples\ex160_automated_yield_report.py
```

## 4. 예상 결과
수율 회귀 모델 비교와 잔차·예측·특징 중요도 보고서가 생성됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "semiconductor_yield_regression.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError(` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 12 | `        "data/semiconductor_yield_regression.csv 파일이 없습니다."` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 13 | `    )` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 14 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 15 | `from sklearn.compose import ColumnTransformer` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 16 | `from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 17 | `from sklearn.linear_model import LinearRegression, Ridge` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 18 | `from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 19 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 20 | `from sklearn.pipeline import Pipeline` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 21 | `from sklearn.preprocessing import OneHotEncoder, StandardScaler` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 22 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 23 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | 수율 예측용 CSV를 DataFrame으로 읽습니다. |
| 24 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 25 | `feature_columns = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `    "recipe",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 27 | `    "chamber_id",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 28 | `    "temp_mean_c",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 29 | `    "temp_std_c",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 30 | `    "pressure_mean_pa",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 31 | `    "pressure_std_pa",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 32 | `    "rf_power_mean_w",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 33 | `    "gas_flow_mean_sccm",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 34 | `    "vibration_rms_g",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 35 | `    "particle_mean",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 36 | `    "downtime_min",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 37 | `    "maintenance_age_hours",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 38 | `]` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 39 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 40 | `x = sensor_df[feature_columns]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 41 | `y = sensor_df["yield_percent"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 43 | `train_index, test_index = train_test_split(` | 학습용 데이터와 평가용 데이터를 분리합니다. |
| 44 | `    np.arange(len(sensor_df)),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 45 | `    test_size=0.25,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 46 | `    random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 47 | `)` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 48 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 49 | `x_train = x.iloc[train_index]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 50 | `x_test = x.iloc[test_index]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 51 | `y_train = y.iloc[train_index]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 52 | `y_test = y.iloc[test_index]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 53 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 54 | `numeric_features = feature_columns[2:]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 55 | `categorical_features = feature_columns[:2]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 56 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 57 | `linear_pre = ColumnTransformer([` | 숫자형과 범주형 컬럼의 전처리를 하나로 묶습니다. |
| 58 | `    ("num", StandardScaler(), numeric_features),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 59 | `    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 60 | `])` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 61 | `tree_pre = ColumnTransformer([` | 숫자형과 범주형 컬럼의 전처리를 하나로 묶습니다. |
| 62 | `    ("num", "passthrough", numeric_features),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 63 | `    ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_features),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 64 | `])` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 65 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 66 | `models = {` | 계산 결과나 설정값을 변수에 저장합니다. |
| 67 | `    "LinearRegression": Pipeline([` | 전처리와 회귀 모델을 하나의 파이프라인으로 연결합니다. |
| 68 | `        ("preprocess", linear_pre),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 69 | `        ("regressor", LinearRegression()),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 70 | `    ]),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 71 | `    "Ridge": Pipeline([` | 전처리와 회귀 모델을 하나의 파이프라인으로 연결합니다. |
| 72 | `        ("preprocess", linear_pre),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 73 | `        ("regressor", Ridge(alpha=1.0)),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 74 | `    ]),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 75 | `    "RandomForest": Pipeline([` | 전처리와 회귀 모델을 하나의 파이프라인으로 연결합니다. |
| 76 | `        ("preprocess", tree_pre),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 77 | `        (` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 78 | `            "regressor",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 79 | `            RandomForestRegressor(` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 80 | `                n_estimators=400,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 81 | `                max_depth=10,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 82 | `                min_samples_leaf=4,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 83 | `                random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 84 | `                n_jobs=-1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 85 | `            ),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 86 | `        ),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 87 | `    ]),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 88 | `    "GradientBoosting": Pipeline([` | 전처리와 회귀 모델을 하나의 파이프라인으로 연결합니다. |
| 89 | `        ("preprocess", tree_pre),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 90 | `        (` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 91 | `            "regressor",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 92 | `            GradientBoostingRegressor(` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 93 | `                n_estimators=250,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 94 | `                learning_rate=0.05,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 95 | `                max_depth=3,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 96 | `                random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 97 | `            ),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 98 | `        ),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 99 | `    ]),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 100 | `}` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 101 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 102 | `metric_rows = []` | 계산 결과나 설정값을 변수에 저장합니다. |
| 103 | `prediction_df = sensor_df.iloc[test_index][` | 계산 결과나 설정값을 변수에 저장합니다. |
| 104 | `    ["timestamp", "lot_id", "recipe", "chamber_id", "yield_percent"]` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 105 | `].copy()` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 106 | `prediction_df = prediction_df.rename(columns={"yield_percent": "actual_yield"})` | 계산 결과나 설정값을 변수에 저장합니다. |
| 107 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 108 | `best_model_name = None` | 계산 결과나 설정값을 변수에 저장합니다. |
| 109 | `best_mae = np.inf` | 계산 결과나 설정값을 변수에 저장합니다. |
| 110 | `best_model = None` | 계산 결과나 설정값을 변수에 저장합니다. |
| 111 | `best_prediction = None` | 계산 결과나 설정값을 변수에 저장합니다. |
| 112 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 113 | `for model_name, model in models.items():` | 여러 모델이나 파라미터를 같은 방식으로 반복 평가합니다. |
| 114 | `    model.fit(x_train, y_train)` | 학습 데이터로 전처리기와 회귀 모델을 학습합니다. |
| 115 | `    prediction = model.predict(x_test)` | 학습된 모델로 수율을 예측합니다. |
| 116 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 117 | `    mae = mean_absolute_error(y_test, prediction)` | 평균 절대 오차를 계산합니다. |
| 118 | `    metric_rows.append({` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 119 | `        "model": model_name,` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 120 | `        "mae": mae,` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 121 | `        "rmse": mean_squared_error(y_test, prediction) ** 0.5,` | 제곱 오차를 이용한 RMSE 계산에 사용합니다. |
| 122 | `        "r2": r2_score(y_test, prediction),` | 모델이 수율 변동을 얼마나 설명하는지 R²를 계산합니다. |
| 123 | `    })` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 124 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 125 | `    prediction_df[f"{model_name}_prediction"] = prediction` | 계산 결과나 설정값을 변수에 저장합니다. |
| 126 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 127 | `    if mae < best_mae:` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 128 | `        best_mae = mae` | 계산 결과나 설정값을 변수에 저장합니다. |
| 129 | `        best_model_name = model_name` | 계산 결과나 설정값을 변수에 저장합니다. |
| 130 | `        best_model = model` | 계산 결과나 설정값을 변수에 저장합니다. |
| 131 | `        best_prediction = prediction` | 계산 결과나 설정값을 변수에 저장합니다. |
| 132 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 133 | `metrics_df = pd.DataFrame(metric_rows).sort_values("mae")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 134 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 135 | `prediction_df["best_model"] = best_model_name` | 계산 결과나 설정값을 변수에 저장합니다. |
| 136 | `prediction_df["best_prediction"] = best_prediction` | 계산 결과나 설정값을 변수에 저장합니다. |
| 137 | `prediction_df["residual"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 138 | `    prediction_df["actual_yield"]` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 139 | `    - prediction_df["best_prediction"]` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 140 | `)` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 141 | `prediction_df["absolute_error"] = prediction_df["residual"].abs()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 142 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 143 | `residual_summary_df = pd.DataFrame([{` | 계산 결과나 설정값을 변수에 저장합니다. |
| 144 | `    "best_model": best_model_name,` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 145 | `    "residual_mean": prediction_df["residual"].mean(),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 146 | `    "residual_std": prediction_df["residual"].std(),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 147 | `    "mae": prediction_df["absolute_error"].mean(),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 148 | `    "low_yield_actual_count": int(` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 149 | `        (prediction_df["actual_yield"] < 92.0).sum()` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 150 | `    ),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 151 | `    "low_yield_predicted_count": int(` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 152 | `        (prediction_df["best_prediction"] < 92.0).sum()` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 153 | `    ),` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 154 | `}])` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 155 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 156 | `if best_model_name == "RandomForest":` | 계산 결과나 설정값을 변수에 저장합니다. |
| 157 | `    feature_names = best_model.named_steps["preprocess"].get_feature_names_out()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 158 | `    importance = best_model.named_steps["regressor"].feature_importances_` | 계산 결과나 설정값을 변수에 저장합니다. |
| 159 | `    importance_df = pd.DataFrame({` | 계산 결과나 설정값을 변수에 저장합니다. |
| 160 | `        "feature": feature_names,` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 161 | `        "importance": importance,` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 162 | `    }).sort_values("importance", ascending=False)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 163 | `else:` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 164 | `    importance_df = pd.DataFrame({` | 계산 결과나 설정값을 변수에 저장합니다. |
| 165 | `        "feature": [],` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 166 | `        "importance": [],` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 167 | `    })` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 168 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 169 | `excel_file = OUTPUT_DIR / "ex160_yield_regression_report.xlsx"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 170 | `with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:` | 계산 결과나 설정값을 변수에 저장합니다. |
| 171 | `    metrics_df.to_excel(writer, sheet_name="model_metrics", index=False)` | 결과를 Excel 보고서로 저장합니다. |
| 172 | `    prediction_df.to_excel(writer, sheet_name="predictions", index=False)` | 결과를 Excel 보고서로 저장합니다. |
| 173 | `    residual_summary_df.to_excel(writer, sheet_name="residual_summary", index=False)` | 결과를 Excel 보고서로 저장합니다. |
| 174 | `    importance_df.to_excel(writer, sheet_name="feature_importance", index=False)` | 결과를 Excel 보고서로 저장합니다. |
| 175 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 176 | `metrics_df.to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 177 | `    OUTPUT_DIR / "ex160_model_metrics.csv",` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 178 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 179 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 180 | `)` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 181 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 182 | `print(metrics_df.round(4))` | 실행 결과를 콘솔에 출력합니다. |
| 183 | `print("최고 모델:", best_model_name)` | 실행 결과를 콘솔에 출력합니다. |
| 184 | `print("보고서 저장:", excel_file)` | 실행 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 수율 라벨이 어떤 검사 시점과 기준으로 계산되었는가?
2. LOT·레시피·챔버 정보가 누수 없이 분할되었는가?
3. 평균 오차뿐 아니라 저수율 구간의 오차를 별도로 확인해야 하는가?