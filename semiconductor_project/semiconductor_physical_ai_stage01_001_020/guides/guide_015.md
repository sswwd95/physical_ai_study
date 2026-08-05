# 실습 015 — zscore_temperature

## 1. 학습 목표
Z-score를 계산해 평균에서 멀리 떨어진 온도값을 탐지합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
scipy.stats.zscore를 사용해 chamber_temp_c의 z-score를 계산하고 절댓값이
3 이상인 행을 이상 후보로 출력하라. z-score 컬럼을 포함하라.
```

## 3. 실행 방법
```bat
conda activate semi-physical-ai
python examples\ex015_zscore_temperature.py
```

## 4. 예상 결과
평균에서 3표준편차 이상 떨어진 고온 구간 일부가 이상 후보로 출력됩니다.

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
| 9 | `from scipy.stats import zscore` | 실습에 필요한 외부 기능을 불러옵니다. |
| 10 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 11 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | CSV 파일을 표 형태의 DataFrame으로 읽습니다. |
| 12 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 13 | `sensor_df["temp_zscore"] = zscore(sensor_df["chamber_temp_c"])` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 14 | `outlier_df = sensor_df.loc[` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 15 | `    sensor_df["temp_zscore"].abs() >= 3.0,` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 16 | `    ["timestamp", "lot_id", "chamber_temp_c", "temp_zscore"],` | 실습 흐름에 필요한 명령을 수행합니다. |
| 17 | `]` | 실습 흐름에 필요한 명령을 수행합니다. |
| 18 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 19 | `print("온도 이상 후보 수:", len(outlier_df))` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |
| 20 | `print(outlier_df.round(3))` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |

## 6. 확인 문제
1. 입력 데이터의 단위가 바뀌면 어느 부분을 수정해야 하는가?
2. 결측값 또는 이상값이 결과에 어떤 영향을 주는가?
3. 이 코드를 실제 반도체 장비 센서에 적용하려면 어떤 컬럼이 더 필요한가?