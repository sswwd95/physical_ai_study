# 실습 099 — anomaly_dashboard_data

## 1. 학습 목표
원본 센서와 모델별 이상점수를 하나의 대시보드 CSV로 통합합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
IsolationForest 점수, LOF 점수, OneClassSVM 점수, 모델별 이상 플래그,
앙상블 투표 수, true_anomaly를 포함하는 대시보드 CSV를 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage05
python examples\ex099_anomaly_dashboard_data.py
```

## 4. 예상 결과
모델 점수와 예측을 비교할 수 있는 통합 대시보드 CSV가 생성됩니다.

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
| 14 | `from sklearn.neighbors import LocalOutlierFactor` | 필요한 라이브러리나 기능을 불러옵니다. |
| 15 | `from sklearn.preprocessing import StandardScaler` | 필요한 라이브러리나 기능을 불러옵니다. |
| 16 | `from sklearn.svm import OneClassSVM` | 필요한 라이브러리나 기능을 불러옵니다. |
| 17 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 18 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | 센서 CSV를 DataFrame으로 읽습니다. |
| 19 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 20 | `features = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `    "chamber_temp_c",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 22 | `    "chamber_pressure_pa",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 23 | `    "rf_power_w",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 24 | `    "gas_flow_sccm",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 25 | `    "vibration_g",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 26 | `    "particle_count",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 27 | `]` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 28 | `x_scaled = StandardScaler().fit_transform(sensor_df[features])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 30 | `iforest_model = IsolationForest(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `    n_estimators=200,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `    contamination=0.1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 33 | `    random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 34 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 35 | `iforest_pred = iforest_model.fit_predict(x_scaled)` | 모델을 학습하고 각 행의 정상·이상 예측을 한 번에 계산합니다. |
| 36 | `sensor_df["iforest_score"] = -iforest_model.score_samples(x_scaled)` | 행별 이상 정도를 연속형 점수로 계산합니다. |
| 37 | `sensor_df["iforest_anomaly"] = (iforest_pred == -1).astype(int)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 38 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 39 | `lof_model = LocalOutlierFactor(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 40 | `    n_neighbors=25,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 41 | `    contamination=0.1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 43 | `lof_pred = lof_model.fit_predict(x_scaled)` | 모델을 학습하고 각 행의 정상·이상 예측을 한 번에 계산합니다. |
| 44 | `sensor_df["lof_score"] = -lof_model.negative_outlier_factor_` | 계산 결과나 설정값을 변수에 저장합니다. |
| 45 | `sensor_df["lof_anomaly"] = (lof_pred == -1).astype(int)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 46 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 47 | `ocsvm_model = OneClassSVM(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 48 | `    kernel="rbf",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 49 | `    gamma="scale",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 50 | `    nu=0.1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 51 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 52 | `ocsvm_pred = ocsvm_model.fit_predict(x_scaled)` | 모델을 학습하고 각 행의 정상·이상 예측을 한 번에 계산합니다. |
| 53 | `sensor_df["ocsvm_score"] = -ocsvm_model.decision_function(x_scaled)` | 행별 이상 정도를 연속형 점수로 계산합니다. |
| 54 | `sensor_df["ocsvm_anomaly"] = (ocsvm_pred == -1).astype(int)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 55 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 56 | `sensor_df["ensemble_vote_count"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 57 | `    sensor_df["iforest_anomaly"]` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 58 | `    + sensor_df["lof_anomaly"]` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 59 | `    + sensor_df["ocsvm_anomaly"]` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 60 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 61 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 62 | `dashboard_columns = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 63 | `    "timestamp",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 64 | `    "lot_id",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 65 | `    *features,` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 66 | `    "iforest_score",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 67 | `    "lof_score",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 68 | `    "ocsvm_score",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 69 | `    "iforest_anomaly",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 70 | `    "lof_anomaly",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 71 | `    "ocsvm_anomaly",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 72 | `    "ensemble_vote_count",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 73 | `    "true_anomaly",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 74 | `]` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 75 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 76 | `sensor_df[dashboard_columns].to_csv(` | 분석 결과를 CSV로 저장합니다. |
| 77 | `    OUTPUT_DIR / "ex099_anomaly_dashboard_data.csv",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 78 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 79 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 80 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 81 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 82 | `print(sensor_df[dashboard_columns].tail(10).round(4))` | 실행 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 이상 비율을 고정하면 실제 공정 변화에 어떤 문제가 생길 수 있는가?
2. 탐지된 이상을 삭제하기 전에 어떤 공정 정보를 확인해야 하는가?
3. 정답 라벨이 부족할 때 모델 성능을 어떻게 검증할 것인가?