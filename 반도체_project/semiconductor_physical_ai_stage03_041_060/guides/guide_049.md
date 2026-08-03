# 실습 049 — subgroup_r_chart

## 1. 학습 목표
소그룹 범위로 R 관리도의 중심선과 관리한계를 계산합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
실습 048과 동일하게 5개씩 소그룹을 만들고 범위를 계산하라.
n=5의 D3=0, D4=2.114를 사용하여 R 관리도의 CL, UCL, LCL을 계산하고
관리한계 이탈 소그룹을 출력하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage03
python examples\ex049_subgroup_r_chart.py
```

## 4. 예상 결과
소그룹 범위의 중심선과 R 관리한계가 계산됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 기능을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 기능을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 기능을 불러옵니다. |
| 4 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 9 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError("data/semiconductor_sensor_data.csv 파일이 없습니다.")` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 12 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 13 | `sensor_df = pd.read_csv(DATA_FILE)` | CSV 센서 데이터를 DataFrame으로 읽습니다. |
| 14 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 15 | `subgroup_size = 5` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 16 | `sensor_df["subgroup_id"] = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 17 | `    np.arange(len(sensor_df)) // subgroup_size` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 18 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 19 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 20 | `range_df = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 21 | `    sensor_df.groupby("subgroup_id")["chamber_temp_c"]` | LOT 또는 소그룹 단위로 데이터를 묶습니다. |
| 22 | `    .agg(["min", "max"])` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 23 | `    .reset_index()` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 24 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 25 | `range_df["subgroup_range"] = range_df["max"] - range_df["min"]` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 26 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 27 | `r_bar = range_df["subgroup_range"].mean()` | 데이터의 평균을 계산합니다. |
| 28 | `d3 = 0.0` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 29 | `d4 = 2.114` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 30 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 31 | `range_df["cl"] = r_bar` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 32 | `range_df["ucl"] = d4 * r_bar` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 33 | `range_df["lcl"] = d3 * r_bar` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 34 | `range_df["out_of_control"] = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 35 | `    (range_df["subgroup_range"] > range_df["ucl"])` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 36 | `    \| (range_df["subgroup_range"] < range_df["lcl"])` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 37 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 38 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 39 | `print(f"Rbar={r_bar:.3f}")` | 실행 결과를 콘솔에 출력합니다. |
| 40 | `print(` | 실행 결과를 콘솔에 출력합니다. |
| 41 | `    "R 관리도 이탈 소그룹:",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 42 | `    int(range_df["out_of_control"].sum()),` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 43 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 44 | `print(range_df.loc[range_df["out_of_control"]])` | 실행 결과를 콘솔에 출력합니다. |
| 45 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 46 | `range_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 47 | `    OUTPUT_DIR / "ex049_r_chart_data.csv",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 48 | `    index=False,` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 49 | `    encoding="utf-8-sig",` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 50 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 관리한계와 규격한계는 어떻게 다른가?
2. 공정 조건이나 레시피가 바뀌면 기준선을 다시 계산해야 하는가?
3. 경보가 발생했을 때 자동 정지와 작업자 확인 중 어떤 절차가 필요한가?