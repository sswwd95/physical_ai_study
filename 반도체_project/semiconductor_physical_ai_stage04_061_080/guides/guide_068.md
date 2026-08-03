# 실습 068 — ewma_lambda_comparison

## 1. 학습 목표
lambda 값에 따른 EWMA 반응 속도를 비교합니다.

## 2. Antigravity용 하네스 프롬프트
```text
온도 데이터에 lambda 0.05, 0.2, 0.5의 EWMA를 각각 계산하라.
세 컬럼을 한 CSV에 저장하고 마지막 20행을 출력하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage04
python examples\ex068_ewma_lambda_comparison.py
```

## 4. 예상 결과
lambda가 클수록 최근 변화에 빠르게 반응하는 모습을 비교할 수 있습니다.

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
| 15 | `for lambda_value in [0.05, 0.2, 0.5]:` | 여러 시점 또는 센서에 같은 계산을 반복합니다. |
| 16 | `    column = f"temp_ewma_{str(lambda_value).replace('.', '_')}"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 17 | `    sensor_df[column] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 18 | `        sensor_df["chamber_temp_c"]` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 19 | `        .ewm(alpha=lambda_value, adjust=False)` | 최근 관측값에 더 큰 가중치를 주는 EWMA를 계산합니다. |
| 20 | `        .mean()` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 21 | `    )` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 22 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 23 | `result_columns = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `    "timestamp",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 25 | `    "chamber_temp_c",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 26 | `    "temp_ewma_0_05",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 27 | `    "temp_ewma_0_2",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 28 | `    "temp_ewma_0_5",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 29 | `]` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 30 | `result_df = sensor_df[result_columns]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 32 | `print(result_df.tail(20).round(4))` | 실행 결과를 콘솔에 출력합니다. |
| 33 | `result_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 34 | `    OUTPUT_DIR / "ex068_ewma_lambda_comparison.csv",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 35 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 36 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 37 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 기준 구간이 오염되면 경보 민감도가 어떻게 달라지는가?
2. 민감도와 오경보 사이의 균형을 어떻게 정할 것인가?
3. 변화 감지 후 장비 정지·레시피 확인·재측정 중 무엇을 먼저 할 것인가?