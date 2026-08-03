# 실습 067 — ewma_control_limits

## 1. 학습 목표
EWMA 중심선과 시간에 따라 변하는 관리한계를 계산합니다.

## 2. Antigravity용 하네스 프롬프트
```text
초기 120개 온도를 기준으로 lambda=0.2, L=3인 EWMA를 계산하라.
시간 t에 따른 표준편차 공식 sigma*sqrt(lambda/(2-lambda)*(1-(1-lambda)^(2t)))을 사용하여
EWMA UCL/LCL을 만들고 경보를 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage04
python examples\ex067_ewma_control_limits.py
```

## 4. 예상 결과
시간에 따라 안정화되는 EWMA 관리한계와 경보가 생성됩니다.

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
| 15 | `baseline = sensor_df["chamber_temp_c"].iloc[:120]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 16 | `mu0 = baseline.mean()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 17 | `sigma = baseline.std(ddof=1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 18 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 19 | `lambda_value = 0.2` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `l_value = 3.0` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 22 | `sensor_df["temp_ewma"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `    sensor_df["chamber_temp_c"]` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 24 | `    .ewm(alpha=lambda_value, adjust=False)` | 최근 관측값에 더 큰 가중치를 주는 EWMA를 계산합니다. |
| 25 | `    .mean()` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 26 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 27 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 28 | `t = np.arange(1, len(sensor_df) + 1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `ewma_std = sigma * np.sqrt(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `    lambda_value / (2 - lambda_value)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 31 | `    * (1 - (1 - lambda_value) ** (2 * t))` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 32 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 33 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 34 | `sensor_df["ewma_ucl"] = mu0 + l_value * ewma_std` | 계산 결과나 설정값을 변수에 저장합니다. |
| 35 | `sensor_df["ewma_lcl"] = mu0 - l_value * ewma_std` | 계산 결과나 설정값을 변수에 저장합니다. |
| 36 | `sensor_df["ewma_alarm"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 37 | `    (sensor_df["temp_ewma"] > sensor_df["ewma_ucl"])` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 38 | `    \| (sensor_df["temp_ewma"] < sensor_df["ewma_lcl"])` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 39 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 40 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 41 | `print("EWMA 경보 수:", int(sensor_df["ewma_alarm"].sum()))` | 실행 결과를 콘솔에 출력합니다. |
| 42 | `sensor_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 43 | `    OUTPUT_DIR / "ex067_ewma_control_limits.csv",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 44 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 45 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 46 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 기준 구간이 오염되면 경보 민감도가 어떻게 달라지는가?
2. 민감도와 오경보 사이의 균형을 어떻게 정할 것인가?
3. 변화 감지 후 장비 정지·레시피 확인·재측정 중 무엇을 먼저 할 것인가?