# 실습 022 — dtype_normalization

## 1. 학습 목표
문자열·실수·정수·범주형 컬럼의 자료형을 명시적으로 정규화합니다.

## 2. Antigravity용 하네스 프롬프트
```text
timestamp는 datetime, 연속형 센서는 float, particle_count는 정수,
lot_id와 process_state는 category로 변환하라. 변환 전후 dtypes를 출력하고
정규화된 CSV를 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage02
python examples\ex022_dtype_normalization.py
```

## 4. 예상 결과
컬럼별 의도된 자료형이 출력되고 정규화된 CSV가 저장됩니다.

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
| 18 | `print("변환 전 자료형:")` | 실행 결과를 콘솔에 출력합니다. |
| 19 | `print(sensor_df.dtypes)` | 실행 결과를 콘솔에 출력합니다. |
| 20 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 21 | `sensor_df["timestamp"] = pd.to_datetime(sensor_df["timestamp"], errors="coerce")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 23 | `float_columns = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `    "chamber_temp_c",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 25 | `    "chamber_pressure_pa",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 26 | `    "rf_power_w",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 27 | `    "gas_flow_sccm",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 28 | `    "vibration_g",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 29 | `]` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 30 | `for column in float_columns:` | 여러 컬럼이나 행에 같은 검사를 반복합니다. |
| 31 | `    sensor_df[column] = pd.to_numeric(sensor_df[column], errors="coerce").astype(float)` | 데이터 형식을 명시적으로 변환합니다. |
| 32 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 33 | `sensor_df["particle_count"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 34 | `    pd.to_numeric(sensor_df["particle_count"], errors="coerce")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 35 | `    .round()` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 36 | `    .astype("Int64")` | 데이터 형식을 명시적으로 변환합니다. |
| 37 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 38 | `sensor_df["lot_id"] = sensor_df["lot_id"].astype("category")` | 데이터 형식을 명시적으로 변환합니다. |
| 39 | `sensor_df["process_state"] = sensor_df["process_state"].astype("category")` | 데이터 형식을 명시적으로 변환합니다. |
| 40 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 41 | `print("\n변환 후 자료형:")` | 실행 결과를 콘솔에 출력합니다. |
| 42 | `print(sensor_df.dtypes)` | 실행 결과를 콘솔에 출력합니다. |
| 43 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 44 | `sensor_df.to_csv(` | 처리 결과를 CSV 파일로 저장합니다. |
| 45 | `    OUTPUT_DIR / "ex022_normalized_dtypes.csv",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 46 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 47 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 48 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |

## 6. 실무 확장 질문
1. 이 검사 규칙의 기준값은 누가 승인해야 하는가?
2. 원본 데이터를 보존하면서 정제 이력을 남기려면 무엇이 필요한가?
3. 장비·챔버·레시피별로 기준값이 달라질 때 코드를 어떻게 바꿀 것인가?