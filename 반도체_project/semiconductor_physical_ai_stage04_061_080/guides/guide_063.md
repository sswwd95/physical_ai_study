# 실습 063 — upper_cusum_temperature

## 1. 학습 목표
상방 CUSUM으로 작은 온도 평균 상승을 누적 감지합니다.

## 2. Antigravity용 하네스 프롬프트
```text
초기 120개 온도를 기준으로 상방 CUSUM을 계산하라.
표준화 데이터에 대해 k=0.5, h=5를 사용하고 S+=max(0, 이전S+z-k)로 계산하라.
h를 넘는 행에 alarm 플래그를 만들고 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage04
python examples\ex063_upper_cusum_temperature.py
```

## 4. 예상 결과
작은 평균 상승이 누적되면서 상방 CUSUM 경보가 발생합니다.

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
| 16 | `mean_value = baseline.mean()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 17 | `std_value = baseline.std(ddof=1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 18 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 19 | `z = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `    sensor_df["chamber_temp_c"] - mean_value` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 21 | `) / std_value` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 22 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 23 | `k = 0.5` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `h = 5.0` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `cusum_values = []` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `current = 0.0` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 28 | `for value in z:` | 여러 시점 또는 센서에 같은 계산을 반복합니다. |
| 29 | `    current = max(0.0, current + value - k)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `    cusum_values.append(current)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 31 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 32 | `sensor_df["cusum_upper"] = cusum_values` | 계산 결과나 설정값을 변수에 저장합니다. |
| 33 | `sensor_df["cusum_upper_alarm"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 34 | `    sensor_df["cusum_upper"] >= h` | 계산 결과나 설정값을 변수에 저장합니다. |
| 35 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 36 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 37 | `print(` | 실행 결과를 콘솔에 출력합니다. |
| 38 | `    "상방 CUSUM 최초 경보 시점:",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 39 | `    sensor_df.loc[` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 40 | `        sensor_df["cusum_upper_alarm"],` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 41 | `        "timestamp",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 42 | `    ].min(),` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 43 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 44 | `sensor_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 45 | `    OUTPUT_DIR / "ex063_upper_cusum_temperature.csv",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 46 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 47 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 48 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 기준 구간이 오염되면 경보 민감도가 어떻게 달라지는가?
2. 민감도와 오경보 사이의 균형을 어떻게 정할 것인가?
3. 변화 감지 후 장비 정지·레시피 확인·재측정 중 무엇을 먼저 할 것인가?