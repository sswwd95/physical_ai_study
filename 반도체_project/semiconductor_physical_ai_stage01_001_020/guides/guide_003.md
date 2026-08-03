# 실습 003 — select_sensor_columns

## 1. 학습 목표
필요한 센서 컬럼만 선택하고 컬럼 선택 문법을 익힙니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
pandas DataFrame에서 timestamp, chamber_temp_c, chamber_pressure_pa,
rf_power_w만 선택하여 출력하고 outputs/ex003_selected_columns.csv로 저장하는
초보자용 예제를 작성하라.
```

## 3. 실행 방법
```bat
conda activate semi-physical-ai
python examples\ex003_select_sensor_columns.py
```

## 4. 예상 결과
선택된 4개 컬럼의 처음 10행이 출력되고 별도 CSV로 저장됩니다.

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
| 9 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | CSV 파일을 표 형태의 DataFrame으로 읽습니다. |
| 10 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 11 | `selected_columns = [` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 12 | `    "timestamp",` | 실습 흐름에 필요한 명령을 수행합니다. |
| 13 | `    "chamber_temp_c",` | 실습 흐름에 필요한 명령을 수행합니다. |
| 14 | `    "chamber_pressure_pa",` | 실습 흐름에 필요한 명령을 수행합니다. |
| 15 | `    "rf_power_w",` | 실습 흐름에 필요한 명령을 수행합니다. |
| 16 | `]` | 실습 흐름에 필요한 명령을 수행합니다. |
| 17 | `selected_df = sensor_df[selected_columns]` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 18 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 19 | `print(selected_df.head(10))` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |
| 20 | `selected_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 21 | `    OUTPUT_DIR / "ex003_selected_columns.csv",` | 실습 흐름에 필요한 명령을 수행합니다. |
| 22 | `    index=False,` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 23 | `    encoding="utf-8-sig",` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 24 | `)` | 실습 흐름에 필요한 명령을 수행합니다. |

## 6. 확인 문제
1. 입력 데이터의 단위가 바뀌면 어느 부분을 수정해야 하는가?
2. 결측값 또는 이상값이 결과에 어떤 영향을 주는가?
3. 이 코드를 실제 반도체 장비 센서에 적용하려면 어떤 컬럼이 더 필요한가?