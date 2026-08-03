# 실습 007 — group_by_lot

## 1. 학습 목표
LOT별 센서 평균과 변동성을 계산해 배치 간 차이를 확인합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
lot_id로 그룹화하여 온도, 압력, 입자 수의 평균과 표준편차를 계산하는
pandas groupby 예제를 작성하라. 다중 컬럼 이름은 읽기 쉬운 단일 이름으로 바꿔라.
```

## 3. 실행 방법
```bat
conda activate semi-physical-ai
python examples\ex007_group_by_lot.py
```

## 4. 예상 결과
LOT-A, LOT-B, LOT-C별 주요 센서 평균과 표준편차가 출력됩니다.

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
| 9 | `sensor_df = pd.read_csv(DATA_FILE)` | CSV 파일을 표 형태의 DataFrame으로 읽습니다. |
| 10 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 11 | `lot_summary = (` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 12 | `    sensor_df.groupby("lot_id")` | 실습 흐름에 필요한 명령을 수행합니다. |
| 13 | `    .agg(` | 실습 흐름에 필요한 명령을 수행합니다. |
| 14 | `        temp_mean=("chamber_temp_c", "mean"),` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 15 | `        temp_std=("chamber_temp_c", "std"),` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 16 | `        pressure_mean=("chamber_pressure_pa", "mean"),` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 17 | `        pressure_std=("chamber_pressure_pa", "std"),` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 18 | `        particle_mean=("particle_count", "mean"),` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 19 | `    )` | 실습 흐름에 필요한 명령을 수행합니다. |
| 20 | `    .reset_index()` | 실습 흐름에 필요한 명령을 수행합니다. |
| 21 | `)` | 실습 흐름에 필요한 명령을 수행합니다. |
| 22 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 23 | `print(lot_summary.round(3))` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |
| 24 | `lot_summary.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 25 | `    OUTPUT_DIR / "ex007_lot_summary.csv",` | 실습 흐름에 필요한 명령을 수행합니다. |
| 26 | `    index=False,` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 27 | `    encoding="utf-8-sig",` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 28 | `)` | 실습 흐름에 필요한 명령을 수행합니다. |

## 6. 확인 문제
1. 입력 데이터의 단위가 바뀌면 어느 부분을 수정해야 하는가?
2. 결측값 또는 이상값이 결과에 어떤 영향을 주는가?
3. 이 코드를 실제 반도체 장비 센서에 적용하려면 어떤 컬럼이 더 필요한가?