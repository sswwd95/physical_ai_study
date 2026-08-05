# 실습 089 — local_outlier_factor

## 1. 학습 목표
LOF로 주변 이웃과 밀도가 다른 국소 이상을 탐지합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
StandardScaler 후 LocalOutlierFactor를 적용하라.
n_neighbors=25, contamination=0.1을 사용하고 negative_outlier_factor_를 양의 점수로 변환하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage05
python examples\ex089_local_outlier_factor.py
```

## 4. 예상 결과
주변 이웃과 밀도가 다른 국소 이상 후보가 탐지됩니다.

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
| 13 | `from sklearn.neighbors import LocalOutlierFactor` | 필요한 라이브러리나 기능을 불러옵니다. |
| 14 | `from sklearn.preprocessing import StandardScaler` | 필요한 라이브러리나 기능을 불러옵니다. |
| 15 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 16 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | 센서 CSV를 DataFrame으로 읽습니다. |
| 17 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 18 | `features = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `    "chamber_temp_c",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 20 | `    "chamber_pressure_pa",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 21 | `    "rf_power_w",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 22 | `    "gas_flow_sccm",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 23 | `    "vibration_g",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 24 | `    "particle_count",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 25 | `]` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 26 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 27 | `x_scaled = StandardScaler().fit_transform(sensor_df[features])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 29 | `model = LocalOutlierFactor(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `    n_neighbors=25,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `    contamination=0.1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 33 | `prediction = model.fit_predict(x_scaled)` | 모델을 학습하고 각 행의 정상·이상 예측을 한 번에 계산합니다. |
| 34 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 35 | `sensor_df["lof_anomaly"] = (prediction == -1).astype(int)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 36 | `sensor_df["lof_anomaly_score"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 37 | `    -model.negative_outlier_factor_` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 38 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 39 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 40 | `print("LOF 이상 수:", int(sensor_df["lof_anomaly"].sum()))` | 실행 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 이상 비율을 고정하면 실제 공정 변화에 어떤 문제가 생길 수 있는가?
2. 탐지된 이상을 삭제하기 전에 어떤 공정 정보를 확인해야 하는가?
3. 정답 라벨이 부족할 때 모델 성능을 어떻게 검증할 것인가?