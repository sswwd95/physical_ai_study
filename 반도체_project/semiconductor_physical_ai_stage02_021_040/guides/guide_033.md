# 실습 033 — iqr_outlier_flags

## 1. 학습 목표
IQR 방식으로 연속형 센서의 통계적 이상값 후보를 플래그 처리합니다.

## 2. Antigravity용 하네스 프롬프트
```text
온도, 압력, RF 전력, 가스 유량, 진동에 대해 Q1, Q3, IQR을 계산하고
1.5*IQR 바깥 값을 이상 후보로 표시하라. 컬럼별 이상 후보 수와 경계값을 출력하고
플래그가 포함된 CSV를 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage02
python examples\ex033_iqr_outlier_flags.py
```

## 4. 예상 결과
센서별 IQR 경계와 이상 후보 건수가 출력됩니다.

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
| 17 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 18 | `sensor_columns = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `    "chamber_temp_c",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 20 | `    "chamber_pressure_pa",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 21 | `    "rf_power_w",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 22 | `    "gas_flow_sccm",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 23 | `    "vibration_g",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 24 | `]` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 25 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 26 | `flag_columns = []` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `for column in sensor_columns:` | 여러 컬럼이나 행에 같은 검사를 반복합니다. |
| 28 | `    q1 = sensor_df[column].quantile(0.25)` | 분포의 분위수를 계산해 이상값 경계를 구합니다. |
| 29 | `    q3 = sensor_df[column].quantile(0.75)` | 분포의 분위수를 계산해 이상값 경계를 구합니다. |
| 30 | `    iqr = q3 - q1` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `    lower = q1 - 1.5 * iqr` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `    upper = q3 + 1.5 * iqr` | 계산 결과나 설정값을 변수에 저장합니다. |
| 33 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 34 | `    flag_column = f"{column}_iqr_outlier"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 35 | `    sensor_df[flag_column] = ~sensor_df[column].between(lower, upper)` | 센서값이 허용 범위 안에 있는지 검사합니다. |
| 36 | `    flag_columns.append(flag_column)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 37 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 38 | `    print(` | 실행 결과를 콘솔에 출력합니다. |
| 39 | `        column,` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 40 | `        f"하한={lower:.3f}",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 41 | `        f"상한={upper:.3f}",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `        f"이상 후보={int(sensor_df[flag_column].sum())}",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 43 | `    )` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 44 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 45 | `sensor_df["any_iqr_outlier"] = sensor_df[flag_columns].any(axis=1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 46 | `sensor_df.to_csv(` | 처리 결과를 CSV 파일로 저장합니다. |
| 47 | `    OUTPUT_DIR / "ex033_iqr_outlier_flags.csv",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 48 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 49 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 50 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |

## 6. 실무 확장 질문
1. 이 검사 규칙의 기준값은 누가 승인해야 하는가?
2. 원본 데이터를 보존하면서 정제 이력을 남기려면 무엇이 필요한가?
3. 장비·챔버·레시피별로 기준값이 달라질 때 코드를 어떻게 바꿀 것인가?