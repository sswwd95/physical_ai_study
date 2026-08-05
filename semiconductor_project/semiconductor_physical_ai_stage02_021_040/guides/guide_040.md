# 실습 040 — cleaning_pipeline

## 1. 학습 목표
스키마 확인부터 정제·검증·저장까지 재사용 가능한 전처리 파이프라인을 완성합니다.

## 2. Antigravity용 하네스 프롬프트
```text
오류 연습 데이터를 입력으로 받는 clean_sensor_data 함수를 작성하라.
필수 컬럼 검사, timestamp 변환, 정렬, 완전 중복 제거, 숫자형 변환,
압력과 RF 결측 시간 보간, 잘못된 process_state를 NaN으로 변경,
품질 플래그 추가, 정제 CSV와 감사 요약 CSV 저장을 수행하라.
각 단계의 처리 건수를 audit 딕셔너리에 기록하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage02
python examples\ex040_cleaning_pipeline.py
```

## 4. 예상 결과
정제된 센서 CSV와 단계별 처리 건수를 기록한 감사 CSV가 생성됩니다.

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
| 17 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 18 | `def clean_sensor_data(input_file, clean_output, audit_output):` | 반복 사용할 품질검사 기능을 함수로 정의합니다. |
| 19 | `    required_columns = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `        "timestamp",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 21 | `        "lot_id",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 22 | `        "chamber_temp_c",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 23 | `        "chamber_pressure_pa",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 24 | `        "rf_power_w",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 25 | `        "gas_flow_sccm",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 26 | `        "vibration_g",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 27 | `        "particle_count",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 28 | `        "process_state",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 29 | `    ]` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 30 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 31 | `    sensor_df = pd.read_csv(input_file)` | CSV 센서 데이터를 DataFrame으로 읽습니다. |
| 32 | `    audit = {"input_rows": len(sensor_df)}` | 계산 결과나 설정값을 변수에 저장합니다. |
| 33 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 34 | `    missing_columns = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 35 | `        column for column in required_columns` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 36 | `        if column not in sensor_df.columns` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 37 | `    ]` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 38 | `    if missing_columns:` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 39 | `        raise ValueError(f"필수 컬럼 누락: {missing_columns}")` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 40 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 41 | `    sensor_df["timestamp"] = pd.to_datetime(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `        sensor_df["timestamp"],` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 43 | `        errors="coerce",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 44 | `    )` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 45 | `    audit["invalid_timestamp_count"] = int(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 46 | `        sensor_df["timestamp"].isna().sum()` | 결측값의 위치나 개수를 확인합니다. |
| 47 | `    )` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 48 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 49 | `    sensor_df = sensor_df.sort_values("timestamp").reset_index(drop=True)` | 데이터를 지정한 기준으로 정렬합니다. |
| 50 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 51 | `    duplicate_count = int(sensor_df.duplicated().sum())` | 중복 행 또는 중복 키를 검사합니다. |
| 52 | `    sensor_df = sensor_df.drop_duplicates().reset_index(drop=True)` | 중복 데이터를 제거합니다. |
| 53 | `    audit["removed_duplicate_count"] = duplicate_count` | 계산 결과나 설정값을 변수에 저장합니다. |
| 54 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 55 | `    numeric_columns = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 56 | `        "chamber_temp_c",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 57 | `        "chamber_pressure_pa",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 58 | `        "rf_power_w",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 59 | `        "gas_flow_sccm",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 60 | `        "vibration_g",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 61 | `        "particle_count",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 62 | `    ]` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 63 | `    for column in numeric_columns:` | 여러 컬럼이나 행에 같은 검사를 반복합니다. |
| 64 | `        sensor_df[column] = pd.to_numeric(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 65 | `            sensor_df[column],` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 66 | `            errors="coerce",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 67 | `        )` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 68 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 69 | `    sensor_df = sensor_df.set_index("timestamp")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 70 | `    interpolate_columns = ["chamber_pressure_pa", "rf_power_w"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 71 | `    before_missing = int(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 72 | `        sensor_df[interpolate_columns].isna().sum().sum()` | 결측값의 위치나 개수를 확인합니다. |
| 73 | `    )` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 74 | `    sensor_df[interpolate_columns] = sensor_df[` | 계산 결과나 설정값을 변수에 저장합니다. |
| 75 | `        interpolate_columns` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 76 | `    ].interpolate(method="time", limit_direction="both")` | 앞뒤 값을 이용해 결측값을 보간합니다. |
| 77 | `    after_missing = int(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 78 | `        sensor_df[interpolate_columns].isna().sum().sum()` | 결측값의 위치나 개수를 확인합니다. |
| 79 | `    )` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 80 | `    sensor_df = sensor_df.reset_index()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 81 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 82 | `    audit["interpolated_cell_count"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 83 | `        before_missing - after_missing` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 84 | `    )` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 85 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 86 | `    valid_states = ["stabilize", "process", "purge"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 87 | `    invalid_state_mask = ~sensor_df["process_state"].isin(valid_states)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 88 | `    audit["invalid_state_count"] = int(invalid_state_mask.sum())` | 계산 결과나 설정값을 변수에 저장합니다. |
| 89 | `    sensor_df.loc[invalid_state_mask, "process_state"] = np.nan` | 계산 결과나 설정값을 변수에 저장합니다. |
| 90 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 91 | `    sensor_df["quality_has_missing"] = sensor_df.isna().any(axis=1)` | 결측값의 위치나 개수를 확인합니다. |
| 92 | `    sensor_df["quality_range_violation"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 93 | `        ~sensor_df["chamber_temp_c"].between(65, 80)` | 센서값이 허용 범위 안에 있는지 검사합니다. |
| 94 | `        \| ~sensor_df["chamber_pressure_pa"].between(15, 22)` | 센서값이 허용 범위 안에 있는지 검사합니다. |
| 95 | `        \| ~sensor_df["rf_power_w"].between(780, 920)` | 센서값이 허용 범위 안에 있는지 검사합니다. |
| 96 | `        \| ~sensor_df["gas_flow_sccm"].between(105, 135)` | 센서값이 허용 범위 안에 있는지 검사합니다. |
| 97 | `        \| ~sensor_df["vibration_g"].between(0, 0.25)` | 센서값이 허용 범위 안에 있는지 검사합니다. |
| 98 | `    )` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 99 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 100 | `    audit["output_rows"] = len(sensor_df)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 101 | `    audit["remaining_missing_cells"] = int(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 102 | `        sensor_df.isna().sum().sum()` | 결측값의 위치나 개수를 확인합니다. |
| 103 | `    )` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 104 | `    audit["range_violation_rows"] = int(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 105 | `        sensor_df["quality_range_violation"].sum()` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 106 | `    )` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 107 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 108 | `    sensor_df.to_csv(` | 처리 결과를 CSV 파일로 저장합니다. |
| 109 | `        clean_output,` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 110 | `        index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 111 | `        encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 112 | `    )` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 113 | `    pd.DataFrame([audit]).to_csv(` | 처리 결과를 CSV 파일로 저장합니다. |
| 114 | `        audit_output,` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 115 | `        index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 116 | `        encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 117 | `    )` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 118 | `    return sensor_df, audit` | 함수의 검사 결과를 호출한 곳에 돌려줍니다. |
| 119 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 120 | `if not QUALITY_FILE.exists():` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 121 | `    raise FileNotFoundError("실습 025를 먼저 실행하세요.")` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 122 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 123 | `clean_df, audit = clean_sensor_data(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 124 | `    QUALITY_FILE,` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 125 | `    OUTPUT_DIR / "ex040_clean_sensor_data.csv",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 126 | `    OUTPUT_DIR / "ex040_cleaning_audit.csv",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 127 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 128 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 129 | `print("정제 결과 행 수:", len(clean_df))` | 실행 결과를 콘솔에 출력합니다. |
| 130 | `print("감사 요약:")` | 실행 결과를 콘솔에 출력합니다. |
| 131 | `for key, value in audit.items():` | 여러 컬럼이나 행에 같은 검사를 반복합니다. |
| 132 | `    print(f"- {key}: {value}")` | 실행 결과를 콘솔에 출력합니다. |

## 6. 실무 확장 질문
1. 이 검사 규칙의 기준값은 누가 승인해야 하는가?
2. 원본 데이터를 보존하면서 정제 이력을 남기려면 무엇이 필요한가?
3. 장비·챔버·레시피별로 기준값이 달라질 때 코드를 어떻게 바꿀 것인가?