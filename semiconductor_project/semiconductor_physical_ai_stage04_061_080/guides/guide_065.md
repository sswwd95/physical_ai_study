# 실습 065 — two_sided_cusum

## 1. 학습 목표
상방·하방 CUSUM을 동시에 계산해 양방향 평균 변화를 감지합니다.

## 2. Antigravity용 하네스 프롬프트
```text
온도에 대해 상방과 하방 CUSUM을 함께 계산하는 함수를 작성하라.
k=0.5, h=5를 사용하고 어느 한쪽이라도 임계값을 넘으면 two_sided_alarm으로 표시하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage04
python examples\ex065_two_sided_cusum.py
```

## 4. 예상 결과
상승과 하락 모두를 감시하는 CUSUM 결과가 생성됩니다.

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
| 13 | `def calculate_two_sided_cusum(values, mean_value, std_value, k=0.5, h=5.0):` | 반복 사용할 계산 절차를 함수로 정의합니다. |
| 14 | `    upper_values = []` | 계산 결과나 설정값을 변수에 저장합니다. |
| 15 | `    lower_values = []` | 계산 결과나 설정값을 변수에 저장합니다. |
| 16 | `    upper = 0.0` | 계산 결과나 설정값을 변수에 저장합니다. |
| 17 | `    lower = 0.0` | 계산 결과나 설정값을 변수에 저장합니다. |
| 18 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 19 | `    for raw_value in values:` | 여러 시점 또는 센서에 같은 계산을 반복합니다. |
| 20 | `        z = (raw_value - mean_value) / std_value` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `        upper = max(0.0, upper + z - k)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `        lower = min(0.0, lower + z + k)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `        upper_values.append(upper)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 24 | `        lower_values.append(lower)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 25 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 26 | `    alarm = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `        (np.array(upper_values) >= h)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `        \| (np.abs(np.array(lower_values)) >= h)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `    )` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 30 | `    return upper_values, lower_values, alarm` | 함수의 결과를 호출한 곳으로 돌려줍니다. |
| 31 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 32 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | 센서 CSV를 DataFrame으로 읽습니다. |
| 33 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 34 | `baseline = sensor_df["chamber_temp_c"].iloc[:120]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 35 | `upper, lower, alarm = calculate_two_sided_cusum(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 36 | `    sensor_df["chamber_temp_c"].to_numpy(),` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 37 | `    baseline.mean(),` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 38 | `    baseline.std(ddof=1),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 39 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 40 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 41 | `sensor_df["cusum_upper"] = upper` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `sensor_df["cusum_lower"] = lower` | 계산 결과나 설정값을 변수에 저장합니다. |
| 43 | `sensor_df["two_sided_alarm"] = alarm` | 계산 결과나 설정값을 변수에 저장합니다. |
| 44 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 45 | `print("양방향 CUSUM 경보 수:", int(alarm.sum()))` | 실행 결과를 콘솔에 출력합니다. |
| 46 | `sensor_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 47 | `    OUTPUT_DIR / "ex065_two_sided_cusum.csv",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 48 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 49 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 50 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 기준 구간이 오염되면 경보 민감도가 어떻게 달라지는가?
2. 민감도와 오경보 사이의 균형을 어떻게 정할 것인가?
3. 변화 감지 후 장비 정지·레시피 확인·재측정 중 무엇을 먼저 할 것인가?