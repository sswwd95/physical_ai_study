# 실습 087 — isolation_forest_scores

## 1. 학습 목표
Isolation Forest의 연속형 이상점수를 계산하고 상위 이상을 확인합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
IsolationForest의 score_samples를 사용해 값이 클수록 이상하도록 anomaly_score=-score로 변환하라.
점수가 높은 상위 20행을 출력하고 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage05
python examples\ex087_isolation_forest_scores.py
```

## 4. 예상 결과
Isolation Forest 이상점수가 높은 상위 20개 시점이 출력됩니다.

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
| 27 | `x_scaled = StandardScaler().fit_transform(sensor_df[features])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 29 | `model = IsolationForest(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `    n_estimators=200,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `    contamination="auto",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `    random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 33 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 34 | `model.fit(x_scaled)` | 정상 패턴 또는 전체 데이터 구조를 모델이 학습합니다. |
| 35 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 36 | `sensor_df["iforest_anomaly_score"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 37 | `    -model.score_samples(x_scaled)` | 행별 이상 정도를 연속형 점수로 계산합니다. |
| 38 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 39 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 40 | `top_df = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 41 | `    sensor_df.sort_values(` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 42 | `        "iforest_anomaly_score",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 43 | `        ascending=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 44 | `    )` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 45 | `    .head(20)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 46 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 47 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 48 | `print(top_df[` | 실행 결과를 콘솔에 출력합니다. |
| 49 | `    ["timestamp", "lot_id", "iforest_anomaly_score", "true_anomaly"]` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 50 | `].round(4))` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 51 | `top_df.to_csv(` | 분석 결과를 CSV로 저장합니다. |
| 52 | `    OUTPUT_DIR / "ex087_iforest_top_scores.csv",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 53 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 54 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 55 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 이상 비율을 고정하면 실제 공정 변화에 어떤 문제가 생길 수 있는가?
2. 탐지된 이상을 삭제하기 전에 어떤 공정 정보를 확인해야 하는가?
3. 정답 라벨이 부족할 때 모델 성능을 어떻게 검증할 것인가?