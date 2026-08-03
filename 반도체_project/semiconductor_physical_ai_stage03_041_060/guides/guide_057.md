# 실습 057 — multi_sensor_alarm_score

## 1. 학습 목표
여러 SPC 경보를 점수화해 통합 공정 위험 점수를 만듭니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
온도 3시그마 이탈은 40점, 압력 3시그마 이탈은 30점,
진동 0.15g 이상은 20점, 입자 수 10 이상은 10점을 부여하라.
합계 50점 이상을 high_risk로 표시하고 위험 행을 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage03
python examples\ex057_multi_sensor_alarm_score.py
```

## 4. 예상 결과
다중 센서 경보를 합산한 위험점수와 고위험 행이 생성됩니다.

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
| 21 | `    (sensor_df["chamber_temp_c"] > temp_mean + 3 * temp_std)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 22 | `    \| (sensor_df["chamber_temp_c"] < temp_mean - 3 * temp_std)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 23 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 24 | `pressure_alarm = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 25 | `    (sensor_df["chamber_pressure_pa"] > pressure_mean + 3 * pressure_std)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 26 | `    \| (sensor_df["chamber_pressure_pa"] < pressure_mean - 3 * pressure_std)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 27 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 28 | `vibration_alarm = sensor_df["vibration_g"] >= 0.15` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 29 | `particle_alarm = sensor_df["particle_count"] >= 10` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 30 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 31 | `sensor_df["risk_score"] = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 32 | `    temp_alarm.astype(int) * 40` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 33 | `    + pressure_alarm.astype(int) * 30` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 34 | `    + vibration_alarm.astype(int) * 20` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 35 | `    + particle_alarm.astype(int) * 10` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 36 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 37 | `sensor_df["high_risk"] = sensor_df["risk_score"] >= 50` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 38 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 39 | `risk_df = sensor_df.loc[` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 40 | `    sensor_df["high_risk"],` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 41 | `    [` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 42 | `        "timestamp",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 43 | `        "lot_id",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 44 | `        "chamber_temp_c",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 45 | `        "chamber_pressure_pa",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 46 | `        "vibration_g",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 47 | `        "particle_count",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 48 | `        "risk_score",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 49 | `    ],` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 50 | `]` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 51 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 52 | `print("고위험 행 수:", len(risk_df))` | 실행 결과를 콘솔에 출력합니다. |
| 53 | `print(risk_df.head(20).round(3))` | 실행 결과를 콘솔에 출력합니다. |
| 54 | `risk_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 55 | `    OUTPUT_DIR / "ex057_high_risk_rows.csv",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 56 | `    index=False,` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 57 | `    encoding="utf-8-sig",` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 58 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 관리한계와 규격한계는 어떻게 다른가?
2. 공정 조건이나 레시피가 바뀌면 기준선을 다시 계산해야 하는가?
3. 경보가 발생했을 때 자동 정지와 작업자 확인 중 어떤 절차가 필요한가?