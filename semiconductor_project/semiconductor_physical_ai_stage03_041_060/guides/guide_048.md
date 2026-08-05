# 실습 048 — subgroup_xbar_chart

## 1. 학습 목표
5개 관측값을 한 소그룹으로 묶어 X-bar 관리도의 기초를 실습합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
온도 데이터를 연속 5개씩 소그룹으로 묶고 subgroup_mean과 subgroup_range를 계산하라.
전체 소그룹 평균과 평균 범위를 사용하여 X-bar 관리한계를
UCL=Xdoublebar+0.577*Rbar, LCL=Xdoublebar-0.577*Rbar로 계산하라.
결과를 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage03
python examples\ex048_subgroup_xbar_chart.py
```

## 4. 예상 결과
60개 소그룹의 평균, 범위, X-bar 관리한계와 이탈 여부가 저장됩니다.

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
| 20 | `subgroup_df = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 21 | `    sensor_df.groupby("subgroup_id")` | LOT 또는 소그룹 단위로 데이터를 묶습니다. |
| 22 | `    .agg(` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 23 | `        subgroup_mean=("chamber_temp_c", "mean"),` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 24 | `        subgroup_min=("chamber_temp_c", "min"),` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 25 | `        subgroup_max=("chamber_temp_c", "max"),` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 26 | `    )` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 27 | `    .reset_index()` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 28 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 29 | `subgroup_df["subgroup_range"] = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 30 | `    subgroup_df["subgroup_max"]` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 31 | `    - subgroup_df["subgroup_min"]` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 32 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 33 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 34 | `x_double_bar = subgroup_df["subgroup_mean"].mean()` | 데이터의 평균을 계산합니다. |
| 35 | `r_bar = subgroup_df["subgroup_range"].mean()` | 데이터의 평균을 계산합니다. |
| 36 | `a2 = 0.577` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 37 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 38 | `subgroup_df["cl"] = x_double_bar` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 39 | `subgroup_df["ucl"] = x_double_bar + a2 * r_bar` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 40 | `subgroup_df["lcl"] = x_double_bar - a2 * r_bar` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 41 | `subgroup_df["out_of_control"] = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 42 | `    (subgroup_df["subgroup_mean"] > subgroup_df["ucl"])` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 43 | `    \| (subgroup_df["subgroup_mean"] < subgroup_df["lcl"])` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 44 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 45 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 46 | `print(subgroup_df.head(10).round(3))` | 실행 결과를 콘솔에 출력합니다. |
| 47 | `print(` | 실행 결과를 콘솔에 출력합니다. |
| 48 | `    "X-bar 이탈 소그룹:",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 49 | `    int(subgroup_df["out_of_control"].sum()),` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 50 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 51 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 52 | `subgroup_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 53 | `    OUTPUT_DIR / "ex048_xbar_chart_data.csv",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 54 | `    index=False,` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 55 | `    encoding="utf-8-sig",` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 56 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 관리한계와 규격한계는 어떻게 다른가?
2. 공정 조건이나 레시피가 바뀌면 기준선을 다시 계산해야 하는가?
3. 경보가 발생했을 때 자동 정지와 작업자 확인 중 어떤 절차가 필요한가?