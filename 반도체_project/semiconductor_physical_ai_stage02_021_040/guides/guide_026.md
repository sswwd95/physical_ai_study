# 실습 026 — missing_value_profile

## 1. 학습 목표
결측값의 개수와 비율을 컬럼별 품질 프로파일로 작성합니다.

## 2. Antigravity용 하네스 프롬프트
```text
sensor_data_with_quality_errors.csv를 읽고 컬럼별 결측 개수와 결측 비율을 계산하라.
결측 비율이 높은 순으로 정렬하고 quality_missing_profile.csv로 저장하라.
파일이 없으면 실습 025를 먼저 실행하라는 메시지를 표시하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage02
python examples\ex026_missing_value_profile.py
```

## 4. 예상 결과
압력 4건, RF 전력 3건의 결측과 각 비율이 컬럼별로 출력됩니다.

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
| 22 | `missing_profile = pd.DataFrame({` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `    "column": quality_df.columns,` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 24 | `    "missing_count": quality_df.isna().sum().values,` | 결측값의 위치나 개수를 확인합니다. |
| 25 | `    "missing_ratio": quality_df.isna().mean().values,` | 결측값의 위치나 개수를 확인합니다. |
| 26 | `}).sort_values("missing_ratio", ascending=False)` | 데이터를 지정한 기준으로 정렬합니다. |
| 27 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 28 | `print(missing_profile)` | 실행 결과를 콘솔에 출력합니다. |
| 29 | `missing_profile.to_csv(` | 처리 결과를 CSV 파일로 저장합니다. |
| 30 | `    OUTPUT_DIR / "ex026_missing_profile.csv",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 31 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 33 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |

## 6. 실무 확장 질문
1. 이 검사 규칙의 기준값은 누가 승인해야 하는가?
2. 원본 데이터를 보존하면서 정제 이력을 남기려면 무엇이 필요한가?
3. 장비·챔버·레시피별로 기준값이 달라질 때 코드를 어떻게 바꿀 것인가?