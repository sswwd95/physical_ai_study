# 실습 008 — group_by_process_state

## 1. 학습 목표
공정 상태별 센서 특성을 비교합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
process_state별 chamber_temp_c, chamber_pressure_pa, vibration_g의
평균을 계산하고 가장 진동이 큰 상태를 찾는 pandas 예제를 작성하라.
```

## 3. 실행 방법
```bat
conda activate semi-physical-ai
python examples\ex008_group_by_process_state.py
```

## 4. 예상 결과
상태별 평균 표와 진동 평균이 가장 큰 공정 상태가 출력됩니다.

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
| 11 | `state_summary = (` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 12 | `    sensor_df.groupby("process_state")[` | 실습 흐름에 필요한 명령을 수행합니다. |
| 13 | `        ["chamber_temp_c", "chamber_pressure_pa", "vibration_g"]` | 실습 흐름에 필요한 명령을 수행합니다. |
| 14 | `    ]` | 실습 흐름에 필요한 명령을 수행합니다. |
| 15 | `    .mean()` | 실습 흐름에 필요한 명령을 수행합니다. |
| 16 | `    .sort_values("vibration_g", ascending=False)` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 17 | `)` | 실습 흐름에 필요한 명령을 수행합니다. |
| 18 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 19 | `print(state_summary.round(4))` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |
| 20 | `print("\n진동 평균이 가장 큰 상태:", state_summary.index[0])` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |

## 6. 확인 문제
1. 입력 데이터의 단위가 바뀌면 어느 부분을 수정해야 하는가?
2. 결측값 또는 이상값이 결과에 어떤 영향을 주는가?
3. 이 코드를 실제 반도체 장비 센서에 적용하려면 어떤 컬럼이 더 필요한가?