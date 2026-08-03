# 실습 028 — duplicate_key_check

## 1. 학습 목표
timestamp와 lot_id 복합키의 중복을 검사하고 원인을 분리해 확인합니다.

## 2. Antigravity용 하네스 프롬프트
```text
오류 연습 데이터에서 완전 중복과 timestamp+lot_id 복합키 중복을 각각 검사하라.
중복 행을 모두 출력하고 별도 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage02
python examples\ex028_duplicate_key_check.py
```

## 4. 예상 결과
완전 중복과 복합키 중복이 구분되어 출력됩니다.

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
| 16 | `QUALITY_FILE = ROOT / "data" / "sensor_data_with_quality_errors.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 17 | `if not QUALITY_FILE.exists():` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 18 | `    raise FileNotFoundError("실습 025를 먼저 실행하세요.")` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 19 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 20 | `quality_df = pd.read_csv(QUALITY_FILE)` | CSV 센서 데이터를 DataFrame으로 읽습니다. |
| 21 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 22 | `full_duplicate_mask = quality_df.duplicated(keep=False)` | 중복 행 또는 중복 키를 검사합니다. |
| 23 | `key_duplicate_mask = quality_df.duplicated(` | 중복 행 또는 중복 키를 검사합니다. |
| 24 | `    subset=["timestamp", "lot_id"],` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `    keep=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 27 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 28 | `full_duplicates = quality_df.loc[full_duplicate_mask]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `key_duplicates = quality_df.loc[key_duplicate_mask].sort_values(` | 데이터를 지정한 기준으로 정렬합니다. |
| 30 | `    ["timestamp", "lot_id"]` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 31 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 32 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 33 | `print("완전 중복 행 수:", len(full_duplicates))` | 실행 결과를 콘솔에 출력합니다. |
| 34 | `print("복합키 중복 행 수:", len(key_duplicates))` | 실행 결과를 콘솔에 출력합니다. |
| 35 | `print(key_duplicates[["timestamp", "lot_id", "process_state"]])` | 실행 결과를 콘솔에 출력합니다. |
| 36 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 37 | `key_duplicates.to_csv(` | 처리 결과를 CSV 파일로 저장합니다. |
| 38 | `    OUTPUT_DIR / "ex028_duplicate_keys.csv",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 39 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 40 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 41 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |

## 6. 실무 확장 질문
1. 이 검사 규칙의 기준값은 누가 승인해야 하는가?
2. 원본 데이터를 보존하면서 정제 이력을 남기려면 무엇이 필요한가?
3. 장비·챔버·레시피별로 기준값이 달라질 때 코드를 어떻게 바꿀 것인가?