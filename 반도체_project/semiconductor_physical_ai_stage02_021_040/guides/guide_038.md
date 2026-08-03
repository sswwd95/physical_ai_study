# 실습 038 — quality_score

## 1. 학습 목표
행 단위 품질 플래그를 점수로 합산해 데이터 품질 등급을 만듭니다.

## 2. Antigravity용 하네스 프롬프트
```text
오류 연습 데이터에 대해 결측, 범주 오류, 범위 위반, 중복 여부를 검사하라.
각 오류는 25점 감점하고 100점에서 시작하는 quality_score를 계산하라.
90 이상 A, 75 이상 B, 50 이상 C, 나머지는 D로 등급화하여 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage02
python examples\ex038_quality_score.py
```

## 4. 예상 결과
각 행에 0~100점 품질점수와 A~D 등급이 생성됩니다.

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
| 22 | `quality_df["has_missing"] = quality_df.isna().any(axis=1)` | 결측값의 위치나 개수를 확인합니다. |
| 23 | `quality_df["invalid_state"] = ~quality_df["process_state"].isin(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `    ["stabilize", "process", "purge"]` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 25 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 26 | `quality_df["range_violation"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `    ~quality_df["chamber_temp_c"].between(65, 80)` | 센서값이 허용 범위 안에 있는지 검사합니다. |
| 28 | `    \| ~quality_df["chamber_pressure_pa"].between(15, 22)` | 센서값이 허용 범위 안에 있는지 검사합니다. |
| 29 | `    \| ~quality_df["rf_power_w"].between(780, 920)` | 센서값이 허용 범위 안에 있는지 검사합니다. |
| 30 | `    \| ~quality_df["gas_flow_sccm"].between(105, 135)` | 센서값이 허용 범위 안에 있는지 검사합니다. |
| 31 | `    \| ~quality_df["vibration_g"].between(0, 0.25)` | 센서값이 허용 범위 안에 있는지 검사합니다. |
| 32 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 33 | `quality_df["is_duplicate"] = quality_df.duplicated(keep=False)` | 중복 행 또는 중복 키를 검사합니다. |
| 34 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 35 | `penalty_columns = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 36 | `    "has_missing",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 37 | `    "invalid_state",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 38 | `    "range_violation",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 39 | `    "is_duplicate",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 40 | `]` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 41 | `quality_df["quality_score"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `    100 - quality_df[penalty_columns].sum(axis=1) * 25` | 계산 결과나 설정값을 변수에 저장합니다. |
| 43 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 44 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 45 | `quality_df["quality_grade"] = pd.cut(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 46 | `    quality_df["quality_score"],` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 47 | `    bins=[-1, 49, 74, 89, 100],` | 계산 결과나 설정값을 변수에 저장합니다. |
| 48 | `    labels=["D", "C", "B", "A"],` | 계산 결과나 설정값을 변수에 저장합니다. |
| 49 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 50 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 51 | `print(quality_df["quality_grade"].value_counts().sort_index())` | 실행 결과를 콘솔에 출력합니다. |
| 52 | `quality_df.to_csv(` | 처리 결과를 CSV 파일로 저장합니다. |
| 53 | `    OUTPUT_DIR / "ex038_quality_score.csv",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 54 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 55 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 56 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |

## 6. 실무 확장 질문
1. 이 검사 규칙의 기준값은 누가 승인해야 하는가?
2. 원본 데이터를 보존하면서 정제 이력을 남기려면 무엇이 필요한가?
3. 장비·챔버·레시피별로 기준값이 달라질 때 코드를 어떻게 바꿀 것인가?