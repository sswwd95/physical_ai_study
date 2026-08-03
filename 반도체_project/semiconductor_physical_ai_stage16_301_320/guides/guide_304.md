# 실습 304 — sensor_bias_estimation

## 1. 학습 목표
두 센서 간 바이어스를 추정합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
온도·압력 이중 센서 간 평균 바이어스와 표준편차를 계산하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage16
python examples\ex304_sensor_bias_estimation.py
```

## 4. 예상 결과
요청한 디지털 트윈·센서 융합 결과가 출력 또는 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리를 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리를 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리를 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "digital_twin_sensor_stream.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError(` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 12 | `        "data/digital_twin_sensor_stream.csv 파일이 없습니다."` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 13 | `    )` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 14 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 15 | `sensor_df = pd.read_csv(DATA_FILE)` | 디지털 트윈 센서 스트림 CSV를 읽습니다. |
| 16 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 17 | `temp_bias = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 18 | `    sensor_df["temp_sensor_b_c"] - sensor_df["temp_sensor_a_c"]` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 19 | `)` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 20 | `pressure_bias = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `    sensor_df["pressure_sensor_b_pa"]` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 22 | `    - sensor_df["pressure_sensor_a_pa"]` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 23 | `)` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 24 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 25 | `result_df = pd.DataFrame([` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `    {` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 27 | `        "sensor_pair": "temperature_b_minus_a",` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 28 | `        "mean_bias": temp_bias.mean(),` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 29 | `        "std_bias": temp_bias.std(),` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 30 | `    },` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 31 | `    {` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 32 | `        "sensor_pair": "pressure_b_minus_a",` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 33 | `        "mean_bias": pressure_bias.mean(),` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 34 | `        "std_bias": pressure_bias.std(),` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 35 | `    },` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 36 | `])` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 37 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 38 | `print(result_df.round(4))` | 결과를 콘솔에 출력합니다. |
| 39 | `result_df.to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 40 | `    OUTPUT_DIR / "ex304_sensor_bias.csv",` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 41 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 43 | `)` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 센서 시간축과 샘플링 주기가 일치하는가?
2. 트윈 오차가 센서 문제인지 모델 문제인지 구분했는가?
3. 추정값을 제어에 사용할 때 안전한 폴백 조건이 있는가?