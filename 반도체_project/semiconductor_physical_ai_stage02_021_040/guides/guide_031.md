# 실습 031 — sampling_interval_check

## 1. 학습 목표
예상 샘플링 주기 1초에서 벗어난 누락·지연·중복 시점을 탐지합니다.

## 2. Antigravity용 하네스 프롬프트
```text
timestamp를 정렬한 뒤 인접 행 시간 차이를 계산하라.
예상 주기는 1초이며 1초가 아닌 간격을 gap_type으로 분류하라.
0초 이하는 duplicate_or_reverse, 1초 초과는 missing_or_delay로 표시하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage02
python examples\ex031_sampling_interval_check.py
```

## 4. 예상 결과
1초가 아닌 간격이 유형별로 표시됩니다.

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
| 21 | `quality_df = quality_df.sort_values("timestamp").reset_index(drop=True)` | 데이터를 지정한 기준으로 정렬합니다. |
| 22 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 23 | `quality_df["interval_seconds"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `    quality_df["timestamp"].diff().dt.total_seconds()` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 25 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 26 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 27 | `def classify_gap(interval):` | 반복 사용할 품질검사 기능을 함수로 정의합니다. |
| 28 | `    if pd.isna(interval) or interval == 1:` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `        return "normal"` | 함수의 검사 결과를 호출한 곳에 돌려줍니다. |
| 30 | `    if interval <= 0:` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `        return "duplicate_or_reverse"` | 함수의 검사 결과를 호출한 곳에 돌려줍니다. |
| 32 | `    return "missing_or_delay"` | 함수의 검사 결과를 호출한 곳에 돌려줍니다. |
| 33 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 34 | `quality_df["gap_type"] = quality_df["interval_seconds"].apply(classify_gap)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 35 | `gap_df = quality_df.loc[quality_df["gap_type"] != "normal"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 36 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 37 | `print(gap_df[["timestamp", "interval_seconds", "gap_type"]])` | 실행 결과를 콘솔에 출력합니다. |
| 38 | `gap_df.to_csv(` | 처리 결과를 CSV 파일로 저장합니다. |
| 39 | `    OUTPUT_DIR / "ex031_sampling_interval_gaps.csv",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 40 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 41 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |

## 6. 실무 확장 질문
1. 이 검사 규칙의 기준값은 누가 승인해야 하는가?
2. 원본 데이터를 보존하면서 정제 이력을 남기려면 무엇이 필요한가?
3. 장비·챔버·레시피별로 기준값이 달라질 때 코드를 어떻게 바꿀 것인가?