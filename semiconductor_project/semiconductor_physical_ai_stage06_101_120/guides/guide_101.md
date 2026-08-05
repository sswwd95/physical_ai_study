# 실습 101 — defect_data_profile

## 1. 학습 목표
불량 분류 데이터의 클래스 비율과 주요 센서 분포를 확인합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
반도체 불량 분류 CSV의 행·열 수, defect 클래스 건수와 비율,
defect_type 건수, 정상·불량별 주요 센서 평균을 출력하는 pandas 예제를 작성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage06
python examples\ex101_defect_data_profile.py
```

## 4. 예상 결과
클래스 불균형 정도와 정상·불량 간 센서 평균 차이가 출력됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 모델을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 모델을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 모델을 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "semiconductor_defect_classification.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError(` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 12 | `        "data/semiconductor_defect_classification.csv 파일이 없습니다."` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 13 | `    )` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 14 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 15 | `sensor_df = pd.read_csv(DATA_FILE)` | 불량 분류용 CSV를 DataFrame으로 읽습니다. |
| 16 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 17 | `print("데이터 크기:", sensor_df.shape)` | 실행 결과를 콘솔에 출력합니다. |
| 18 | `print("\n불량 클래스 건수:")` | 실행 결과를 콘솔에 출력합니다. |
| 19 | `print(sensor_df["defect"].value_counts())` | 실행 결과를 콘솔에 출력합니다. |
| 20 | `print("\n불량 비율:", round(sensor_df["defect"].mean(), 4))` | 실행 결과를 콘솔에 출력합니다. |
| 21 | `print("\n불량 유형:")` | 실행 결과를 콘솔에 출력합니다. |
| 22 | `print(sensor_df["defect_type"].value_counts())` | 실행 결과를 콘솔에 출력합니다. |
| 23 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 24 | `summary = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `    sensor_df.groupby("defect")[` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 26 | `        [` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 27 | `            "chamber_temp_c",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 28 | `            "chamber_pressure_pa",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 29 | `            "rf_power_w",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 30 | `            "vibration_g",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 31 | `            "particle_count",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 32 | `            "etch_rate_nm_min",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 33 | `            "uniformity_percent",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 34 | `        ]` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 35 | `    ]` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 36 | `    .mean()` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 37 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 38 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 39 | `print("\n정상·불량 그룹 평균:")` | 실행 결과를 콘솔에 출력합니다. |
| 40 | `print(summary.round(3))` | 실행 결과를 콘솔에 출력합니다. |
| 41 | `summary.to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 42 | `    OUTPUT_DIR / "ex101_defect_group_summary.csv",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 43 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 44 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 불량 라벨은 어떤 검사 장비와 판정 절차에서 생성되었는가?
2. LOT 단위 데이터 누수가 발생하지 않도록 어떻게 분할할 것인가?
3. 불량 미탐지와 정상 오탐 중 어느 비용이 더 큰가?