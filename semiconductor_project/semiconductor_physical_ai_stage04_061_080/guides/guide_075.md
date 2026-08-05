# 실습 075 — mahalanobis_distance_monitor

## 1. 학습 목표
센서 공분산을 반영한 Mahalanobis 거리로 다변량 이상을 감지합니다.

## 2. Antigravity용 하네스 프롬프트
```text
초기 120개의 온도, 압력, RF, 가스, 진동으로 평균과 공분산을 계산하라.
전체 행의 Mahalanobis 거리 제곱을 계산하고 기준 구간 99% 분위수를 넘으면 경보로 표시하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage04
python examples\ex075_mahalanobis_distance_monitor.py
```

## 4. 예상 결과
센서 간 상관관계를 반영한 다변량 거리 경보가 계산됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 기능을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 기능을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 기능을 불러옵니다. |
| 4 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "semiconductor_sensor_data_stage04.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError("data/semiconductor_sensor_data_stage04.csv 파일이 없습니다.")` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 12 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 13 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | 센서 CSV를 DataFrame으로 읽습니다. |
| 14 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 15 | `features = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 16 | `    "chamber_temp_c",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 17 | `    "chamber_pressure_pa",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 18 | `    "rf_power_w",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 19 | `    "gas_flow_sccm",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 20 | `    "vibration_g",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 21 | `]` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 22 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 23 | `baseline_x = sensor_df[features].iloc[:120].to_numpy()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `all_x = sensor_df[features].to_numpy()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 26 | `mean_vector = baseline_x.mean(axis=0)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `covariance = np.cov(baseline_x, rowvar=False)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `inverse_covariance = np.linalg.pinv(covariance)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 30 | `def mahalanobis_squared(row):` | 반복 사용할 계산 절차를 함수로 정의합니다. |
| 31 | `    difference = row - mean_vector` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `    return float(` | 함수의 결과를 호출한 곳으로 돌려줍니다. |
| 33 | `        difference.T` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 34 | `        @ inverse_covariance` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 35 | `        @ difference` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 36 | `    )` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 37 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 38 | `baseline_distance = np.array([` | 계산 결과나 설정값을 변수에 저장합니다. |
| 39 | `    mahalanobis_squared(row)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 40 | `    for row in baseline_x` | 여러 시점 또는 센서에 같은 계산을 반복합니다. |
| 41 | `])` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 42 | `all_distance = np.array([` | 계산 결과나 설정값을 변수에 저장합니다. |
| 43 | `    mahalanobis_squared(row)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 44 | `    for row in all_x` | 여러 시점 또는 센서에 같은 계산을 반복합니다. |
| 45 | `])` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 46 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 47 | `threshold = np.quantile(baseline_distance, 0.99)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 48 | `sensor_df["mahalanobis_d2"] = all_distance` | 계산 결과나 설정값을 변수에 저장합니다. |
| 49 | `sensor_df["mahalanobis_alarm"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 50 | `    sensor_df["mahalanobis_d2"] > threshold` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 51 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 52 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 53 | `print("Mahalanobis D² 기준:", round(threshold, 4))` | 실행 결과를 콘솔에 출력합니다. |
| 54 | `print(` | 실행 결과를 콘솔에 출력합니다. |
| 55 | `    "경보 수:",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 56 | `    int(sensor_df["mahalanobis_alarm"].sum()),` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 57 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 기준 구간이 오염되면 경보 민감도가 어떻게 달라지는가?
2. 민감도와 오경보 사이의 균형을 어떻게 정할 것인가?
3. 변화 감지 후 장비 정지·레시피 확인·재측정 중 무엇을 먼저 할 것인가?