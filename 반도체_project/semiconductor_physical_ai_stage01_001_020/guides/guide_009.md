# 실습 009 — handle_missing_values

## 1. 학습 목표
결측값을 탐지하고 중앙값으로 보정하는 기본 절차를 익힙니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
원본 센서 데이터의 일부 압력값을 의도적으로 NaN으로 바꾸고 결측 개수를
확인한 뒤 중앙값으로 채우는 예제를 작성하라. 원본 CSV는 수정하지 말고 결과를
outputs/ex009_filled_missing.csv에 저장하라.
```

## 3. 실행 방법
```bat
conda activate semi-physical-ai
python examples\ex009_handle_missing_values.py
```

## 4. 예상 결과
보정 전 압력 결측값 5개가 확인되고, 중앙값 대체 후 0개가 됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 실습에 필요한 외부 기능을 불러옵니다. |
| 2 | `import pandas as pd` | 실습에 필요한 외부 기능을 불러옵니다. |
| 3 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 4 | `ROOT = Path(__file__).resolve().parents[1]` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 5 | `DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 6 | `OUTPUT_DIR = ROOT / "outputs"` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 7 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 8 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 9 | `import numpy as np` | 실습에 필요한 외부 기능을 불러옵니다. |
| 10 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 11 | `sensor_df = pd.read_csv(DATA_FILE)` | CSV 파일을 표 형태의 DataFrame으로 읽습니다. |
| 12 | `working_df = sensor_df.copy()` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 13 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 14 | `missing_rows = [10, 55, 120, 180, 250]` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 15 | `working_df.loc[missing_rows, "chamber_pressure_pa"] = np.nan` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 16 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 17 | `print("보정 전 결측 개수:")` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |
| 18 | `print(working_df.isna().sum())` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |
| 19 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 20 | `pressure_median = working_df["chamber_pressure_pa"].median()` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 21 | `working_df["chamber_pressure_pa"] = working_df[` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 22 | `    "chamber_pressure_pa"` | 실습 흐름에 필요한 명령을 수행합니다. |
| 23 | `].fillna(pressure_median)` | 실습 흐름에 필요한 명령을 수행합니다. |
| 24 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 25 | `print("\n보정 후 결측 개수:")` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |
| 26 | `print(working_df.isna().sum())` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |
| 27 | `working_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 28 | `    OUTPUT_DIR / "ex009_filled_missing.csv",` | 실습 흐름에 필요한 명령을 수행합니다. |
| 29 | `    index=False,` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 30 | `    encoding="utf-8-sig",` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 31 | `)` | 실습 흐름에 필요한 명령을 수행합니다. |

## 6. 확인 문제
1. 입력 데이터의 단위가 바뀌면 어느 부분을 수정해야 하는가?
2. 결측값 또는 이상값이 결과에 어떤 영향을 주는가?
3. 이 코드를 실제 반도체 장비 센서에 적용하려면 어떤 컬럼이 더 필요한가?