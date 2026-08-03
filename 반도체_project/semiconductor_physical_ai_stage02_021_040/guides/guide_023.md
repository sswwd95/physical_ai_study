# 실습 023 — unit_conversion

## 1. 학습 목표
센서 단위를 변환하면서 원본 단위 컬럼을 보존하는 방법을 익힙니다.

## 2. Antigravity용 하네스 프롬프트
```text
온도 °C를 K로, 압력 Pa를 kPa로, 진동 g를 m/s²로 변환하는 파생 컬럼을 추가하라.
원본 컬럼을 유지하고 변환 공식을 주석으로 설명하며 결과를 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage02
python examples\ex023_unit_conversion.py
```

## 4. 예상 결과
원본 단위와 변환 단위를 함께 가진 결과 CSV가 생성됩니다.

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
| 18 | `sensor_df["chamber_temp_k"] = sensor_df["chamber_temp_c"] + 273.15` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `sensor_df["chamber_pressure_kpa"] = sensor_df["chamber_pressure_pa"] / 1000.0` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `sensor_df["vibration_m_s2"] = sensor_df["vibration_g"] * 9.80665` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 22 | `result_columns = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `    "timestamp",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 24 | `    "chamber_temp_c",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 25 | `    "chamber_temp_k",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 26 | `    "chamber_pressure_pa",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 27 | `    "chamber_pressure_kpa",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 28 | `    "vibration_g",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 29 | `    "vibration_m_s2",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 30 | `]` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 31 | `result_df = sensor_df[result_columns]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 33 | `print(result_df.head().round(5))` | 실행 결과를 콘솔에 출력합니다. |
| 34 | `result_df.to_csv(` | 처리 결과를 CSV 파일로 저장합니다. |
| 35 | `    OUTPUT_DIR / "ex023_unit_conversion.csv",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 36 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 37 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 38 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |

## 6. 실무 확장 질문
1. 이 검사 규칙의 기준값은 누가 승인해야 하는가?
2. 원본 데이터를 보존하면서 정제 이력을 남기려면 무엇이 필요한가?
3. 장비·챔버·레시피별로 기준값이 달라질 때 코드를 어떻게 바꿀 것인가?