# 실습 077 — alarm_cooldown

## 1. 학습 목표
경보 후 일정 시간 동안 재경보를 억제하는 쿨다운 로직을 구현합니다.

## 2. Antigravity용 하네스 프롬프트
```text
change_score가 8 이상인 시점을 원시 경보로 정의하라.
한 번 경보가 발생하면 다음 20개 시점 동안 새 경보를 억제하는 cooldown_alarm을 구현하라.
원시 경보 수와 최종 경보 수를 비교하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage04
python examples\ex077_alarm_cooldown.py
```

## 4. 예상 결과
중복 알림이 줄어들고 사건 중심의 경보만 남습니다.

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
| 15 | `score = np.zeros(len(sensor_df))` | 계산 결과나 설정값을 변수에 저장합니다. |
| 16 | `for column in [` | 여러 시점 또는 센서에 같은 계산을 반복합니다. |
| 17 | `    "chamber_temp_c",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 18 | `    "chamber_pressure_pa",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 19 | `    "vibration_g",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 20 | `]:` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 21 | `    baseline = sensor_df[column].iloc[:120]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `    z = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `        sensor_df[column] - baseline.mean()` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 24 | `    ) / baseline.std(ddof=1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `    score += z.abs()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 27 | `raw_alarm = score >= 8.0` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 29 | `cooldown = 20` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `cooldown_alarm = np.zeros(len(sensor_df), dtype=bool)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `next_allowed_index = 0` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 33 | `for index, alarm in enumerate(raw_alarm):` | 여러 시점 또는 센서에 같은 계산을 반복합니다. |
| 34 | `    if alarm and index >= next_allowed_index:` | 계산 결과나 설정값을 변수에 저장합니다. |
| 35 | `        cooldown_alarm[index] = True` | 계산 결과나 설정값을 변수에 저장합니다. |
| 36 | `        next_allowed_index = index + cooldown` | 계산 결과나 설정값을 변수에 저장합니다. |
| 37 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 38 | `sensor_df["raw_alarm"] = raw_alarm` | 계산 결과나 설정값을 변수에 저장합니다. |
| 39 | `sensor_df["cooldown_alarm"] = cooldown_alarm` | 계산 결과나 설정값을 변수에 저장합니다. |
| 40 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 41 | `print("원시 경보 수:", int(raw_alarm.sum()))` | 실행 결과를 콘솔에 출력합니다. |
| 42 | `print("쿨다운 적용 경보 수:", int(cooldown_alarm.sum()))` | 실행 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 기준 구간이 오염되면 경보 민감도가 어떻게 달라지는가?
2. 민감도와 오경보 사이의 균형을 어떻게 정할 것인가?
3. 변화 감지 후 장비 정지·레시피 확인·재측정 중 무엇을 먼저 할 것인가?