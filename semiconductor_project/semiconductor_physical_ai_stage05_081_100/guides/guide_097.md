# 실습 097 — threshold_optimization

## 1. 학습 목표
연속형 이상점수의 임계값을 바꾸며 최적 F1 기준을 찾습니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
IsolationForest anomaly_score를 계산하라.
90%부터 99% 분위수까지 1% 간격 임계값을 비교하고 precision, recall, f1을 계산하라.
F1이 가장 높은 임계값을 출력하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage05
python examples\ex097_threshold_optimization.py
```

## 4. 예상 결과
정밀도와 재현율 균형이 가장 좋은 점수 임계값 후보가 출력됩니다.

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
| 27 | `x_scaled = StandardScaler().fit_transform(sensor_df[features])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `y_true = sensor_df["true_anomaly"].to_numpy()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 30 | `model = IsolationForest(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `    n_estimators=200,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `    contamination="auto",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 33 | `    random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 34 | `).fit(x_scaled)` | 정상 패턴 또는 전체 데이터 구조를 모델이 학습합니다. |
| 35 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 36 | `score = -model.score_samples(x_scaled)` | 행별 이상 정도를 연속형 점수로 계산합니다. |
| 37 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 38 | `rows = []` | 계산 결과나 설정값을 변수에 저장합니다. |
| 39 | `for quantile in np.arange(0.90, 1.00, 0.01):` | 여러 센서나 파라미터에 같은 계산을 반복합니다. |
| 40 | `    threshold = np.quantile(score, quantile)` | 분포의 분위수를 이용해 임계값을 계산합니다. |
| 41 | `    y_pred = (score >= threshold).astype(int)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `    rows.append({` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 43 | `        "quantile": round(float(quantile), 2),` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 44 | `        "threshold": threshold,` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 45 | `        "precision": precision_score(y_true, y_pred, zero_division=0),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 46 | `        "recall": recall_score(y_true, y_pred, zero_division=0),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 47 | `        "f1": f1_score(y_true, y_pred, zero_division=0),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 48 | `    })` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 49 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 50 | `result_df = pd.DataFrame(rows)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 51 | `best_row = result_df.loc[result_df["f1"].idxmax()]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 52 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 53 | `print(result_df.round(4))` | 실행 결과를 콘솔에 출력합니다. |
| 54 | `print("\n최적 설정:")` | 실행 결과를 콘솔에 출력합니다. |
| 55 | `print(best_row.round(4))` | 실행 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 이상 비율을 고정하면 실제 공정 변화에 어떤 문제가 생길 수 있는가?
2. 탐지된 이상을 삭제하기 전에 어떤 공정 정보를 확인해야 하는가?
3. 정답 라벨이 부족할 때 모델 성능을 어떻게 검증할 것인가?