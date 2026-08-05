# 실습 052 — zone_rule_detection

## 1. 학습 목표
2시그마와 3시그마 구역을 이용한 간단한 Western Electric 규칙을 적용합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
압력 평균과 표준편차를 계산하라.
최근 3개 중 2개 이상이 같은 방향으로 평균±2표준편차를 넘으면 zone_rule_violation으로
표시하라. 위쪽과 아래쪽 규칙을 모두 검사하고 위반 행을 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage03
python examples\ex052_zone_rule_detection.py
```

## 4. 예상 결과
최근 3개 중 2개가 2시그마 밖에 위치한 구간이 탐지됩니다.

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
| 15 | `mean_value = sensor_df["chamber_pressure_pa"].mean()` | 데이터의 평균을 계산합니다. |
| 16 | `std_value = sensor_df["chamber_pressure_pa"].std(ddof=1)` | 데이터의 표준편차를 계산합니다. |
| 17 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 18 | `upper_2s = mean_value + 2 * std_value` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 19 | `lower_2s = mean_value - 2 * std_value` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 20 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 21 | `above_upper = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 22 | `    sensor_df["chamber_pressure_pa"] > upper_2s` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 23 | `).astype(int)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 24 | `below_lower = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 25 | `    sensor_df["chamber_pressure_pa"] < lower_2s` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 26 | `).astype(int)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 27 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 28 | `upper_count = above_upper.rolling(window=3).sum()` | 지정한 구간의 이동통계를 계산합니다. |
| 29 | `lower_count = below_lower.rolling(window=3).sum()` | 지정한 구간의 이동통계를 계산합니다. |
| 30 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 31 | `sensor_df["zone_rule_violation"] = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 32 | `    (upper_count >= 2)` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 33 | `    \| (lower_count >= 2)` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 34 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 35 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 36 | `violation_df = sensor_df.loc[` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 37 | `    sensor_df["zone_rule_violation"],` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 38 | `    ["timestamp", "chamber_pressure_pa"],` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 39 | `]` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 40 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 41 | `print("Zone 규칙 위반 행 수:", len(violation_df))` | 실행 결과를 콘솔에 출력합니다. |
| 42 | `violation_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 43 | `    OUTPUT_DIR / "ex052_zone_rule_violations.csv",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 44 | `    index=False,` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 45 | `    encoding="utf-8-sig",` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 46 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 관리한계와 규격한계는 어떻게 다른가?
2. 공정 조건이나 레시피가 바뀌면 기준선을 다시 계산해야 하는가?
3. 경보가 발생했을 때 자동 정지와 작업자 확인 중 어떤 절차가 필요한가?