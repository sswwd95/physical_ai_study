# 실습 024 — allowed_range_check

## 1. 학습 목표
공정 엔지니어가 정의한 허용 범위 밖의 센서값을 플래그로 표시합니다.

## 2. Antigravity용 하네스 프롬프트
```text
센서별 허용 범위를 딕셔너리로 정의하라.
온도 65~80°C, 압력 15~22Pa, RF 780~920W, 가스 105~135sccm,
진동 0~0.25g, 입자 수 0~40으로 검사하라.
각 센서별 범위 위반 건수와 전체 품질 플래그를 출력하고 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage02
python examples\ex024_allowed_range_check.py
```

## 4. 예상 결과
센서별 범위 위반 건수와 행 단위 전체 위반 플래그가 생성됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 Python 기능이나 라이브러리를 불러옵니다. |
| 2 | `import numpy as np` | 필요한 Python 기능이나 라이브러리를 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 Python 기능이나 라이브러리를 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError(` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 12 | `        "기본 데이터가 없습니다. 프로젝트 루트에서 "` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 13 | `        "python generate_base_data.py를 먼저 실행하세요."` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 14 | `    )` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 15 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 16 | `sensor_df = pd.read_csv(DATA_FILE)` | CSV 센서 데이터를 DataFrame으로 읽습니다. |
| 17 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 18 | `allowed_ranges = {` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `    "chamber_temp_c": (65.0, 80.0),` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 20 | `    "chamber_pressure_pa": (15.0, 22.0),` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 21 | `    "rf_power_w": (780.0, 920.0),` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 22 | `    "gas_flow_sccm": (105.0, 135.0),` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 23 | `    "vibration_g": (0.0, 0.25),` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 24 | `    "particle_count": (0, 40),` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 25 | `}` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 26 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 27 | `violation_columns = []` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `for column, (lower, upper) in allowed_ranges.items():` | 여러 컬럼이나 행에 같은 검사를 반복합니다. |
| 29 | `    flag_column = f"{column}_range_violation"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `    sensor_df[flag_column] = ~sensor_df[column].between(lower, upper)` | 센서값이 허용 범위 안에 있는지 검사합니다. |
| 31 | `    violation_columns.append(flag_column)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 32 | `    print(column, "위반 건수:", int(sensor_df[flag_column].sum()))` | 실행 결과를 콘솔에 출력합니다. |
| 33 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 34 | `sensor_df["any_range_violation"] = sensor_df[violation_columns].any(axis=1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 35 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 36 | `print("전체 범위 위반 행:", int(sensor_df["any_range_violation"].sum()))` | 실행 결과를 콘솔에 출력합니다. |
| 37 | `sensor_df.to_csv(` | 처리 결과를 CSV 파일로 저장합니다. |
| 38 | `    OUTPUT_DIR / "ex024_allowed_range_check.csv",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 39 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 40 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 41 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |

## 6. 실무 확장 질문
1. 이 검사 규칙의 기준값은 누가 승인해야 하는가?
2. 원본 데이터를 보존하면서 정제 이력을 남기려면 무엇이 필요한가?
3. 장비·챔버·레시피별로 기준값이 달라질 때 코드를 어떻게 바꿀 것인가?