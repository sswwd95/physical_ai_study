# 실습 058 — alarm_persistence

## 1. 학습 목표
순간 경보와 지속 경보를 구분해 오경보를 줄입니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
실습 057과 같은 risk_score를 계산하라.
high_risk가 최근 5개 중 3개 이상이면 persistent_alarm으로 표시하라.
지속 경보 시작 시점을 찾아 출력하고 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage03
python examples\ex058_alarm_persistence.py
```

## 4. 예상 결과
최근 5개 중 3개 이상 고위험인 지속 경보 시작점이 탐지됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 기능을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 기능을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 기능을 불러옵니다. |
| 4 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 9 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError("data/semiconductor_sensor_data.csv 파일이 없습니다.")` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 12 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 13 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | CSV 센서 데이터를 DataFrame으로 읽습니다. |
| 14 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 15 | `temp_mean = sensor_df["chamber_temp_c"].mean()` | 데이터의 평균을 계산합니다. |
| 16 | `temp_std = sensor_df["chamber_temp_c"].std(ddof=1)` | 데이터의 표준편차를 계산합니다. |
| 17 | `pressure_mean = sensor_df["chamber_pressure_pa"].mean()` | 데이터의 평균을 계산합니다. |
| 18 | `pressure_std = sensor_df["chamber_pressure_pa"].std(ddof=1)` | 데이터의 표준편차를 계산합니다. |
| 19 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 20 | `temp_alarm = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 21 | `    sensor_df["chamber_temp_c"] > temp_mean + 3 * temp_std` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 22 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 23 | `pressure_alarm = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 24 | `    sensor_df["chamber_pressure_pa"] > pressure_mean + 3 * pressure_std` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 25 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 26 | `vibration_alarm = sensor_df["vibration_g"] >= 0.15` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 27 | `particle_alarm = sensor_df["particle_count"] >= 10` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 28 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 29 | `sensor_df["risk_score"] = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 30 | `    temp_alarm.astype(int) * 40` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 31 | `    + pressure_alarm.astype(int) * 30` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 32 | `    + vibration_alarm.astype(int) * 20` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 33 | `    + particle_alarm.astype(int) * 10` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 34 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 35 | `sensor_df["high_risk"] = sensor_df["risk_score"] >= 50` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 36 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 37 | `recent_high_count = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 38 | `    sensor_df["high_risk"]` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 39 | `    .astype(int)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 40 | `    .rolling(window=5, min_periods=1)` | 지정한 구간의 이동통계를 계산합니다. |
| 41 | `    .sum()` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 42 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 43 | `sensor_df["persistent_alarm"] = recent_high_count >= 3` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 44 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 45 | `alarm_start = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 46 | `    sensor_df["persistent_alarm"]` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 47 | `    & ~sensor_df["persistent_alarm"].shift(1, fill_value=False)` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 48 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 49 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 50 | `start_df = sensor_df.loc[` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 51 | `    alarm_start,` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 52 | `    ["timestamp", "lot_id", "risk_score"],` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 53 | `]` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 54 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 55 | `print("지속 경보 시작 수:", len(start_df))` | 실행 결과를 콘솔에 출력합니다. |
| 56 | `print(start_df)` | 실행 결과를 콘솔에 출력합니다. |
| 57 | `start_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 58 | `    OUTPUT_DIR / "ex058_persistent_alarm_starts.csv",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 59 | `    index=False,` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 60 | `    encoding="utf-8-sig",` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 61 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 관리한계와 규격한계는 어떻게 다른가?
2. 공정 조건이나 레시피가 바뀌면 기준선을 다시 계산해야 하는가?
3. 경보가 발생했을 때 자동 정지와 작업자 확인 중 어떤 절차가 필요한가?