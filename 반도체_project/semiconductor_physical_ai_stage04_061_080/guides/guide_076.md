# 실습 076 — drift_segment_summary

## 1. 학습 목표
경보가 연속된 구간을 하나의 드리프트 세그먼트로 묶습니다.

## 2. Antigravity용 하네스 프롬프트
```text
온도 상방 CUSUM 경보를 계산한 뒤 연속된 True 구간마다 segment_id를 부여하라.
각 세그먼트의 시작, 종료, 길이, 평균 온도를 요약하여 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage04
python examples\ex076_drift_segment_summary.py
```

## 4. 예상 결과
연속 경보를 하나의 사건 단위로 묶은 드리프트 세그먼트 표가 생성됩니다.

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
| 16 | `z = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 17 | `    sensor_df["chamber_temp_c"] - baseline.mean()` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 18 | `) / baseline.std(ddof=1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 20 | `k = 0.5` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `h = 5.0` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `values = []` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `current = 0.0` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 25 | `for value in z:` | 여러 시점 또는 센서에 같은 계산을 반복합니다. |
| 26 | `    current = max(0.0, current + value - k)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `    values.append(current)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 28 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 29 | `sensor_df["cusum_alarm"] = np.array(values) >= h` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 31 | `start_flag = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `    sensor_df["cusum_alarm"]` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 33 | `    & ~sensor_df["cusum_alarm"].shift(1, fill_value=False)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 34 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 35 | `sensor_df["segment_id"] = start_flag.cumsum()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 36 | `sensor_df.loc[` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 37 | `    ~sensor_df["cusum_alarm"],` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 38 | `    "segment_id",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 39 | `] = 0` | 계산 결과나 설정값을 변수에 저장합니다. |
| 40 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 41 | `segment_df = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `    sensor_df.loc[sensor_df["segment_id"] > 0]` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 43 | `    .groupby("segment_id")` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 44 | `    .agg(` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 45 | `        start_time=("timestamp", "min"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 46 | `        end_time=("timestamp", "max"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 47 | `        length=("timestamp", "size"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 48 | `        mean_temperature=("chamber_temp_c", "mean"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 49 | `    )` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 50 | `    .reset_index()` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 51 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 52 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 53 | `print(segment_df.round(3))` | 실행 결과를 콘솔에 출력합니다. |
| 54 | `segment_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 55 | `    OUTPUT_DIR / "ex076_drift_segments.csv",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 56 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 57 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 58 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 기준 구간이 오염되면 경보 민감도가 어떻게 달라지는가?
2. 민감도와 오경보 사이의 균형을 어떻게 정할 것인가?
3. 변화 감지 후 장비 정지·레시피 확인·재측정 중 무엇을 먼저 할 것인가?