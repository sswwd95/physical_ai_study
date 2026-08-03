# 실습 021 — schema_validation

## 1. 학습 목표
필수 컬럼과 컬럼 순서를 검사하여 입력 스키마 오류를 조기에 발견합니다.

## 2. Antigravity용 하네스 프롬프트
```text
반도체 센서 CSV의 필수 컬럼 9개가 모두 존재하는지 검사하는 Python 예제를 작성하라.
누락 컬럼, 예상하지 않은 컬럼, 현재 컬럼 순서를 출력하고 검사 결과를 PASS/FAIL로 표시하라.
원본 파일은 수정하지 말고 한국어 주석을 사용하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage02
python examples\ex021_schema_validation.py
```

## 4. 예상 결과
필수 컬럼 누락이 없으므로 스키마 검사 결과가 PASS로 출력됩니다.

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
| 18 | `required_columns = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `    "timestamp",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 20 | `    "lot_id",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 21 | `    "chamber_temp_c",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 22 | `    "chamber_pressure_pa",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 23 | `    "rf_power_w",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 24 | `    "gas_flow_sccm",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 25 | `    "vibration_g",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 26 | `    "particle_count",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 27 | `    "process_state",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 28 | `]` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 29 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 30 | `missing_columns = [c for c in required_columns if c not in sensor_df.columns]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `unexpected_columns = [c for c in sensor_df.columns if c not in required_columns]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 33 | `print("현재 컬럼 순서:", sensor_df.columns.tolist())` | 실행 결과를 콘솔에 출력합니다. |
| 34 | `print("누락 컬럼:", missing_columns)` | 실행 결과를 콘솔에 출력합니다. |
| 35 | `print("예상하지 않은 컬럼:", unexpected_columns)` | 실행 결과를 콘솔에 출력합니다. |
| 36 | `print("스키마 검사:", "PASS" if not missing_columns else "FAIL")` | 실행 결과를 콘솔에 출력합니다. |

## 6. 실무 확장 질문
1. 이 검사 규칙의 기준값은 누가 승인해야 하는가?
2. 원본 데이터를 보존하면서 정제 이력을 남기려면 무엇이 필요한가?
3. 장비·챔버·레시피별로 기준값이 달라질 때 코드를 어떻게 바꿀 것인가?