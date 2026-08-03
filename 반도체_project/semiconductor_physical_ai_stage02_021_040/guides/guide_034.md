# 실습 034 — winsorize_outliers

## 1. 학습 목표
이상값을 삭제하지 않고 분위수 경계로 제한하는 Winsorization을 실습합니다.

## 2. Antigravity용 하네스 프롬프트
```text
온도와 압력 컬럼의 1% 및 99% 분위수를 구하고 clip으로 경계 밖 값을 제한하라.
원본 컬럼은 유지하고 _winsorized 컬럼을 추가하라.
변경된 행 수와 전후 최솟값·최댓값을 출력하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage02
python examples\ex034_winsorize_outliers.py
```

## 4. 예상 결과
상하위 극단값만 경계값으로 제한되고 원본 컬럼은 보존됩니다.

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
| 18 | `for column in ["chamber_temp_c", "chamber_pressure_pa"]:` | 여러 컬럼이나 행에 같은 검사를 반복합니다. |
| 19 | `    lower = sensor_df[column].quantile(0.01)` | 분포의 분위수를 계산해 이상값 경계를 구합니다. |
| 20 | `    upper = sensor_df[column].quantile(0.99)` | 분포의 분위수를 계산해 이상값 경계를 구합니다. |
| 21 | `    new_column = f"{column}_winsorized"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 23 | `    sensor_df[new_column] = sensor_df[column].clip(lower=lower, upper=upper)` | 센서값이 허용 범위를 넘지 않도록 경계값으로 제한합니다. |
| 24 | `    changed_count = int((sensor_df[column] != sensor_df[new_column]).sum())` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 26 | `    print(column)` | 실행 결과를 콘솔에 출력합니다. |
| 27 | `    print("변경 행 수:", changed_count)` | 실행 결과를 콘솔에 출력합니다. |
| 28 | `    print(` | 실행 결과를 콘솔에 출력합니다. |
| 29 | `        "원본 범위:",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 30 | `        round(sensor_df[column].min(), 3),` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 31 | `        "~",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 32 | `        round(sensor_df[column].max(), 3),` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 33 | `    )` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 34 | `    print(` | 실행 결과를 콘솔에 출력합니다. |
| 35 | `        "보정 범위:",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 36 | `        round(sensor_df[new_column].min(), 3),` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 37 | `        "~",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 38 | `        round(sensor_df[new_column].max(), 3),` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 39 | `    )` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 40 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 41 | `sensor_df.to_csv(` | 처리 결과를 CSV 파일로 저장합니다. |
| 42 | `    OUTPUT_DIR / "ex034_winsorized_sensors.csv",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 43 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 44 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 45 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |

## 6. 실무 확장 질문
1. 이 검사 규칙의 기준값은 누가 승인해야 하는가?
2. 원본 데이터를 보존하면서 정제 이력을 남기려면 무엇이 필요한가?
3. 장비·챔버·레시피별로 기준값이 달라질 때 코드를 어떻게 바꿀 것인가?