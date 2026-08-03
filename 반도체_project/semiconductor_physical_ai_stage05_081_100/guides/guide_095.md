# 실습 095 — model_metric_comparison

## 1. 학습 목표
여러 비지도 모델의 예측 결과를 동일한 평가 지표로 비교합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
IsolationForest, LOF, OneClassSVM 세 모델을 같은 표준화 데이터에 적용하라.
각 모델의 precision, recall, f1, predicted_count를 한 표로 비교하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage05
python examples\ex095_model_metric_comparison.py
```

## 4. 예상 결과
세 비지도 이상 탐지 모델의 성능이 같은 기준으로 비교됩니다.

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
| 19 | `sensor_df = pd.read_csv(DATA_FILE)` | 센서 CSV를 DataFrame으로 읽습니다. |
| 20 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 21 | `features = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `    "chamber_temp_c",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 23 | `    "chamber_pressure_pa",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 24 | `    "rf_power_w",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 25 | `    "gas_flow_sccm",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 26 | `    "vibration_g",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 27 | `    "particle_count",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 28 | `]` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 29 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 30 | `x_scaled = StandardScaler().fit_transform(sensor_df[features])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `y_true = sensor_df["true_anomaly"].to_numpy()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 33 | `predictions = {` | 계산 결과나 설정값을 변수에 저장합니다. |
| 34 | `    "IsolationForest": (` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 35 | `        IsolationForest(` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 36 | `            n_estimators=200,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 37 | `            contamination=0.1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 38 | `            random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 39 | `        ).fit_predict(x_scaled) == -1` | 모델을 학습하고 각 행의 정상·이상 예측을 한 번에 계산합니다. |
| 40 | `    ).astype(int),` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 41 | `    "LOF": (` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 42 | `        LocalOutlierFactor(` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 43 | `            n_neighbors=25,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 44 | `            contamination=0.1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 45 | `        ).fit_predict(x_scaled) == -1` | 모델을 학습하고 각 행의 정상·이상 예측을 한 번에 계산합니다. |
| 46 | `    ).astype(int),` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 47 | `    "OneClassSVM": (` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 48 | `        OneClassSVM(` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 49 | `            kernel="rbf",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 50 | `            gamma="scale",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 51 | `            nu=0.1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 52 | `        ).fit_predict(x_scaled) == -1` | 모델을 학습하고 각 행의 정상·이상 예측을 한 번에 계산합니다. |
| 53 | `    ).astype(int),` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 54 | `}` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 55 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 56 | `rows = []` | 계산 결과나 설정값을 변수에 저장합니다. |
| 57 | `for name, y_pred in predictions.items():` | 여러 센서나 파라미터에 같은 계산을 반복합니다. |
| 58 | `    rows.append({` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 59 | `        "model": name,` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 60 | `        "predicted_count": int(y_pred.sum()),` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 61 | `        "precision": precision_score(y_true, y_pred, zero_division=0),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 62 | `        "recall": recall_score(y_true, y_pred, zero_division=0),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 63 | `        "f1": f1_score(y_true, y_pred, zero_division=0),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 64 | `    })` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 65 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 66 | `result_df = pd.DataFrame(rows).sort_values("f1", ascending=False)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 67 | `print(result_df.round(4))` | 실행 결과를 콘솔에 출력합니다. |
| 68 | `result_df.to_csv(` | 분석 결과를 CSV로 저장합니다. |
| 69 | `    OUTPUT_DIR / "ex095_model_metric_comparison.csv",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 70 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 71 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 72 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 이상 비율을 고정하면 실제 공정 변화에 어떤 문제가 생길 수 있는가?
2. 탐지된 이상을 삭제하기 전에 어떤 공정 정보를 확인해야 하는가?
3. 정답 라벨이 부족할 때 모델 성능을 어떻게 검증할 것인가?