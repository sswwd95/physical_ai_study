# 실습 001 — generate_sensor_data

## 1. 학습 목표
반도체 식각 장비를 모사한 온도·압력·RF 전력·가스 유량 센서 데이터를 생성하고 CSV 구조를 이해합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
Windows 10과 Anaconda에서 실행할 초보자용 Python 예제를 작성하라.
반도체 식각 장비의 300개 시점 데이터를 합성하라.
컬럼은 timestamp, lot_id, chamber_temp_c, chamber_pressure_pa, rf_power_w,
gas_flow_sccm, vibration_g, particle_count, process_state로 구성하라.
정상 구간과 일부 이상 구간을 포함하고 data/semiconductor_sensor_data.csv에 저장하라.
재현 가능하도록 난수 시드를 고정하고 각 처리 단계에 한국어 주석을 넣어라.
```

## 3. 실행 방법
```bat
conda activate semi-physical-ai
python examples\ex001_generate_sensor_data.py
```

## 4. 예상 결과
300행의 센서 데이터가 생성되고 `data/semiconductor_sensor_data.csv`에 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 실습에 필요한 외부 기능을 불러옵니다. |
| 2 | `import numpy as np` | 실습에 필요한 외부 기능을 불러옵니다. |
| 3 | `import pandas as pd` | 실습에 필요한 외부 기능을 불러옵니다. |
| 4 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 6 | `DATA_DIR = ROOT / "data"` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 7 | `DATA_DIR.mkdir(exist_ok=True)` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 8 | `OUTPUT_FILE = DATA_DIR / "semiconductor_sensor_data.csv"` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 9 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 10 | `rng = np.random.default_rng(42)` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 11 | `row_count = 300` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 12 | `timestamp = pd.date_range("2026-01-01 09:00:00", periods=row_count, freq="s")` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 13 | `lot_id = np.repeat(["LOT-A", "LOT-B", "LOT-C"], row_count // 3)` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 14 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 15 | `temperature = rng.normal(72.0, 0.8, row_count)` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 16 | `pressure = rng.normal(18.0, 0.35, row_count)` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 17 | `rf_power = rng.normal(850.0, 12.0, row_count)` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 18 | `gas_flow = rng.normal(120.0, 2.0, row_count)` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 19 | `vibration = np.abs(rng.normal(0.08, 0.015, row_count))` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 20 | `particle_count = rng.poisson(4, row_count)` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 21 | `process_state = np.repeat(["stabilize", "process", "purge"], 100)` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 22 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 23 | `anomaly_index = np.arange(220, 235)` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 24 | `temperature[anomaly_index] += rng.normal(5.0, 0.5, len(anomaly_index))` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 25 | `pressure[anomaly_index] += rng.normal(2.5, 0.2, len(anomaly_index))` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 26 | `vibration[anomaly_index] += rng.normal(0.12, 0.01, len(anomaly_index))` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 27 | `particle_count[anomaly_index] += rng.poisson(12, len(anomaly_index))` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 28 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 29 | `sensor_df = pd.DataFrame(` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 30 | `    {` | 실습 흐름에 필요한 명령을 수행합니다. |
| 31 | `        "timestamp": timestamp,` | 실습 흐름에 필요한 명령을 수행합니다. |
| 32 | `        "lot_id": lot_id,` | 실습 흐름에 필요한 명령을 수행합니다. |
| 33 | `        "chamber_temp_c": temperature,` | 실습 흐름에 필요한 명령을 수행합니다. |
| 34 | `        "chamber_pressure_pa": pressure,` | 실습 흐름에 필요한 명령을 수행합니다. |
| 35 | `        "rf_power_w": rf_power,` | 실습 흐름에 필요한 명령을 수행합니다. |
| 36 | `        "gas_flow_sccm": gas_flow,` | 실습 흐름에 필요한 명령을 수행합니다. |
| 37 | `        "vibration_g": vibration,` | 실습 흐름에 필요한 명령을 수행합니다. |
| 38 | `        "particle_count": particle_count,` | 실습 흐름에 필요한 명령을 수행합니다. |
| 39 | `        "process_state": process_state,` | 실습 흐름에 필요한 명령을 수행합니다. |
| 40 | `    }` | 실습 흐름에 필요한 명령을 수행합니다. |
| 41 | `)` | 실습 흐름에 필요한 명령을 수행합니다. |
| 42 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 43 | `sensor_df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")` | 계산 결과를 CSV 파일로 저장합니다. |
| 44 | `print(f"저장 완료: {OUTPUT_FILE}")` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |
| 45 | `print(sensor_df.head())` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |

## 6. 확인 문제
1. 입력 데이터의 단위가 바뀌면 어느 부분을 수정해야 하는가?
2. 결측값 또는 이상값이 결과에 어떤 영향을 주는가?
3. 이 코드를 실제 반도체 장비 센서에 적용하려면 어떤 컬럼이 더 필요한가?