# 실습 036 — state_transition_check

## 1. 학습 목표
공정 상태 전이가 허용된 순서인지 검사하는 상태머신 기초를 익힙니다.

## 2. Antigravity용 하네스 프롬프트
```text
허용 전이는 stabilize→stabilize/process, process→process/purge,
purge→purge/stabilize로 정의하라. 현재 행과 다음 행의 process_state를 비교해
허용되지 않은 전이를 찾고 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage02
python examples\ex036_state_transition_check.py
```

## 4. 예상 결과
기본 데이터의 상태 전이 중 허용 규칙을 위반한 구간이 있는지 출력됩니다.

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
| 17 | `sensor_df = sensor_df.sort_values("timestamp").reset_index(drop=True)` | 데이터를 지정한 기준으로 정렬합니다. |
| 18 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 19 | `allowed_transitions = {` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `    ("stabilize", "stabilize"),` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 21 | `    ("stabilize", "process"),` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 22 | `    ("process", "process"),` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 23 | `    ("process", "purge"),` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 24 | `    ("purge", "purge"),` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 25 | `    ("purge", "stabilize"),` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 26 | `}` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 27 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 28 | `sensor_df["next_state"] = sensor_df["process_state"].shift(-1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `sensor_df["transition_allowed"] = sensor_df.apply(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `    lambda row: True` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 31 | `    if pd.isna(row["next_state"])` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 32 | `    else (row["process_state"], row["next_state"]) in allowed_transitions,` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 33 | `    axis=1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 34 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 35 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 36 | `invalid_df = sensor_df.loc[` | 계산 결과나 설정값을 변수에 저장합니다. |
| 37 | `    ~sensor_df["transition_allowed"],` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 38 | `    ["timestamp", "process_state", "next_state"],` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 39 | `]` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 40 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 41 | `print("잘못된 상태 전이 수:", len(invalid_df))` | 실행 결과를 콘솔에 출력합니다. |
| 42 | `print(invalid_df)` | 실행 결과를 콘솔에 출력합니다. |
| 43 | `invalid_df.to_csv(` | 처리 결과를 CSV 파일로 저장합니다. |
| 44 | `    OUTPUT_DIR / "ex036_invalid_state_transitions.csv",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 45 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 46 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 47 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |

## 6. 실무 확장 질문
1. 이 검사 규칙의 기준값은 누가 승인해야 하는가?
2. 원본 데이터를 보존하면서 정제 이력을 남기려면 무엇이 필요한가?
3. 장비·챔버·레시피별로 기준값이 달라질 때 코드를 어떻게 바꿀 것인가?