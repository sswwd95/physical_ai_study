# 실습 073 — multi_sensor_change_score

## 1. 학습 목표
온도·압력·진동의 표준화 변화량을 합쳐 다중 센서 변화점수를 만듭니다.

## 2. Antigravity용 하네스 프롬프트
```text
초기 120개를 기준으로 온도, 압력, 진동의 z-score를 계산하라.
각 절댓값을 합한 change_score를 만들고 8 이상이면 change_alarm으로 표시하라.
고득점 상위 20행을 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage04
python examples\ex073_multi_sensor_change_score.py
```

## 4. 예상 결과
여러 센서가 동시에 변하는 구간이 높은 변화점수로 탐지됩니다.

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
| 15 | `sensor_columns = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 16 | `    "chamber_temp_c",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 17 | `    "chamber_pressure_pa",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 18 | `    "vibration_g",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 19 | `]` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 20 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 21 | `score = np.zeros(len(sensor_df))` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 23 | `for column in sensor_columns:` | 여러 시점 또는 센서에 같은 계산을 반복합니다. |
| 24 | `    baseline = sensor_df[column].iloc[:120]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `    z = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `        sensor_df[column] - baseline.mean()` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 27 | `    ) / baseline.std(ddof=1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `    sensor_df[f"{column}_z"] = z` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `    score += z.abs()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 31 | `sensor_df["change_score"] = score` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `sensor_df["change_alarm"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 33 | `    sensor_df["change_score"] >= 8.0` | 계산 결과나 설정값을 변수에 저장합니다. |
| 34 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 35 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 36 | `top_df = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 37 | `    sensor_df.sort_values(` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 38 | `        "change_score",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 39 | `        ascending=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 40 | `    )` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 41 | `    .head(20)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 42 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 43 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 44 | `print(top_df[` | 실행 결과를 콘솔에 출력합니다. |
| 45 | `    ["timestamp", "lot_id", "change_score", "change_alarm"]` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 46 | `].round(3))` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 47 | `top_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 48 | `    OUTPUT_DIR / "ex073_multi_sensor_change_score.csv",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 49 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 50 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 51 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 기준 구간이 오염되면 경보 민감도가 어떻게 달라지는가?
2. 민감도와 오경보 사이의 균형을 어떻게 정할 것인가?
3. 변화 감지 후 장비 정지·레시피 확인·재측정 중 무엇을 먼저 할 것인가?