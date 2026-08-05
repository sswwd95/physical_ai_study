# 실습 303 — missing_value_interpolation

## 1. 학습 목표
센서 결측값을 시간 보간으로 복원합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
다중 센서 결측값을 선형 시간 보간하고 전후 결측 수를 비교하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage16
python examples\ex303_missing_value_interpolation.py
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
| 16 | `sensor_df = sensor_df.sort_values("timestamp")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 17 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 18 | `sensor_columns = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `    "temp_sensor_a_c",` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 20 | `    "temp_sensor_b_c",` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 21 | `    "pressure_sensor_a_pa",` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 22 | `    "pressure_sensor_b_pa",` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 23 | `    "rf_sensor_w",` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 24 | `    "gas_sensor_sccm",` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 25 | `]` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 26 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 27 | `before = sensor_df[sensor_columns].isna().sum()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `sensor_df[sensor_columns] = sensor_df[sensor_columns].interpolate(` | 시간 순서에 따라 결측값을 보간합니다. |
| 29 | `    method="linear",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `    limit_direction="both",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `)` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 32 | `after = sensor_df[sensor_columns].isna().sum()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 33 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 34 | `summary_df = pd.DataFrame({` | 계산 결과나 설정값을 변수에 저장합니다. |
| 35 | `    "missing_before": before,` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 36 | `    "missing_after": after,` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 37 | `})` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 38 | `print(summary_df)` | 결과를 콘솔에 출력합니다. |
| 39 | `sensor_df.to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 40 | `    OUTPUT_DIR / "ex303_interpolated_stream.csv",` | 시간 순서에 따라 결측값을 보간합니다. |
| 41 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 43 | `)` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 센서 시간축과 샘플링 주기가 일치하는가?
2. 트윈 오차가 센서 문제인지 모델 문제인지 구분했는가?
3. 추정값을 제어에 사용할 때 안전한 폴백 조건이 있는가?