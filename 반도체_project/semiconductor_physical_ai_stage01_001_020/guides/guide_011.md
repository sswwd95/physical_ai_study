# 실습 011 — sort_by_particle_count

## 1. 학습 목표
입자 수가 높은 순서로 정렬하여 오염 위험 시점을 찾습니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
particle_count를 내림차순 정렬하여 상위 15개 시점의 timestamp, lot_id,
particle_count, chamber_temp_c를 출력하고 CSV로 저장하라.
```

## 3. 실행 방법
```bat
conda activate semi-physical-ai
python examples\ex011_sort_by_particle_count.py
```

## 4. 예상 결과
입자 수가 가장 높은 15개 시점이 큰 값부터 출력됩니다.

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
| 11 | `top_particle_df = (` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 12 | `    sensor_df[` | 실습 흐름에 필요한 명령을 수행합니다. |
| 13 | `        ["timestamp", "lot_id", "particle_count", "chamber_temp_c"]` | 실습 흐름에 필요한 명령을 수행합니다. |
| 14 | `    ]` | 실습 흐름에 필요한 명령을 수행합니다. |
| 15 | `    .sort_values("particle_count", ascending=False)` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 16 | `    .head(15)` | 실습 흐름에 필요한 명령을 수행합니다. |
| 17 | `)` | 실습 흐름에 필요한 명령을 수행합니다. |
| 18 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 19 | `print(top_particle_df)` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |
| 20 | `top_particle_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 21 | `    OUTPUT_DIR / "ex011_top_particle_count.csv",` | 실습 흐름에 필요한 명령을 수행합니다. |
| 22 | `    index=False,` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 23 | `    encoding="utf-8-sig",` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 24 | `)` | 실습 흐름에 필요한 명령을 수행합니다. |

## 6. 확인 문제
1. 입력 데이터의 단위가 바뀌면 어느 부분을 수정해야 하는가?
2. 결측값 또는 이상값이 결과에 어떤 영향을 주는가?
3. 이 코드를 실제 반도체 장비 센서에 적용하려면 어떤 컬럼이 더 필요한가?