# 실습 047 — moving_range_chart

## 1. 학습 목표
연속 두 관측값의 차이로 이동범위(MR)를 계산하고 MR 관리도를 작성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
온도 센서의 절대 1시점 차이를 moving_range로 계산하라.
MR 평균과 UCL=3.267*MR평균을 계산하고 MR 관리도를 PNG로 저장하라.
UCL을 넘는 시점 수를 출력하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage03
python examples\ex047_moving_range_chart.py
```

## 4. 예상 결과
온도 이동범위 관리도와 MR 관리한계 이탈 수가 생성됩니다.

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
| 19 | `sensor_df["moving_range"] = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 20 | `    sensor_df["chamber_temp_c"]` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 21 | `    .diff()` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 22 | `    .abs()` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 23 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 24 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 25 | `mr_mean = sensor_df["moving_range"].mean()` | 데이터의 평균을 계산합니다. |
| 26 | `mr_ucl = 3.267 * mr_mean` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 27 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 28 | `sensor_df["mr_out_of_control"] = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 29 | `    sensor_df["moving_range"] > mr_ucl` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 30 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 31 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 32 | `plt.figure(figsize=(12, 5))` | 관리도나 추세 그래프의 모양과 저장 방식을 설정합니다. |
| 33 | `plt.plot(` | 관리도나 추세 그래프의 모양과 저장 방식을 설정합니다. |
| 34 | `    sensor_df["timestamp"],` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 35 | `    sensor_df["moving_range"],` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 36 | `    label="Moving range",` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 37 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 38 | `plt.axhline(mr_mean, linestyle="-", label="MR mean")` | 관리도나 추세 그래프의 모양과 저장 방식을 설정합니다. |
| 39 | `plt.axhline(mr_ucl, linestyle="--", label="MR UCL")` | 관리도나 추세 그래프의 모양과 저장 방식을 설정합니다. |
| 40 | `plt.title("Temperature Moving Range Chart")` | 관리도나 추세 그래프의 모양과 저장 방식을 설정합니다. |
| 41 | `plt.xlabel("Time")` | 관리도나 추세 그래프의 모양과 저장 방식을 설정합니다. |
| 42 | `plt.ylabel("Moving range")` | 관리도나 추세 그래프의 모양과 저장 방식을 설정합니다. |
| 43 | `plt.grid(True)` | 관리도나 추세 그래프의 모양과 저장 방식을 설정합니다. |
| 44 | `plt.legend()` | 관리도나 추세 그래프의 모양과 저장 방식을 설정합니다. |
| 45 | `plt.tight_layout()` | 관리도나 추세 그래프의 모양과 저장 방식을 설정합니다. |
| 46 | `plt.savefig(` | 관리도나 추세 그래프의 모양과 저장 방식을 설정합니다. |
| 47 | `    OUTPUT_DIR / "ex047_temperature_mr_chart.png",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 48 | `    dpi=150,` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 49 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 50 | `plt.close()` | 관리도나 추세 그래프의 모양과 저장 방식을 설정합니다. |
| 51 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 52 | `print(f"MR 평균={mr_mean:.3f}, UCL={mr_ucl:.3f}")` | 실행 결과를 콘솔에 출력합니다. |
| 53 | `print(` | 실행 결과를 콘솔에 출력합니다. |
| 54 | `    "MR 관리한계 이탈 수:",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 55 | `    int(sensor_df["mr_out_of_control"].sum()),` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 56 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 관리한계와 규격한계는 어떻게 다른가?
2. 공정 조건이나 레시피가 바뀌면 기준선을 다시 계산해야 하는가?
3. 경보가 발생했을 때 자동 정지와 작업자 확인 중 어떤 절차가 필요한가?