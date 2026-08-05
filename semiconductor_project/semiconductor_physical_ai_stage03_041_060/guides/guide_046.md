# 실습 046 — individuals_control_chart

## 1. 학습 목표
개별값 관리도(I Chart)를 생성하고 관리한계 이탈점을 표시합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
챔버 온도의 평균과 표준편차로 I 관리도를 작성하라.
원본값, 중심선, UCL, LCL을 표시하고 관리한계 이탈점을 별도 마커로 표시한 뒤
PNG로 저장하라. 화면 없이 저장 가능하게 작성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage03
python examples\ex046_individuals_control_chart.py
```

## 4. 예상 결과
`outputs/ex046_temperature_i_chart.png`에 온도 I 관리도가 저장됩니다.

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
| 13 | `import matplotlib` | 필요한 라이브러리나 기능을 불러옵니다. |
| 14 | `matplotlib.use("Agg")` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 15 | `import matplotlib.pyplot as plt` | 필요한 라이브러리나 기능을 불러옵니다. |
| 16 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 17 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | CSV 센서 데이터를 DataFrame으로 읽습니다. |
| 18 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 19 | `mean_value = sensor_df["chamber_temp_c"].mean()` | 데이터의 평균을 계산합니다. |
| 20 | `std_value = sensor_df["chamber_temp_c"].std(ddof=1)` | 데이터의 표준편차를 계산합니다. |
| 21 | `ucl = mean_value + 3 * std_value` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 22 | `lcl = mean_value - 3 * std_value` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 23 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 24 | `outlier_mask = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 25 | `    (sensor_df["chamber_temp_c"] > ucl)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 26 | `    \| (sensor_df["chamber_temp_c"] < lcl)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 27 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 28 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 29 | `plt.figure(figsize=(12, 5))` | 관리도나 추세 그래프의 모양과 저장 방식을 설정합니다. |
| 30 | `plt.plot(` | 관리도나 추세 그래프의 모양과 저장 방식을 설정합니다. |
| 31 | `    sensor_df["timestamp"],` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 32 | `    sensor_df["chamber_temp_c"],` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 33 | `    label="Temperature",` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 34 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 35 | `plt.axhline(mean_value, linestyle="-", label="CL")` | 관리도나 추세 그래프의 모양과 저장 방식을 설정합니다. |
| 36 | `plt.axhline(ucl, linestyle="--", label="UCL")` | 관리도나 추세 그래프의 모양과 저장 방식을 설정합니다. |
| 37 | `plt.axhline(lcl, linestyle="--", label="LCL")` | 관리도나 추세 그래프의 모양과 저장 방식을 설정합니다. |
| 38 | `plt.scatter(` | 관리도나 추세 그래프의 모양과 저장 방식을 설정합니다. |
| 39 | `    sensor_df.loc[outlier_mask, "timestamp"],` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 40 | `    sensor_df.loc[outlier_mask, "chamber_temp_c"],` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 41 | `    label="Out of control",` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 42 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 43 | `plt.title("Temperature Individuals Control Chart")` | 관리도나 추세 그래프의 모양과 저장 방식을 설정합니다. |
| 44 | `plt.xlabel("Time")` | 관리도나 추세 그래프의 모양과 저장 방식을 설정합니다. |
| 45 | `plt.ylabel("Temperature (C)")` | 관리도나 추세 그래프의 모양과 저장 방식을 설정합니다. |
| 46 | `plt.grid(True)` | 관리도나 추세 그래프의 모양과 저장 방식을 설정합니다. |
| 47 | `plt.legend()` | 관리도나 추세 그래프의 모양과 저장 방식을 설정합니다. |
| 48 | `plt.tight_layout()` | 관리도나 추세 그래프의 모양과 저장 방식을 설정합니다. |
| 49 | `plt.savefig(` | 관리도나 추세 그래프의 모양과 저장 방식을 설정합니다. |
| 50 | `    OUTPUT_DIR / "ex046_temperature_i_chart.png",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 51 | `    dpi=150,` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 52 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 53 | `plt.close()` | 관리도나 추세 그래프의 모양과 저장 방식을 설정합니다. |
| 54 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 55 | `print("I 관리도 저장 완료")` | 실행 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 관리한계와 규격한계는 어떻게 다른가?
2. 공정 조건이나 레시피가 바뀌면 기준선을 다시 계산해야 하는가?
3. 경보가 발생했을 때 자동 정지와 작업자 확인 중 어떤 절차가 필요한가?