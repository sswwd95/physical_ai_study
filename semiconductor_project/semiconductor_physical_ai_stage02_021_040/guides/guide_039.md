# 실습 039 — quality_report

## 1. 학습 목표
여러 품질 지표를 한 번에 요약하는 자동 리포트를 생성합니다.

## 2. Antigravity용 하네스 프롬프트
```text
오류 연습 데이터의 행 수, 컬럼 수, 결측 셀 수, 완전 중복 수,
잘못된 상태 수, 범위 위반 행 수를 한 행의 품질 요약표로 작성하라.
컬럼별 결측표와 함께 Excel의 summary, missing_by_column 시트로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage02
python examples\ex039_quality_report.py
```

## 4. 예상 결과
품질 요약과 컬럼별 결측 현황이 두 시트의 Excel 보고서로 저장됩니다.

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
| 22 | `range_violation = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `    ~quality_df["chamber_temp_c"].between(65, 80)` | 센서값이 허용 범위 안에 있는지 검사합니다. |
| 24 | `    \| ~quality_df["chamber_pressure_pa"].between(15, 22)` | 센서값이 허용 범위 안에 있는지 검사합니다. |
| 25 | `    \| ~quality_df["rf_power_w"].between(780, 920)` | 센서값이 허용 범위 안에 있는지 검사합니다. |
| 26 | `    \| ~quality_df["gas_flow_sccm"].between(105, 135)` | 센서값이 허용 범위 안에 있는지 검사합니다. |
| 27 | `    \| ~quality_df["vibration_g"].between(0, 0.25)` | 센서값이 허용 범위 안에 있는지 검사합니다. |
| 28 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 29 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 30 | `summary_df = pd.DataFrame([{` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `    "row_count": len(quality_df),` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 32 | `    "column_count": len(quality_df.columns),` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 33 | `    "missing_cell_count": int(quality_df.isna().sum().sum()),` | 결측값의 위치나 개수를 확인합니다. |
| 34 | `    "full_duplicate_count": int(quality_df.duplicated().sum()),` | 중복 행 또는 중복 키를 검사합니다. |
| 35 | `    "invalid_state_count": int(` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 36 | `        (~quality_df["process_state"].isin(["stabilize", "process", "purge"])).sum()` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 37 | `    ),` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 38 | `    "range_violation_row_count": int(range_violation.sum()),` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 39 | `}])` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 40 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 41 | `missing_df = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `    quality_df.isna()` | 결측값의 위치나 개수를 확인합니다. |
| 43 | `    .sum()` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 44 | `    .rename("missing_count")` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 45 | `    .reset_index()` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 46 | `    .rename(columns={"index": "column"})` | 계산 결과나 설정값을 변수에 저장합니다. |
| 47 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 48 | `missing_df["missing_ratio"] = missing_df["missing_count"] / len(quality_df)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 49 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 50 | `output_file = OUTPUT_DIR / "ex039_quality_report.xlsx"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 51 | `with pd.ExcelWriter(output_file, engine="openpyxl") as writer:` | 계산 결과나 설정값을 변수에 저장합니다. |
| 52 | `    summary_df.to_excel(writer, sheet_name="summary", index=False)` | 품질검사 결과를 Excel 파일로 저장합니다. |
| 53 | `    missing_df.to_excel(writer, sheet_name="missing_by_column", index=False)` | 품질검사 결과를 Excel 파일로 저장합니다. |
| 54 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 55 | `print(summary_df)` | 실행 결과를 콘솔에 출력합니다. |
| 56 | `print("Excel 저장:", output_file)` | 실행 결과를 콘솔에 출력합니다. |

## 6. 실무 확장 질문
1. 이 검사 규칙의 기준값은 누가 승인해야 하는가?
2. 원본 데이터를 보존하면서 정제 이력을 남기려면 무엇이 필요한가?
3. 장비·챔버·레시피별로 기준값이 달라질 때 코드를 어떻게 바꿀 것인가?