# 실습 029 — remove_duplicates_with_audit

## 1. 학습 목표
중복 제거 전후의 행 수와 제거 대상을 감사 로그로 남깁니다.

## 2. Antigravity용 하네스 프롬프트
```text
오류 연습 데이터에서 완전 중복 행을 제거하라.
제거되는 행은 duplicate_audit.csv에, 정제 데이터는 cleaned_no_duplicates.csv에 저장하라.
처리 전후 행 수와 제거 수를 출력하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage02
python examples\ex029_remove_duplicates_with_audit.py
```

## 4. 예상 결과
중복 2건이 감사 로그에 저장되고 정제 데이터는 300행이 됩니다.

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
| 22 | `duplicate_mask = quality_df.duplicated(keep="first")` | 중복 행 또는 중복 키를 검사합니다. |
| 23 | `duplicate_audit = quality_df.loc[duplicate_mask].copy()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `clean_df = quality_df.loc[~duplicate_mask].copy().reset_index(drop=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 26 | `print("처리 전:", len(quality_df))` | 실행 결과를 콘솔에 출력합니다. |
| 27 | `print("제거 수:", int(duplicate_mask.sum()))` | 실행 결과를 콘솔에 출력합니다. |
| 28 | `print("처리 후:", len(clean_df))` | 실행 결과를 콘솔에 출력합니다. |
| 29 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 30 | `duplicate_audit.to_csv(` | 처리 결과를 CSV 파일로 저장합니다. |
| 31 | `    OUTPUT_DIR / "ex029_duplicate_audit.csv",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 32 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 33 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 34 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 35 | `clean_df.to_csv(` | 처리 결과를 CSV 파일로 저장합니다. |
| 36 | `    OUTPUT_DIR / "ex029_cleaned_no_duplicates.csv",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 37 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 38 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 39 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |

## 6. 실무 확장 질문
1. 이 검사 규칙의 기준값은 누가 승인해야 하는가?
2. 원본 데이터를 보존하면서 정제 이력을 남기려면 무엇이 필요한가?
3. 장비·챔버·레시피별로 기준값이 달라질 때 코드를 어떻게 바꿀 것인가?