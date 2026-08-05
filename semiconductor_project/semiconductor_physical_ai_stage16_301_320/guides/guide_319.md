# 실습 319 — realtime_twin_output

## 1. 학습 목표
실시간 전달용 상태 추정 CSV를 생성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
융합 센서값·잔차·경보가 포함된 실시간 전달 CSV를 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage16
python examples\ex319_realtime_twin_output.py
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
| 15 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | 디지털 트윈 센서 스트림 CSV를 읽습니다. |
| 16 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 17 | `temp_a = sensor_df["temp_sensor_a_c"].interpolate(limit_direction="both")` | 시간 순서에 따라 결측값을 보간합니다. |
| 18 | `temp_b = sensor_df["temp_sensor_b_c"].interpolate(limit_direction="both")` | 시간 순서에 따라 결측값을 보간합니다. |
| 19 | `pressure_a = sensor_df["pressure_sensor_a_pa"].interpolate(limit_direction="both")` | 시간 순서에 따라 결측값을 보간합니다. |
| 20 | `pressure_b = sensor_df["pressure_sensor_b_pa"].interpolate(limit_direction="both")` | 시간 순서에 따라 결측값을 보간합니다. |
| 21 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 22 | `sensor_df["fused_temperature_c"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `    0.7 * temp_a + 0.3 * temp_b` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 24 | `)` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 25 | `sensor_df["fused_pressure_pa"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `    0.75 * pressure_a + 0.25 * pressure_b` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 27 | `)` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 28 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 29 | `sensor_df["temperature_error"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `    sensor_df["fused_temperature_c"]` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 31 | `    - sensor_df["true_temperature_c"]` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 32 | `)` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 33 | `sensor_df["pressure_error"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 34 | `    sensor_df["fused_pressure_pa"]` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 35 | `    - sensor_df["true_pressure_pa"]` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 36 | `)` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 37 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 38 | `sensor_df["alarm"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 39 | `    sensor_df["temperature_error"].abs() > 2.0` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 40 | `) \| (` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 41 | `    sensor_df["pressure_error"].abs() > 0.8` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 42 | `)` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 43 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 44 | `output_columns = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 45 | `    "timestamp",` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 46 | `    "process_phase",` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 47 | `    "fused_temperature_c",` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 48 | `    "fused_pressure_pa",` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 49 | `    "rf_sensor_w",` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 50 | `    "gas_sensor_sccm",` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 51 | `    "temperature_error",` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 52 | `    "pressure_error",` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 53 | `    "alarm",` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 54 | `]` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 55 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 56 | `sensor_df[output_columns].to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 57 | `    OUTPUT_DIR / "ex319_realtime_twin_output.csv",` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 58 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 59 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 60 | `)` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 61 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 62 | `print(sensor_df[output_columns].head(10).round(4))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 센서 시간축과 샘플링 주기가 일치하는가?
2. 트윈 오차가 센서 문제인지 모델 문제인지 구분했는가?
3. 추정값을 제어에 사용할 때 안전한 폴백 조건이 있는가?