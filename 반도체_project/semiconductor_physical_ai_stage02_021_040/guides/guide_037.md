# 실습 037 — cross_sensor_rule_check

## 1. 학습 목표
센서 간 물리·공정 논리를 이용한 교차 검증 규칙을 구현합니다.

## 2. Antigravity용 하네스 프롬프트
```text
process_state가 process인데 RF 전력이 800W 미만이거나 가스 유량이 110sccm 미만이면
cross_sensor_violation으로 표시하라. 또한 purge 상태에서 RF 전력이 900W를 넘으면
위반으로 표시하라. 규칙별 위반 건수와 문제 행을 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage02
python examples\ex037_cross_sensor_rule_check.py
```

## 4. 예상 결과
공정 상태와 센서값 사이의 논리 위반이 규칙별로 집계됩니다.

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
| 16 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | CSV 센서 데이터를 DataFrame으로 읽습니다. |
| 17 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 18 | `rule_process_low_rf = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `    (sensor_df["process_state"] == "process")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `    & (sensor_df["rf_power_w"] < 800.0)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 21 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 22 | `rule_process_low_gas = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `    (sensor_df["process_state"] == "process")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `    & (sensor_df["gas_flow_sccm"] < 110.0)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 25 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 26 | `rule_purge_high_rf = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `    (sensor_df["process_state"] == "purge")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `    & (sensor_df["rf_power_w"] > 900.0)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 29 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 30 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 31 | `sensor_df["cross_sensor_violation"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `    rule_process_low_rf` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 33 | `    \| rule_process_low_gas` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 34 | `    \| rule_purge_high_rf` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 35 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 36 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 37 | `print("process 저전력:", int(rule_process_low_rf.sum()))` | 실행 결과를 콘솔에 출력합니다. |
| 38 | `print("process 저유량:", int(rule_process_low_gas.sum()))` | 실행 결과를 콘솔에 출력합니다. |
| 39 | `print("purge 고전력:", int(rule_purge_high_rf.sum()))` | 실행 결과를 콘솔에 출력합니다. |
| 40 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 41 | `problem_df = sensor_df.loc[sensor_df["cross_sensor_violation"]]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `problem_df.to_csv(` | 처리 결과를 CSV 파일로 저장합니다. |
| 43 | `    OUTPUT_DIR / "ex037_cross_sensor_violations.csv",` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |
| 44 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 45 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 46 | `)` | 데이터 전처리 또는 품질검사 단계를 수행합니다. |

## 6. 실무 확장 질문
1. 이 검사 규칙의 기준값은 누가 승인해야 하는가?
2. 원본 데이터를 보존하면서 정제 이력을 남기려면 무엇이 필요한가?
3. 장비·챔버·레시피별로 기준값이 달라질 때 코드를 어떻게 바꿀 것인가?