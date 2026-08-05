# 실습 035 — lot_consistency_check

## 1. 학습 목표
한 LOT 안에서 공정 상태 순서와 행 개수를 점검하는 기초 일관성 검사를 수행합니다.

## 2. Antigravity용 하네스 프롬프트
```text
각 lot_id별 행 수, 첫 시각, 마지막 시각, process_state 고유값을 요약하라.
LOT별 행 수가 100이 아니면 lot_count_error를 True로 표시하라.
결과를 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage02
python examples\ex035_lot_consistency_check.py
```

## 4. 예상 결과
각 LOT의 100행 여부와 시간 범위, 상태 구성이 요약됩니다.

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
| 16 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | CSV 센서 데이터를 DataFrame으로 읽습니다. |
| 17 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 18 | `lot_summary = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `    sensor_df.groupby("lot_id")` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 20 | `    .agg(` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 21 | `        row_count=("timestamp", "size"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `        first_timestamp=("timestamp", "min"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `        last_timestamp=("timestamp", "max"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `        state_count=("process_state", "nunique"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `        states=("process_state", lambda x: ",".join(sorted(x.unique()))),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `    )` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 27 | `    .reset_index()` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 28 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 29 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 30 | `lot_summary["lot_count_error"] = lot_summary["row_count"] != 100` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 32 | `print(lot_summary)` | 실행 결과를 콘솔에 출력합니다. |
| 33 | `lot_summary.to_csv(` | 처리 결과를 CSV 파일로 저장합니다. |
| 34 | `    OUTPUT_DIR / "ex035_lot_consistency.csv",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 35 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 36 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 37 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |

## 6. 실무 확장 질문
1. 이 검사 규칙의 기준값은 누가 승인해야 하는가?
2. 원본 데이터를 보존하면서 정제 이력을 남기려면 무엇이 필요한가?
3. 장비·챔버·레시피별로 기준값이 달라질 때 코드를 어떻게 바꿀 것인가?