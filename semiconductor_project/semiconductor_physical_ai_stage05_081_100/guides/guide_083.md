# 실습 083 — iqr_multi_sensor_flags

## 1. 학습 목표
여러 센서에 IQR 규칙을 적용하고 행별 이상 센서 수를 계산합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
온도, 압력, RF, 가스, 진동, 입자 수에 대해 1.5*IQR 이상치 플래그를 만들라.
행별 이상 센서 개수 anomaly_sensor_count를 계산하고 2개 이상이면 multi_iqr_anomaly로 표시하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage05
python examples\ex083_iqr_multi_sensor_flags.py
```

## 4. 예상 결과
한 행에서 동시에 이상인 센서 수와 다중 이상 여부가 계산됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 기능을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 기능을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 기능을 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "semiconductor_anomaly_data.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError("data/semiconductor_anomaly_data.csv 파일이 없습니다.")` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 12 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 13 | `sensor_df = pd.read_csv(DATA_FILE)` | 센서 CSV를 DataFrame으로 읽습니다. |
| 14 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 15 | `features = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 16 | `    "chamber_temp_c",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 17 | `    "chamber_pressure_pa",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 18 | `    "rf_power_w",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 19 | `    "gas_flow_sccm",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 20 | `    "vibration_g",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 21 | `    "particle_count",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 22 | `]` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 23 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 24 | `flags = []` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `for column in features:` | 여러 센서나 파라미터에 같은 계산을 반복합니다. |
| 26 | `    q1 = sensor_df[column].quantile(0.25)` | 분포의 분위수를 이용해 임계값을 계산합니다. |
| 27 | `    q3 = sensor_df[column].quantile(0.75)` | 분포의 분위수를 이용해 임계값을 계산합니다. |
| 28 | `    iqr = q3 - q1` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `    lower = q1 - 1.5 * iqr` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `    upper = q3 + 1.5 * iqr` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `    flag = f"{column}_iqr_anomaly"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `    sensor_df[flag] = ~sensor_df[column].between(lower, upper)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 33 | `    flags.append(flag)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 34 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 35 | `sensor_df["anomaly_sensor_count"] = sensor_df[flags].sum(axis=1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 36 | `sensor_df["multi_iqr_anomaly"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 37 | `    sensor_df["anomaly_sensor_count"] >= 2` | 계산 결과나 설정값을 변수에 저장합니다. |
| 38 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 39 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 40 | `print(` | 실행 결과를 콘솔에 출력합니다. |
| 41 | `    "다중 IQR 이상 행:",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 42 | `    int(sensor_df["multi_iqr_anomaly"].sum()),` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 43 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 이상 비율을 고정하면 실제 공정 변화에 어떤 문제가 생길 수 있는가?
2. 탐지된 이상을 삭제하기 전에 어떤 공정 정보를 확인해야 하는가?
3. 정답 라벨이 부족할 때 모델 성능을 어떻게 검증할 것인가?