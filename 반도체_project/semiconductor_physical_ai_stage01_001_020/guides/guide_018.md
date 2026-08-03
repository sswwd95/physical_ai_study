# 실습 018 — plot_sensor_histogram

## 1. 학습 목표
히스토그램으로 센서값의 분포 모양을 확인합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
chamber_pressure_pa의 히스토그램을 25개 구간으로 작성하고 평균선을 표시하라.
제목, 축 이름, 범례를 넣고 PNG로 저장하라.
```

## 3. 실행 방법
```bat
conda activate semi-physical-ai
python examples\ex018_plot_sensor_histogram.py
```

## 4. 예상 결과
압력값의 빈도 분포와 평균선이 PNG 파일에 저장됩니다.

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
| 9 | `import matplotlib` | 실습에 필요한 외부 기능을 불러옵니다. |
| 10 | `matplotlib.use("Agg")` | 실습 흐름에 필요한 명령을 수행합니다. |
| 11 | `import matplotlib.pyplot as plt` | 실습에 필요한 외부 기능을 불러옵니다. |
| 12 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 13 | `sensor_df = pd.read_csv(DATA_FILE)` | CSV 파일을 표 형태의 DataFrame으로 읽습니다. |
| 14 | `pressure_mean = sensor_df["chamber_pressure_pa"].mean()` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 15 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 16 | `plt.figure(figsize=(8, 5))` | 그래프의 모양, 제목, 축 또는 저장 방식을 설정합니다. |
| 17 | `plt.hist(sensor_df["chamber_pressure_pa"], bins=25, alpha=0.8)` | 그래프의 모양, 제목, 축 또는 저장 방식을 설정합니다. |
| 18 | `plt.axvline(pressure_mean, linestyle="--", label=f"Mean={pressure_mean:.2f}")` | 그래프의 모양, 제목, 축 또는 저장 방식을 설정합니다. |
| 19 | `plt.title("Chamber Pressure Distribution")` | 그래프의 모양, 제목, 축 또는 저장 방식을 설정합니다. |
| 20 | `plt.xlabel("Pressure (Pa)")` | 그래프의 모양, 제목, 축 또는 저장 방식을 설정합니다. |
| 21 | `plt.ylabel("Frequency")` | 그래프의 모양, 제목, 축 또는 저장 방식을 설정합니다. |
| 22 | `plt.legend()` | 그래프의 모양, 제목, 축 또는 저장 방식을 설정합니다. |
| 23 | `plt.tight_layout()` | 그래프의 모양, 제목, 축 또는 저장 방식을 설정합니다. |
| 24 | `plt.savefig(OUTPUT_DIR / "ex018_pressure_histogram.png", dpi=150)` | 그래프의 모양, 제목, 축 또는 저장 방식을 설정합니다. |
| 25 | `plt.close()` | 그래프의 모양, 제목, 축 또는 저장 방식을 설정합니다. |
| 26 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 27 | `print(f"압력 평균: {pressure_mean:.3f} Pa")` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |

## 6. 확인 문제
1. 입력 데이터의 단위가 바뀌면 어느 부분을 수정해야 하는가?
2. 결측값 또는 이상값이 결과에 어떤 영향을 주는가?
3. 이 코드를 실제 반도체 장비 센서에 적용하려면 어떤 컬럼이 더 필요한가?