# 실습 059 — spc_dashboard_data

## 1. 학습 목표
관리도와 KPI에 사용할 통합 대시보드 데이터를 생성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
timestamp별 온도, 압력, EWMA, 온도 UCL/LCL, 압력 UCL/LCL,
규격 이탈 여부, 위험점수를 포함하는 대시보드용 CSV를 생성하라.
모든 기준값은 데이터에서 계산하고 결과의 마지막 10행을 출력하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage03
python examples\ex059_spc_dashboard_data.py
```

## 4. 예상 결과
SPC 대시보드에서 바로 사용할 시계열 기준선과 위험지표 CSV가 생성됩니다.

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
| 20 | `sensor_df["temp_ewma"] = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 21 | `    sensor_df["chamber_temp_c"]` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 22 | `    .ewm(span=20, adjust=False)` | 최근 데이터에 더 큰 가중치를 주는 지수이동통계를 계산합니다. |
| 23 | `    .mean()` | 데이터의 평균을 계산합니다. |
| 24 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 25 | `sensor_df["temp_ucl"] = temp_mean + 3 * temp_std` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 26 | `sensor_df["temp_lcl"] = temp_mean - 3 * temp_std` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 27 | `sensor_df["pressure_ucl"] = pressure_mean + 3 * pressure_std` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 28 | `sensor_df["pressure_lcl"] = pressure_mean - 3 * pressure_std` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 29 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 30 | `sensor_df["spec_violation"] = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 31 | `    ~sensor_df["chamber_temp_c"].between(69, 75)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 32 | `    \| ~sensor_df["chamber_pressure_pa"].between(17, 19)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 33 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 34 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 35 | `sensor_df["risk_score"] = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 36 | `    (` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 37 | `        sensor_df["chamber_temp_c"] > sensor_df["temp_ucl"]` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 38 | `    ).astype(int) * 40` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 39 | `    + (` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 40 | `        sensor_df["chamber_pressure_pa"] > sensor_df["pressure_ucl"]` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 41 | `    ).astype(int) * 30` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 42 | `    + (` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 43 | `        sensor_df["vibration_g"] >= 0.15` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 44 | `    ).astype(int) * 20` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 45 | `    + (` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 46 | `        sensor_df["particle_count"] >= 10` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 47 | `    ).astype(int) * 10` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 48 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 49 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 50 | `dashboard_columns = [` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 51 | `    "timestamp",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 52 | `    "lot_id",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 53 | `    "chamber_temp_c",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 54 | `    "chamber_pressure_pa",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 55 | `    "temp_ewma",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 56 | `    "temp_ucl",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 57 | `    "temp_lcl",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 58 | `    "pressure_ucl",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 59 | `    "pressure_lcl",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 60 | `    "spec_violation",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 61 | `    "risk_score",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 62 | `]` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 63 | `dashboard_df = sensor_df[dashboard_columns]` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 64 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 65 | `print(dashboard_df.tail(10).round(3))` | 실행 결과를 콘솔에 출력합니다. |
| 66 | `dashboard_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 67 | `    OUTPUT_DIR / "ex059_spc_dashboard_data.csv",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 68 | `    index=False,` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 69 | `    encoding="utf-8-sig",` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 70 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 관리한계와 규격한계는 어떻게 다른가?
2. 공정 조건이나 레시피가 바뀌면 기준선을 다시 계산해야 하는가?
3. 경보가 발생했을 때 자동 정지와 작업자 확인 중 어떤 절차가 필요한가?