# 실습 072 — window_mean_difference

## 1. 학습 목표
좌우 고정 창의 평균 차이로 국소 변화점을 탐지합니다.

## 2. Antigravity용 하네스 프롬프트
```text
각 시점 기준 앞 20개와 뒤 20개의 온도 평균 차이를 계산하라.
절댓값이 1.0°C 이상이면 local_change_alarm으로 표시하고 결과를 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage04
python examples\ex072_window_mean_difference.py
```

## 4. 예상 결과
급격한 평균 이동이 있는 시점 주변에 변화 경보가 생성됩니다.

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
| 15 | `values = sensor_df["chamber_temp_c"].to_numpy()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 16 | `window = 20` | 계산 결과나 설정값을 변수에 저장합니다. |
| 17 | `difference = np.full(len(values), np.nan)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 18 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 19 | `for index in range(window, len(values) - window):` | 여러 시점 또는 센서에 같은 계산을 반복합니다. |
| 20 | `    left_mean = values[index - window:index].mean()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `    right_mean = values[index:index + window].mean()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `    difference[index] = right_mean - left_mean` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 24 | `sensor_df["local_mean_difference"] = difference` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `sensor_df["local_change_alarm"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `    sensor_df["local_mean_difference"].abs() >= 1.0` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 28 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 29 | `print(` | 실행 결과를 콘솔에 출력합니다. |
| 30 | `    "국소 변화 경보 수:",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 31 | `    int(sensor_df["local_change_alarm"].sum()),` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 32 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 33 | `sensor_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 34 | `    OUTPUT_DIR / "ex072_local_change_detection.csv",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 35 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 36 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 37 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 기준 구간이 오염되면 경보 민감도가 어떻게 달라지는가?
2. 민감도와 오경보 사이의 균형을 어떻게 정할 것인가?
3. 변화 감지 후 장비 정지·레시피 확인·재측정 중 무엇을 먼저 할 것인가?