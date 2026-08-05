# 실습 305 — weighted_sensor_fusion

## 1. 학습 목표
센서 분산 기반 가중평균 융합을 수행합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
센서 오차분산의 역수를 가중치로 온도 센서를 융합하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage16
python examples\ex305_weighted_sensor_fusion.py
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
| 17 | `temp_a = sensor_df["temp_sensor_a_c"].interpolate(limit_direction="both")` | 시간 순서에 따라 결측값을 보간합니다. |
| 18 | `temp_b = sensor_df["temp_sensor_b_c"].interpolate(limit_direction="both")` | 시간 순서에 따라 결측값을 보간합니다. |
| 19 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 20 | `var_a = np.nanvar(temp_a - sensor_df["true_temperature_c"])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `var_b = np.nanvar(temp_b - sensor_df["true_temperature_c"])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 23 | `weight_a = 1 / var_a` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `weight_b = 1 / var_b` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `weight_sum = weight_a + weight_b` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 27 | `sensor_df["fused_temperature_c"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `    weight_a * temp_a + weight_b * temp_b` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 29 | `) / weight_sum` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 30 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 31 | `rmse = np.sqrt(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `    np.mean(` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 33 | `        (` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 34 | `            sensor_df["fused_temperature_c"]` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 35 | `            - sensor_df["true_temperature_c"]` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 36 | `        ) ** 2` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 37 | `    )` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 38 | `)` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 39 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 40 | `print("센서 A 가중치:", round(weight_a / weight_sum, 4))` | 결과를 콘솔에 출력합니다. |
| 41 | `print("센서 B 가중치:", round(weight_b / weight_sum, 4))` | 결과를 콘솔에 출력합니다. |
| 42 | `print("융합 RMSE:", round(rmse, 4))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 센서 시간축과 샘플링 주기가 일치하는가?
2. 트윈 오차가 센서 문제인지 모델 문제인지 구분했는가?
3. 추정값을 제어에 사용할 때 안전한 폴백 조건이 있는가?