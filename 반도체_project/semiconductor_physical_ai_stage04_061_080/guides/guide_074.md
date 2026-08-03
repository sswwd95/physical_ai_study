# 실습 074 — pca_distance_monitor

## 1. 학습 목표
주성분 공간에서 기준 공정과의 거리를 계산합니다.

## 2. Antigravity용 하네스 프롬프트
```text
초기 120개 온도, 압력, RF, 가스, 진동을 StandardScaler와 PCA(2)로 학습하라.
전체 데이터를 변환하고 기준 PCA 점수 평균으로부터 유클리드 거리를 계산하라.
기준 거리 99% 분위수를 넘으면 alarm으로 표시하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage04
python examples\ex074_pca_distance_monitor.py
```

## 4. 예상 결과
다변량 공정 상태가 기준 정상군에서 멀어지는 시점을 탐지합니다.

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
| 13 | `from sklearn.decomposition import PCA` | 필요한 라이브러리나 기능을 불러옵니다. |
| 14 | `from sklearn.preprocessing import StandardScaler` | 필요한 라이브러리나 기능을 불러옵니다. |
| 15 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 16 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | 센서 CSV를 DataFrame으로 읽습니다. |
| 17 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 18 | `features = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `    "chamber_temp_c",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 20 | `    "chamber_pressure_pa",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 21 | `    "rf_power_w",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 22 | `    "gas_flow_sccm",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 23 | `    "vibration_g",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 24 | `]` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 25 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 26 | `baseline_x = sensor_df[features].iloc[:120]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `all_x = sensor_df[features]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 29 | `scaler = StandardScaler()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `baseline_scaled = scaler.fit_transform(baseline_x)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `all_scaled = scaler.transform(all_x)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 33 | `pca = PCA(n_components=2, random_state=42)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 34 | `baseline_score = pca.fit_transform(baseline_scaled)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 35 | `all_score = pca.transform(all_scaled)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 36 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 37 | `center = baseline_score.mean(axis=0)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 38 | `baseline_distance = np.linalg.norm(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 39 | `    baseline_score - center,` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 40 | `    axis=1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 41 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 42 | `threshold = np.quantile(baseline_distance, 0.99)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 43 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 44 | `sensor_df["pca_distance"] = np.linalg.norm(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 45 | `    all_score - center,` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 46 | `    axis=1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 47 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 48 | `sensor_df["pca_distance_alarm"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 49 | `    sensor_df["pca_distance"] > threshold` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 50 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 51 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 52 | `print("PCA 거리 기준:", round(threshold, 4))` | 실행 결과를 콘솔에 출력합니다. |
| 53 | `print(` | 실행 결과를 콘솔에 출력합니다. |
| 54 | `    "PCA 거리 경보 수:",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 55 | `    int(sensor_df["pca_distance_alarm"].sum()),` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 56 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 기준 구간이 오염되면 경보 민감도가 어떻게 달라지는가?
2. 민감도와 오경보 사이의 균형을 어떻게 정할 것인가?
3. 변화 감지 후 장비 정지·레시피 확인·재측정 중 무엇을 먼저 할 것인가?