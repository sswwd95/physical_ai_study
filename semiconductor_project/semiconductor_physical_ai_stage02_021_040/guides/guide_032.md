# 실습 032 — category_validation

## 1. 학습 목표
허용된 LOT와 공정 상태만 존재하는지 범주형 값을 검증합니다.

## 2. Antigravity용 하네스 프롬프트
```text
lot_id 허용값은 LOT-A, LOT-B, LOT-C이고 process_state 허용값은
stabilize, process, purge이다. 허용되지 않은 값을 컬럼별로 찾고
invalid_category 플래그를 생성하여 문제 행을 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage02
python examples\ex032_category_validation.py
```

## 4. 예상 결과
`unknown` 상태를 가진 2개 행이 잘못된 범주로 탐지됩니다.

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
| 22 | `allowed_lots = {"LOT-A", "LOT-B", "LOT-C"}` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `allowed_states = {"stabilize", "process", "purge"}` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 25 | `invalid_lot = ~quality_df["lot_id"].isin(allowed_lots)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `invalid_state = ~quality_df["process_state"].isin(allowed_states)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `quality_df["invalid_category"] = invalid_lot \| invalid_state` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 29 | `problem_df = quality_df.loc[` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `    quality_df["invalid_category"],` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 31 | `    ["timestamp", "lot_id", "process_state", "invalid_category"],` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 32 | `]` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 33 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 34 | `print("잘못된 범주 행 수:", len(problem_df))` | 실행 결과를 콘솔에 출력합니다. |
| 35 | `print(problem_df)` | 실행 결과를 콘솔에 출력합니다. |
| 36 | `problem_df.to_csv(` | 처리 결과를 CSV 파일로 저장합니다. |
| 37 | `    OUTPUT_DIR / "ex032_invalid_categories.csv",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 38 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 39 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 40 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |

## 6. 실무 확장 질문
1. 이 검사 규칙의 기준값은 누가 승인해야 하는가?
2. 원본 데이터를 보존하면서 정제 이력을 남기려면 무엇이 필요한가?
3. 장비·챔버·레시피별로 기준값이 달라질 때 코드를 어떻게 바꿀 것인가?