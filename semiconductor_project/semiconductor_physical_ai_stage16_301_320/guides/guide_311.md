# 실습 311 — multivariable_state_estimation

## 1. 학습 목표
온도·압력 상태를 함께 추정합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
온도와 압력을 2차원 상태벡터로 칼만 추정하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage16
python examples\ex311_multivariable_state_estimation.py
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
| 17 | `temp = sensor_df["temp_sensor_a_c"].interpolate(limit_direction="both")` | 시간 순서에 따라 결측값을 보간합니다. |
| 18 | `pressure = sensor_df["pressure_sensor_a_pa"].interpolate(limit_direction="both")` | 시간 순서에 따라 결측값을 보간합니다. |
| 19 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 20 | `state = np.array([temp.iloc[0], pressure.iloc[0]], dtype=float)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `state_covariance = np.eye(2)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `transition = np.eye(2)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `observation = np.eye(2)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `process_covariance = np.diag([0.02, 0.01])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `measurement_covariance = np.diag([0.45**2, 0.18**2])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 27 | `estimated_states = []` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 29 | `for temp_value, pressure_value in zip(temp, pressure):` | 센서 시점 또는 변수별 작업을 반복합니다. |
| 30 | `    state = transition @ state` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `    state_covariance = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `        transition @ state_covariance @ transition.T` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 33 | `        + process_covariance` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 34 | `    )` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 35 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 36 | `    measurement = np.array([temp_value, pressure_value])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 37 | `    innovation = measurement - observation @ state` | 계산 결과나 설정값을 변수에 저장합니다. |
| 38 | `    innovation_covariance = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 39 | `        observation @ state_covariance @ observation.T` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 40 | `        + measurement_covariance` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 41 | `    )` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 42 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 43 | `    kalman_gain = (` | 칼만 필터 상태 추정 단계를 수행합니다. |
| 44 | `        state_covariance` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 45 | `        @ observation.T` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 46 | `        @ np.linalg.inv(innovation_covariance)` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 47 | `    )` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 48 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 49 | `    state = state + kalman_gain @ innovation` | 칼만 필터 상태 추정 단계를 수행합니다. |
| 50 | `    state_covariance = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 51 | `        np.eye(2) - kalman_gain @ observation` | 칼만 필터 상태 추정 단계를 수행합니다. |
| 52 | `    ) @ state_covariance` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 53 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 54 | `    estimated_states.append(state.copy())` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 55 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 56 | `estimated_states = np.vstack(estimated_states)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 57 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 58 | `sensor_df["estimated_temperature_c"] = estimated_states[:, 0]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 59 | `sensor_df["estimated_pressure_pa"] = estimated_states[:, 1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 60 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 61 | `print(` | 결과를 콘솔에 출력합니다. |
| 62 | `    sensor_df[` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 63 | `        ["estimated_temperature_c", "estimated_pressure_pa"]` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 64 | `    ].head()` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 65 | `)` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 센서 시간축과 샘플링 주기가 일치하는가?
2. 트윈 오차가 센서 문제인지 모델 문제인지 구분했는가?
3. 추정값을 제어에 사용할 때 안전한 폴백 조건이 있는가?