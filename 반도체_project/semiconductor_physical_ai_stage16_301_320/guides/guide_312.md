# 실습 312 — phase_based_twin_model

## 1. 학습 목표
공정 단계별 디지털 트윈 기준값을 생성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
공정 단계별 디지털 트윈 기준값을 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage16
python examples\ex312_phase_based_twin_model.py
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
| 17 | `phase_twin = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 18 | `    sensor_df.groupby("process_phase")[` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 19 | `        [` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 20 | `            "true_temperature_c",` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 21 | `            "true_pressure_pa",` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 22 | `            "true_rf_power_w",` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 23 | `            "true_gas_flow_sccm",` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 24 | `        ]` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 25 | `    ]` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 26 | `    .mean()` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 27 | `)` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 28 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 29 | `print(phase_twin.round(3))` | 결과를 콘솔에 출력합니다. |
| 30 | `phase_twin.to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 31 | `    OUTPUT_DIR / "ex312_phase_twin_reference.csv",` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 32 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 33 | `)` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 센서 시간축과 샘플링 주기가 일치하는가?
2. 트윈 오차가 센서 문제인지 모델 문제인지 구분했는가?
3. 추정값을 제어에 사용할 때 안전한 폴백 조건이 있는가?