# 실습 086 — isolation_forest_basic

## 1. 학습 목표
Isolation Forest로 다변량 비지도 이상 탐지를 수행합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
StandardScaler로 6개 센서를 표준화하고 IsolationForest를 적용하라.
n_estimators=200, contamination=0.1, random_state=42를 사용하고
예측 -1을 anomaly로 변환하여 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage05
python examples\ex086_isolation_forest_basic.py
```

## 4. 예상 결과
전체 데이터의 약 10%가 Isolation Forest 이상 후보로 표시됩니다.

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
| 27 | `scaler = StandardScaler()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `x_scaled = scaler.fit_transform(sensor_df[features])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 30 | `model = IsolationForest(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `    n_estimators=200,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `    contamination=0.1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 33 | `    random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 34 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 35 | `prediction = model.fit_predict(x_scaled)` | 모델을 학습하고 각 행의 정상·이상 예측을 한 번에 계산합니다. |
| 36 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 37 | `sensor_df["iforest_anomaly"] = (prediction == -1).astype(int)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 38 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 39 | `print(` | 실행 결과를 콘솔에 출력합니다. |
| 40 | `    "Isolation Forest 이상 수:",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 41 | `    int(sensor_df["iforest_anomaly"].sum()),` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 42 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 43 | `sensor_df.to_csv(` | 분석 결과를 CSV로 저장합니다. |
| 44 | `    OUTPUT_DIR / "ex086_isolation_forest.csv",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 45 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 46 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 47 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 이상 비율을 고정하면 실제 공정 변화에 어떤 문제가 생길 수 있는가?
2. 탐지된 이상을 삭제하기 전에 어떤 공정 정보를 확인해야 하는가?
3. 정답 라벨이 부족할 때 모델 성능을 어떻게 검증할 것인가?