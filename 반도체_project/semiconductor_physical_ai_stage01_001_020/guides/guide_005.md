# 실습 005 — filter_temperature

## 1. 학습 목표
조건식으로 고온 구간을 찾고 Boolean 필터링을 익힙니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
chamber_temp_c가 75도 이상인 행만 필터링하고 시점, LOT, 온도, 압력을
출력하는 초보자용 pandas 예제를 작성하라. 필터링된 행 개수도 출력하라.
```

## 3. 실행 방법
```bat
conda activate semi-physical-ai
python examples\ex005_filter_temperature.py
```

## 4. 예상 결과
이상 구간을 중심으로 75°C 이상인 행과 총 개수가 출력됩니다.

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
| 11 | `high_temp_mask = sensor_df["chamber_temp_c"] >= 75.0` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 12 | `high_temp_df = sensor_df.loc[` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 13 | `    high_temp_mask,` | 실습 흐름에 필요한 명령을 수행합니다. |
| 14 | `    ["timestamp", "lot_id", "chamber_temp_c", "chamber_pressure_pa"],` | 실습 흐름에 필요한 명령을 수행합니다. |
| 15 | `]` | 실습 흐름에 필요한 명령을 수행합니다. |
| 16 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 17 | `print(f"고온 행 개수: {len(high_temp_df)}")` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |
| 18 | `print(high_temp_df.head(20))` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |
| 19 | `high_temp_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 20 | `    OUTPUT_DIR / "ex005_high_temperature.csv",` | 실습 흐름에 필요한 명령을 수행합니다. |
| 21 | `    index=False,` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 22 | `    encoding="utf-8-sig",` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 23 | `)` | 실습 흐름에 필요한 명령을 수행합니다. |

## 6. 확인 문제
1. 입력 데이터의 단위가 바뀌면 어느 부분을 수정해야 하는가?
2. 결측값 또는 이상값이 결과에 어떤 영향을 주는가?
3. 이 코드를 실제 반도체 장비 센서에 적용하려면 어떤 컬럼이 더 필요한가?