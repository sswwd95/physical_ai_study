# 실습 030 — timestamp_monotonicity

## 1. 학습 목표
시간축이 증가하는지 검사하고 역순·동일 시각 데이터를 찾습니다.

## 2. Antigravity용 하네스 프롬프트
```text
오류 연습 데이터의 timestamp를 datetime으로 변환하라.
원래 행 순서에서 시간이 이전 행보다 작거나 같은 위치를 찾고
timestamp_monotonic 플래그와 시간 차이 초를 계산하라.
문제 행을 출력하고 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage02
python examples\ex030_timestamp_monotonicity.py
```

## 4. 예상 결과
역순 또는 동일 시각으로 인해 시간 차이가 0 이하인 행이 출력됩니다.

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
| 20 | `quality_df = pd.read_csv(QUALITY_FILE, parse_dates=["timestamp"])` | CSV 센서 데이터를 DataFrame으로 읽습니다. |
| 21 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 22 | `quality_df["time_diff_seconds"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `    quality_df["timestamp"].diff().dt.total_seconds()` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 24 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 25 | `quality_df["timestamp_monotonic"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `    quality_df["time_diff_seconds"].isna()` | 결측값의 위치나 개수를 확인합니다. |
| 27 | `    \| (quality_df["time_diff_seconds"] > 0)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 28 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 29 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 30 | `problem_df = quality_df.loc[` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `    ~quality_df["timestamp_monotonic"],` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 32 | `    ["timestamp", "lot_id", "time_diff_seconds"],` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 33 | `]` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 34 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 35 | `print("시간축 문제 행 수:", len(problem_df))` | 실행 결과를 콘솔에 출력합니다. |
| 36 | `print(problem_df)` | 실행 결과를 콘솔에 출력합니다. |
| 37 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 38 | `problem_df.to_csv(` | 처리 결과를 CSV 파일로 저장합니다. |
| 39 | `    OUTPUT_DIR / "ex030_timestamp_problems.csv",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 40 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 41 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |

## 6. 실무 확장 질문
1. 이 검사 규칙의 기준값은 누가 승인해야 하는가?
2. 원본 데이터를 보존하면서 정제 이력을 남기려면 무엇이 필요한가?
3. 장비·챔버·레시피별로 기준값이 달라질 때 코드를 어떻게 바꿀 것인가?