# 실습 309 — scalar_kalman_temperature

## 1. 학습 목표
1차원 칼만 필터로 온도를 추정합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
1차원 칼만 필터로 온도 상태를 추정하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage16
python examples\ex309_scalar_kalman_temperature.py
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
| 17 | `measurement = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 18 | `    sensor_df["temp_sensor_a_c"]` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 19 | `    .interpolate(limit_direction="both")` | 시간 순서에 따라 결측값을 보간합니다. |
| 20 | `    .to_numpy()` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 21 | `)` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 22 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 23 | `process_variance = 0.02` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `measurement_variance = 0.45 ** 2` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 26 | `estimate = measurement[0]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `estimate_variance = 1.0` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `filtered = []` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 30 | `for value in measurement:` | 센서 시점 또는 변수별 작업을 반복합니다. |
| 31 | `    estimate_variance = estimate_variance + process_variance` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 33 | `    kalman_gain = (` | 칼만 필터 상태 추정 단계를 수행합니다. |
| 34 | `        estimate_variance` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 35 | `        / (estimate_variance + measurement_variance)` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 36 | `    )` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 37 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 38 | `    estimate = estimate + kalman_gain * (value - estimate)` | 칼만 필터 상태 추정 단계를 수행합니다. |
| 39 | `    estimate_variance = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 40 | `        1 - kalman_gain` | 칼만 필터 상태 추정 단계를 수행합니다. |
| 41 | `    ) * estimate_variance` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 42 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 43 | `    filtered.append(estimate)` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 44 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 45 | `sensor_df["kalman_temperature_c"] = filtered` | 칼만 필터 상태 추정 단계를 수행합니다. |
| 46 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 47 | `rmse = np.sqrt(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 48 | `    np.mean(` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 49 | `        (` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 50 | `            sensor_df["kalman_temperature_c"]` | 칼만 필터 상태 추정 단계를 수행합니다. |
| 51 | `            - sensor_df["true_temperature_c"]` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 52 | `        ) ** 2` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 53 | `    )` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 54 | `)` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 55 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 56 | `print("Kalman 온도 RMSE:", round(rmse, 4))` | 칼만 필터 상태 추정 단계를 수행합니다. |
| 57 | `sensor_df[` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 58 | `    ["timestamp", "true_temperature_c", "kalman_temperature_c"]` | 칼만 필터 상태 추정 단계를 수행합니다. |
| 59 | `].to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 60 | `    OUTPUT_DIR / "ex309_kalman_temperature.csv",` | 칼만 필터 상태 추정 단계를 수행합니다. |
| 61 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 62 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 63 | `)` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 센서 시간축과 샘플링 주기가 일치하는가?
2. 트윈 오차가 센서 문제인지 모델 문제인지 구분했는가?
3. 추정값을 제어에 사용할 때 안전한 폴백 조건이 있는가?