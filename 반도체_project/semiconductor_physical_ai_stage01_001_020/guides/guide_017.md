# 실습 017 — plot_temperature_trend

## 1. 학습 목표
Matplotlib으로 시간에 따른 온도 추세를 시각화하고 파일로 저장합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
timestamp와 chamber_temp_c를 이용해 12x5 크기의 선 그래프를 작성하라.
75도 기준선을 표시하고 제목, 축 이름, 범례, 격자를 추가한 뒤 PNG로 저장하라.
화면 표시 없이 저장 가능하게 작성하라.
```

## 3. 실행 방법
```bat
conda activate semi-physical-ai
python examples\ex017_plot_temperature_trend.py
```

## 4. 예상 결과
`outputs/ex017_temperature_trend.png`에 온도 추세와 75°C 기준선이 저장됩니다.

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
| 13 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | CSV 파일을 표 형태의 DataFrame으로 읽습니다. |
| 14 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 15 | `plt.figure(figsize=(12, 5))` | 그래프의 모양, 제목, 축 또는 저장 방식을 설정합니다. |
| 16 | `plt.plot(` | 그래프의 모양, 제목, 축 또는 저장 방식을 설정합니다. |
| 17 | `    sensor_df["timestamp"],` | 실습 흐름에 필요한 명령을 수행합니다. |
| 18 | `    sensor_df["chamber_temp_c"],` | 실습 흐름에 필요한 명령을 수행합니다. |
| 19 | `    label="Chamber temperature",` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 20 | `)` | 실습 흐름에 필요한 명령을 수행합니다. |
| 21 | `plt.axhline(75.0, linestyle="--", label="75 C threshold")` | 그래프의 모양, 제목, 축 또는 저장 방식을 설정합니다. |
| 22 | `plt.title("Semiconductor Chamber Temperature Trend")` | 그래프의 모양, 제목, 축 또는 저장 방식을 설정합니다. |
| 23 | `plt.xlabel("Time")` | 그래프의 모양, 제목, 축 또는 저장 방식을 설정합니다. |
| 24 | `plt.ylabel("Temperature (C)")` | 그래프의 모양, 제목, 축 또는 저장 방식을 설정합니다. |
| 25 | `plt.grid(True)` | 그래프의 모양, 제목, 축 또는 저장 방식을 설정합니다. |
| 26 | `plt.legend()` | 그래프의 모양, 제목, 축 또는 저장 방식을 설정합니다. |
| 27 | `plt.tight_layout()` | 그래프의 모양, 제목, 축 또는 저장 방식을 설정합니다. |
| 28 | `plt.savefig(OUTPUT_DIR / "ex017_temperature_trend.png", dpi=150)` | 그래프의 모양, 제목, 축 또는 저장 방식을 설정합니다. |
| 29 | `plt.close()` | 그래프의 모양, 제목, 축 또는 저장 방식을 설정합니다. |
| 30 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 31 | `print("그래프 저장 완료")` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |

## 6. 확인 문제
1. 입력 데이터의 단위가 바뀌면 어느 부분을 수정해야 하는가?
2. 결측값 또는 이상값이 결과에 어떤 영향을 주는가?
3. 이 코드를 실제 반도체 장비 센서에 적용하려면 어떤 컬럼이 더 필요한가?