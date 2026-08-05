# 실습 025 — inject_quality_errors

## 1. 학습 목표
후속 품질검사를 위해 결측·중복·역순 시간·잘못된 범주값을 포함한 연습 데이터를 만듭니다.

## 2. Antigravity용 하네스 프롬프트
```text
원본 센서 데이터를 복사하여 품질 오류 연습용 CSV를 생성하라.
압력 결측 4건, RF 전력 결측 3건, 중복 행 2건, timestamp 역순 1건,
잘못된 process_state 값 unknown 2건을 삽입하라.
원본은 수정하지 말고 오류 삽입 내역을 출력하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage02
python examples\ex025_inject_quality_errors.py
```

## 4. 예상 결과
302행의 오류 연습용 CSV가 생성되고 삽입한 오류 개수가 출력됩니다.

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
| 17 | `quality_df = sensor_df.copy()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 18 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 19 | `quality_df.loc[[15, 80, 155, 260], "chamber_pressure_pa"] = np.nan` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `quality_df.loc[[40, 140, 240], "rf_power_w"] = np.nan` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `quality_df.loc[[35, 135], "process_state"] = "unknown"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `quality_df.loc[200, "timestamp"] = quality_df.loc[150, "timestamp"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 24 | `duplicate_rows = quality_df.iloc[[20, 21]].copy()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `quality_df = pd.concat([quality_df, duplicate_rows], ignore_index=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 27 | `output_file = ROOT / "data" / "sensor_data_with_quality_errors.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `quality_df.to_csv(output_file, index=False, encoding="utf-8-sig")` | 처리 결과를 CSV 파일로 저장합니다. |
| 29 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 30 | `print("오류 연습 데이터 저장:", output_file)` | 실행 결과를 콘솔에 출력합니다. |
| 31 | `print("행 수:", len(quality_df))` | 실행 결과를 콘솔에 출력합니다. |
| 32 | `print("압력 결측:", int(quality_df["chamber_pressure_pa"].isna().sum()))` | 결측값의 위치나 개수를 확인합니다. |
| 33 | `print("RF 결측:", int(quality_df["rf_power_w"].isna().sum()))` | 결측값의 위치나 개수를 확인합니다. |
| 34 | `print("unknown 상태:", int((quality_df["process_state"] == "unknown").sum()))` | 실행 결과를 콘솔에 출력합니다. |
| 35 | `print("완전 중복:", int(quality_df.duplicated().sum()))` | 중복 행 또는 중복 키를 검사합니다. |

## 6. 실무 확장 질문
1. 이 검사 규칙의 기준값은 누가 승인해야 하는가?
2. 원본 데이터를 보존하면서 정제 이력을 남기려면 무엇이 필요한가?
3. 장비·챔버·레시피별로 기준값이 달라질 때 코드를 어떻게 바꿀 것인가?