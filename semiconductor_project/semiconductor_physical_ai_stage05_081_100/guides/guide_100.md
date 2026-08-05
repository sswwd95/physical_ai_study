# 실습 100 — automated_anomaly_report

## 1. 학습 목표
모델 성능, 이상 행, LOT별 이상률을 Excel 보고서로 자동 생성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
IsolationForest, LOF, OneClassSVM과 2표 이상 앙상블을 계산하라.
model_metrics, anomaly_rows, lot_summary 세 시트의 Excel 보고서와 CSV 요약을 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage05
python examples\ex100_automated_anomaly_report.py
```

## 4. 예상 결과
모델별 성능, 앙상블 이상 행, LOT별 이상률이 Excel 보고서로 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 기능을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 기능을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 기능을 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "semiconductor_anomaly_data.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError("data/semiconductor_anomaly_data.csv 파일이 없습니다.")` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 12 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 13 | `from sklearn.ensemble import IsolationForest` | 필요한 라이브러리나 기능을 불러옵니다. |
| 14 | `from sklearn.metrics import precision_score, recall_score, f1_score` | 필요한 라이브러리나 기능을 불러옵니다. |
| 15 | `from sklearn.neighbors import LocalOutlierFactor` | 필요한 라이브러리나 기능을 불러옵니다. |
| 16 | `from sklearn.preprocessing import StandardScaler` | 필요한 라이브러리나 기능을 불러옵니다. |
| 17 | `from sklearn.svm import OneClassSVM` | 필요한 라이브러리나 기능을 불러옵니다. |
| 18 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 19 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | 센서 CSV를 DataFrame으로 읽습니다. |
| 20 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 21 | `features = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `    "chamber_temp_c",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 23 | `    "chamber_pressure_pa",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 24 | `    "rf_power_w",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 25 | `    "gas_flow_sccm",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 26 | `    "vibration_g",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 27 | `    "particle_count",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 28 | `]` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 29 | `x_scaled = StandardScaler().fit_transform(sensor_df[features])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `y_true = sensor_df["true_anomaly"].to_numpy()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 32 | `predictions = {}` | 계산 결과나 설정값을 변수에 저장합니다. |
| 33 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 34 | `iforest_model = IsolationForest(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 35 | `    n_estimators=200,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 36 | `    contamination=0.1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 37 | `    random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 38 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 39 | `predictions["IsolationForest"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 40 | `    iforest_model.fit_predict(x_scaled) == -1` | 모델을 학습하고 각 행의 정상·이상 예측을 한 번에 계산합니다. |
| 41 | `).astype(int)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 42 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 43 | `lof_model = LocalOutlierFactor(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 44 | `    n_neighbors=25,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 45 | `    contamination=0.1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 46 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 47 | `predictions["LOF"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 48 | `    lof_model.fit_predict(x_scaled) == -1` | 모델을 학습하고 각 행의 정상·이상 예측을 한 번에 계산합니다. |
| 49 | `).astype(int)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 50 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 51 | `ocsvm_model = OneClassSVM(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 52 | `    kernel="rbf",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 53 | `    gamma="scale",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 54 | `    nu=0.1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 55 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 56 | `predictions["OneClassSVM"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 57 | `    ocsvm_model.fit_predict(x_scaled) == -1` | 모델을 학습하고 각 행의 정상·이상 예측을 한 번에 계산합니다. |
| 58 | `).astype(int)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 59 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 60 | `vote_count = sum(predictions.values())` | 계산 결과나 설정값을 변수에 저장합니다. |
| 61 | `predictions["Ensemble"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 62 | `    vote_count >= 2` | 계산 결과나 설정값을 변수에 저장합니다. |
| 63 | `).astype(int)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 64 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 65 | `metric_rows = []` | 계산 결과나 설정값을 변수에 저장합니다. |
| 66 | `for model_name, y_pred in predictions.items():` | 여러 센서나 파라미터에 같은 계산을 반복합니다. |
| 67 | `    metric_rows.append({` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 68 | `        "model": model_name,` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 69 | `        "predicted_count": int(y_pred.sum()),` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 70 | `        "precision": precision_score(y_true, y_pred, zero_division=0),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 71 | `        "recall": recall_score(y_true, y_pred, zero_division=0),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 72 | `        "f1": f1_score(y_true, y_pred, zero_division=0),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 73 | `    })` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 74 | `    sensor_df[f"{model_name}_anomaly"] = y_pred` | 계산 결과나 설정값을 변수에 저장합니다. |
| 75 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 76 | `metrics_df = pd.DataFrame(metric_rows).sort_values(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 77 | `    "f1",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 78 | `    ascending=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 79 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 80 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 81 | `sensor_df["ensemble_vote_count"] = vote_count` | 계산 결과나 설정값을 변수에 저장합니다. |
| 82 | `anomaly_df = sensor_df.loc[` | 계산 결과나 설정값을 변수에 저장합니다. |
| 83 | `    sensor_df["Ensemble_anomaly"] == 1` | 계산 결과나 설정값을 변수에 저장합니다. |
| 84 | `].copy()` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 85 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 86 | `lot_summary = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 87 | `    sensor_df.groupby("lot_id")` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 88 | `    .agg(` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 89 | `        row_count=("timestamp", "size"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 90 | `        true_anomaly_count=("true_anomaly", "sum"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 91 | `        ensemble_anomaly_count=("Ensemble_anomaly", "sum"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 92 | `    )` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 93 | `    .reset_index()` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 94 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 95 | `lot_summary["ensemble_anomaly_rate"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 96 | `    lot_summary["ensemble_anomaly_count"]` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 97 | `    / lot_summary["row_count"]` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 98 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 99 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 100 | `excel_file = OUTPUT_DIR / "ex100_automated_anomaly_report.xlsx"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 101 | `with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:` | 계산 결과나 설정값을 변수에 저장합니다. |
| 102 | `    metrics_df.to_excel(writer, sheet_name="model_metrics", index=False)` | 분석 결과를 Excel 파일로 저장합니다. |
| 103 | `    anomaly_df.to_excel(writer, sheet_name="anomaly_rows", index=False)` | 분석 결과를 Excel 파일로 저장합니다. |
| 104 | `    lot_summary.to_excel(writer, sheet_name="lot_summary", index=False)` | 분석 결과를 Excel 파일로 저장합니다. |
| 105 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 106 | `metrics_df.to_csv(` | 분석 결과를 CSV로 저장합니다. |
| 107 | `    OUTPUT_DIR / "ex100_model_metrics.csv",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 108 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 109 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 110 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 111 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 112 | `print(metrics_df.round(4))` | 실행 결과를 콘솔에 출력합니다. |
| 113 | `print("보고서 저장:", excel_file)` | 실행 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 이상 비율을 고정하면 실제 공정 변화에 어떤 문제가 생길 수 있는가?
2. 탐지된 이상을 삭제하기 전에 어떤 공정 정보를 확인해야 하는가?
3. 정답 라벨이 부족할 때 모델 성능을 어떻게 검증할 것인가?