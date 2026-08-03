# 실습 062 — standardized_residuals

## 1. 학습 목표
기준 구간의 평균과 표준편차로 표준화 잔차를 계산합니다.

## 2. Antigravity용 하네스 프롬프트
```text
초기 120개 온도 데이터를 기준으로 z=(x-mean)/std를 계산하라.
절댓값 2 이상, 3 이상인 행의 개수를 각각 출력하고 결과를 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage04
python examples\ex062_standardized_residuals.py
```

## 4. 예상 결과
기준 정상 구간 대비 온도 잔차가 표준화되어 저장됩니다.

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
| 19 | `sensor_df["temp_standardized_residual"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `    sensor_df["chamber_temp_c"] - mean_value` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 21 | `) / std_value` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 22 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 23 | `count_2 = int(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `    (sensor_df["temp_standardized_residual"].abs() >= 2).sum()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 26 | `count_3 = int(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `    (sensor_df["temp_standardized_residual"].abs() >= 3).sum()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 29 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 30 | `print("절댓값 2 이상:", count_2)` | 실행 결과를 콘솔에 출력합니다. |
| 31 | `print("절댓값 3 이상:", count_3)` | 실행 결과를 콘솔에 출력합니다. |
| 32 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 33 | `sensor_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 34 | `    OUTPUT_DIR / "ex062_standardized_residuals.csv",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 35 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 36 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 37 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 기준 구간이 오염되면 경보 민감도가 어떻게 달라지는가?
2. 민감도와 오경보 사이의 균형을 어떻게 정할 것인가?
3. 변화 감지 후 장비 정지·레시피 확인·재측정 중 무엇을 먼저 할 것인가?