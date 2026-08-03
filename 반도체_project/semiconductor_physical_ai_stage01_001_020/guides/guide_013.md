# 실습 013 — rolling_average

## 1. 학습 목표
이동평균으로 순간 잡음을 줄이고 추세를 확인합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
온도 센서에 10개 시점 이동평균 컬럼 temp_ma10을 추가하라.
원본 온도와 이동평균의 마지막 20행을 출력하고 CSV로 저장하라.
```

## 3. 실행 방법
```bat
conda activate semi-physical-ai
python examples\ex013_rolling_average.py
```

## 4. 예상 결과
원본 온도보다 부드럽게 변화하는 10시점 이동평균이 계산됩니다.

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
| 11 | `sensor_df["temp_ma10"] = (` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 12 | `    sensor_df["chamber_temp_c"]` | 실습 흐름에 필요한 명령을 수행합니다. |
| 13 | `    .rolling(window=10, min_periods=1)` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 14 | `    .mean()` | 실습 흐름에 필요한 명령을 수행합니다. |
| 15 | `)` | 실습 흐름에 필요한 명령을 수행합니다. |
| 16 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 17 | `result_df = sensor_df[["timestamp", "chamber_temp_c", "temp_ma10"]]` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 18 | `print(result_df.tail(20).round(3))` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |
| 19 | `result_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 20 | `    OUTPUT_DIR / "ex013_temperature_moving_average.csv",` | 실습 흐름에 필요한 명령을 수행합니다. |
| 21 | `    index=False,` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 22 | `    encoding="utf-8-sig",` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 23 | `)` | 실습 흐름에 필요한 명령을 수행합니다. |

## 6. 확인 문제
1. 입력 데이터의 단위가 바뀌면 어느 부분을 수정해야 하는가?
2. 결측값 또는 이상값이 결과에 어떤 영향을 주는가?
3. 이 코드를 실제 반도체 장비 센서에 적용하려면 어떤 컬럼이 더 필요한가?