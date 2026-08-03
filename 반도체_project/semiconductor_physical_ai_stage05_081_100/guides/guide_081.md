# 실습 081 — anomaly_data_profile

## 1. 학습 목표
정상·이상 라벨과 센서 분포를 먼저 확인하여 탐지 문제를 정의합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
반도체 이상 탐지 CSV의 행·열 수, 이상 라벨 건수와 비율,
정상·이상 그룹별 주요 센서 평균을 계산하는 pandas 예제를 작성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage05
python examples\ex081_anomaly_data_profile.py
```

## 4. 예상 결과
정상과 이상 그룹의 센서 평균 차이가 출력됩니다.

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
| 15 | `print("데이터 크기:", sensor_df.shape)` | 실행 결과를 콘솔에 출력합니다. |
| 16 | `print("이상 건수:", int(sensor_df["true_anomaly"].sum()))` | 실행 결과를 콘솔에 출력합니다. |
| 17 | `print("이상 비율:", round(sensor_df["true_anomaly"].mean(), 4))` | 실행 결과를 콘솔에 출력합니다. |
| 18 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 19 | `group_summary = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `    sensor_df.groupby("true_anomaly")[` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 21 | `        [` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 22 | `            "chamber_temp_c",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 23 | `            "chamber_pressure_pa",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 24 | `            "rf_power_w",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 25 | `            "vibration_g",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 26 | `            "particle_count",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 27 | `        ]` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 28 | `    ]` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 29 | `    .mean()` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 30 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 31 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 32 | `print(group_summary.round(3))` | 실행 결과를 콘솔에 출력합니다. |
| 33 | `group_summary.to_csv(` | 분석 결과를 CSV로 저장합니다. |
| 34 | `    OUTPUT_DIR / "ex081_anomaly_group_summary.csv",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 35 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 36 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 이상 비율을 고정하면 실제 공정 변화에 어떤 문제가 생길 수 있는가?
2. 탐지된 이상을 삭제하기 전에 어떤 공정 정보를 확인해야 하는가?
3. 정답 라벨이 부족할 때 모델 성능을 어떻게 검증할 것인가?