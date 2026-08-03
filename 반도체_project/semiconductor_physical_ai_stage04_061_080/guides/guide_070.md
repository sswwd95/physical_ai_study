# 실습 070 — variance_ratio_monitor

## 1. 학습 목표
최근 구간 분산과 기준 분산의 비율로 변동성 변화를 정량화합니다.

## 2. Antigravity용 하네스 프롬프트
```text
온도 기준분산은 초기 120개로 계산하라.
최근 40개 이동분산을 기준분산으로 나눈 variance_ratio를 만들고
비율이 2.5 이상이면 경보로 표시하여 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage04
python examples\ex070_variance_ratio_monitor.py
```

## 4. 예상 결과
최근 변동성이 기준보다 몇 배 커졌는지 시점별로 계산됩니다.

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
| 15 | `baseline_variance = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 16 | `    sensor_df["chamber_temp_c"]` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 17 | `    .iloc[:120]` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 18 | `    .var(ddof=1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 20 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 21 | `rolling_variance = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `    sensor_df["chamber_temp_c"]` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 23 | `    .rolling(window=40, min_periods=15)` | 이동 구간의 통계량을 계산합니다. |
| 24 | `    .var(ddof=1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 26 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 27 | `sensor_df["variance_ratio"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `    rolling_variance / baseline_variance` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 29 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 30 | `sensor_df["variance_ratio_alarm"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `    sensor_df["variance_ratio"] >= 2.5` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 33 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 34 | `print(` | 실행 결과를 콘솔에 출력합니다. |
| 35 | `    "분산비 경보 수:",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 36 | `    int(sensor_df["variance_ratio_alarm"].sum()),` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 37 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 38 | `sensor_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 39 | `    OUTPUT_DIR / "ex070_variance_ratio_monitor.csv",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 40 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 41 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 기준 구간이 오염되면 경보 민감도가 어떻게 달라지는가?
2. 민감도와 오경보 사이의 균형을 어떻게 정할 것인가?
3. 변화 감지 후 장비 정지·레시피 확인·재측정 중 무엇을 먼저 할 것인가?