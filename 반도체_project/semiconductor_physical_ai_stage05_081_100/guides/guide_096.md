# 실습 096 — confusion_matrix_report

## 1. 학습 목표
이상 탐지 결과의 TP·FP·FN·TN과 주요 지표를 계산합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
IsolationForest 예측과 true_anomaly를 사용하여 confusion_matrix를 계산하라.
TN, FP, FN, TP와 precision, recall, specificity, f1을 출력하고 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage05
python examples\ex096_confusion_matrix_report.py
```

## 4. 예상 결과
정상·이상 판정의 네 가지 경우와 핵심 평가 지표가 출력됩니다.

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
| 14 | `from sklearn.metrics import confusion_matrix` | 필요한 라이브러리나 기능을 불러옵니다. |
| 15 | `from sklearn.preprocessing import StandardScaler` | 필요한 라이브러리나 기능을 불러옵니다. |
| 16 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 17 | `sensor_df = pd.read_csv(DATA_FILE)` | 센서 CSV를 DataFrame으로 읽습니다. |
| 18 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 19 | `features = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `    "chamber_temp_c",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 21 | `    "chamber_pressure_pa",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 22 | `    "rf_power_w",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 23 | `    "gas_flow_sccm",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 24 | `    "vibration_g",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 25 | `    "particle_count",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 26 | `]` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 27 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 28 | `x_scaled = StandardScaler().fit_transform(sensor_df[features])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `y_true = sensor_df["true_anomaly"].to_numpy()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 31 | `model = IsolationForest(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `    n_estimators=200,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 33 | `    contamination=0.1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 34 | `    random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 35 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 36 | `y_pred = (model.fit_predict(x_scaled) == -1).astype(int)` | 모델을 학습하고 각 행의 정상·이상 예측을 한 번에 계산합니다. |
| 37 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 38 | `tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 39 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 40 | `precision = tp / (tp + fp) if tp + fp else 0` | 계산 결과나 설정값을 변수에 저장합니다. |
| 41 | `recall = tp / (tp + fn) if tp + fn else 0` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `specificity = tn / (tn + fp) if tn + fp else 0` | 계산 결과나 설정값을 변수에 저장합니다. |
| 43 | `f1 = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 44 | `    2 * precision * recall / (precision + recall)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 45 | `    if precision + recall` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 46 | `    else 0` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 47 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 48 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 49 | `report_df = pd.DataFrame([{` | 계산 결과나 설정값을 변수에 저장합니다. |
| 50 | `    "tn": tn,` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 51 | `    "fp": fp,` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 52 | `    "fn": fn,` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 53 | `    "tp": tp,` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 54 | `    "precision": precision,` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 55 | `    "recall": recall,` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 56 | `    "specificity": specificity,` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 57 | `    "f1": f1,` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 58 | `}])` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 59 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 60 | `print(report_df.round(4))` | 실행 결과를 콘솔에 출력합니다. |
| 61 | `report_df.to_csv(` | 분석 결과를 CSV로 저장합니다. |
| 62 | `    OUTPUT_DIR / "ex096_confusion_matrix_report.csv",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 63 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 64 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 65 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 이상 비율을 고정하면 실제 공정 변화에 어떤 문제가 생길 수 있는가?
2. 탐지된 이상을 삭제하기 전에 어떤 공정 정보를 확인해야 하는가?
3. 정답 라벨이 부족할 때 모델 성능을 어떻게 검증할 것인가?