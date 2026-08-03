# 실습 045 — three_sigma_limits

## 1. 학습 목표
평균과 표준편차를 이용해 3시그마 관리한계를 계산합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
챔버 압력의 평균과 표준편차를 계산하고 중심선 CL, 상한 UCL, 하한 LCL을
평균 ± 3표준편차로 계산하라. 관리한계를 벗어난 행을 출력하고 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage03
python examples\ex045_three_sigma_limits.py
```

## 4. 예상 결과
압력 중심선과 3시그마 관리한계, 관리한계 이탈 행이 출력됩니다.

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
| 15 | `pressure_mean = sensor_df["chamber_pressure_pa"].mean()` | 데이터의 평균을 계산합니다. |
| 16 | `pressure_std = sensor_df["chamber_pressure_pa"].std(ddof=1)` | 데이터의 표준편차를 계산합니다. |
| 17 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 18 | `cl = pressure_mean` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 19 | `ucl = pressure_mean + 3 * pressure_std` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 20 | `lcl = pressure_mean - 3 * pressure_std` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 21 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 22 | `sensor_df["pressure_out_of_control"] = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 23 | `    (sensor_df["chamber_pressure_pa"] > ucl)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 24 | `    \| (sensor_df["chamber_pressure_pa"] < lcl)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 25 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 26 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 27 | `problem_df = sensor_df.loc[` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 28 | `    sensor_df["pressure_out_of_control"],` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 29 | `    ["timestamp", "lot_id", "chamber_pressure_pa"],` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 30 | `]` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 31 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 32 | `print(f"CL={cl:.3f}, UCL={ucl:.3f}, LCL={lcl:.3f}")` | 실행 결과를 콘솔에 출력합니다. |
| 33 | `print("관리한계 이탈 수:", len(problem_df))` | 실행 결과를 콘솔에 출력합니다. |
| 34 | `print(problem_df.round(3))` | 실행 결과를 콘솔에 출력합니다. |
| 35 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 36 | `problem_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 37 | `    OUTPUT_DIR / "ex045_pressure_out_of_control.csv",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 38 | `    index=False,` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 39 | `    encoding="utf-8-sig",` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 40 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 관리한계와 규격한계는 어떻게 다른가?
2. 공정 조건이나 레시피가 바뀌면 기준선을 다시 계산해야 하는가?
3. 경보가 발생했을 때 자동 정지와 작업자 확인 중 어떤 절차가 필요한가?