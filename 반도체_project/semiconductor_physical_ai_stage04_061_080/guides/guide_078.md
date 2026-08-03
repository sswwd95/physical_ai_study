# 실습 078 — alarm_severity_levels

## 1. 학습 목표
변화점수에 따라 주의·경고·위험 등급을 부여합니다.

## 2. Antigravity용 하네스 프롬프트
```text
온도, 압력, 진동의 절대 z-score 합으로 change_score를 계산하라.
0~4 normal, 4~8 caution, 8~12 warning, 12 이상 critical로 분류하고 등급별 건수를 출력하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage04
python examples\ex078_alarm_severity_levels.py
```

## 4. 예상 결과
공정 변화 정도가 네 단계 등급으로 분류됩니다.

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
| 13 | `sensor_df = pd.read_csv(DATA_FILE)` | 센서 CSV를 DataFrame으로 읽습니다. |
| 14 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 15 | `score = np.zeros(len(sensor_df))` | 계산 결과나 설정값을 변수에 저장합니다. |
| 16 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 17 | `for column in [` | 여러 시점 또는 센서에 같은 계산을 반복합니다. |
| 18 | `    "chamber_temp_c",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 19 | `    "chamber_pressure_pa",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 20 | `    "vibration_g",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 21 | `]:` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 22 | `    baseline = sensor_df[column].iloc[:120]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `    z = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `        sensor_df[column] - baseline.mean()` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 25 | `    ) / baseline.std(ddof=1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `    score += z.abs()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 28 | `sensor_df["change_score"] = score` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `sensor_df["severity"] = pd.cut(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `    sensor_df["change_score"],` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 31 | `    bins=[-np.inf, 4, 8, 12, np.inf],` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `    labels=["normal", "caution", "warning", "critical"],` | 계산 결과나 설정값을 변수에 저장합니다. |
| 33 | `    right=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 34 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 35 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 36 | `print(sensor_df["severity"].value_counts().sort_index())` | 실행 결과를 콘솔에 출력합니다. |
| 37 | `sensor_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 38 | `    OUTPUT_DIR / "ex078_alarm_severity.csv",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 39 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 40 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 41 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 기준 구간이 오염되면 경보 민감도가 어떻게 달라지는가?
2. 민감도와 오경보 사이의 균형을 어떻게 정할 것인가?
3. 변화 감지 후 장비 정지·레시피 확인·재측정 중 무엇을 먼저 할 것인가?