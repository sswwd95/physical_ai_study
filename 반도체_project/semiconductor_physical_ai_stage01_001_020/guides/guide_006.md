# 실습 006 — create_derived_feature

## 1. 학습 목표
센서 두 개를 조합해 간단한 공정 부하 지표를 만듭니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
RF 전력과 가스 유량을 이용해 process_load = rf_power_w / gas_flow_sccm
파생변수를 만들고 상위 10개 행을 출력하라. 0으로 나누는 문제를 방지하라.
```

## 3. 실행 방법
```bat
conda activate semi-physical-ai
python examples\ex006_create_derived_feature.py
```

## 4. 예상 결과
`process_load` 파생 컬럼이 생성되고 RF 전력 대비 가스 유량 비율을 확인할 수 있습니다.

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
| 12 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 13 | `safe_gas_flow = sensor_df["gas_flow_sccm"].replace(0, np.nan)` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 14 | `sensor_df["process_load"] = sensor_df["rf_power_w"] / safe_gas_flow` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 15 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 16 | `result_df = sensor_df[` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 17 | `    ["timestamp", "lot_id", "rf_power_w", "gas_flow_sccm", "process_load"]` | 실습 흐름에 필요한 명령을 수행합니다. |
| 18 | `]` | 실습 흐름에 필요한 명령을 수행합니다. |
| 19 | `print(result_df.head(10).round(3))` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |
| 20 | `result_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 21 | `    OUTPUT_DIR / "ex006_process_load.csv",` | 실습 흐름에 필요한 명령을 수행합니다. |
| 22 | `    index=False,` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 23 | `    encoding="utf-8-sig",` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 24 | `)` | 실습 흐름에 필요한 명령을 수행합니다. |

## 6. 확인 문제
1. 입력 데이터의 단위가 바뀌면 어느 부분을 수정해야 하는가?
2. 결측값 또는 이상값이 결과에 어떤 영향을 주는가?
3. 이 코드를 실제 반도체 장비 센서에 적용하려면 어떤 컬럼이 더 필요한가?