# 실습 121 — multiclass_data_profile

## 1. 학습 목표
다중 불량 유형의 클래스 분포와 특징 평균을 확인합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
반도체 다중 불량 유형 CSV에서 클래스별 건수와 비율,
클래스별 주요 센서 평균을 출력하는 pandas 예제를 작성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage07
python examples\ex121_multiclass_data_profile.py
```

## 4. 예상 결과
normal, particle, uniformity, etch_rate 클래스의 분포와 특징 차이가 출력됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 모델을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 모델을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 모델을 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "semiconductor_multiclass_defects.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError(` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 12 | `        "data/semiconductor_multiclass_defects.csv 파일이 없습니다."` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 13 | `    )` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 14 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 15 | `sensor_df = pd.read_csv(DATA_FILE)` | 다중 불량 유형 CSV를 DataFrame으로 읽습니다. |
| 16 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 17 | `class_count = sensor_df["defect_type"].value_counts()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 18 | `class_ratio = sensor_df["defect_type"].value_counts(normalize=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 20 | `print("클래스 건수:")` | 실행 결과를 콘솔에 출력합니다. |
| 21 | `print(class_count)` | 실행 결과를 콘솔에 출력합니다. |
| 22 | `print("\n클래스 비율:")` | 실행 결과를 콘솔에 출력합니다. |
| 23 | `print(class_ratio.round(4))` | 실행 결과를 콘솔에 출력합니다. |
| 24 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 25 | `summary = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `    sensor_df.groupby("defect_type")[` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 27 | `        [` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 28 | `            "chamber_temp_c",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 29 | `            "chamber_pressure_pa",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 30 | `            "rf_power_w",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 31 | `            "vibration_g",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 32 | `            "particle_count",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 33 | `            "etch_rate_nm_min",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 34 | `            "uniformity_percent",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 35 | `        ]` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 36 | `    ]` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 37 | `    .mean()` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 38 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 39 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 40 | `print("\n클래스별 평균:")` | 실행 결과를 콘솔에 출력합니다. |
| 41 | `print(summary.round(3))` | 실행 결과를 콘솔에 출력합니다. |
| 42 | `summary.to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 43 | `    OUTPUT_DIR / "ex121_multiclass_summary.csv",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 44 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 45 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 가장 희소한 불량 유형의 재현율이 낮으면 어떤 위험이 있는가?
2. macro F1과 weighted F1 중 어떤 지표가 더 적합한가?
3. 클래스 확률이 낮을 때 보류 또는 재검사 정책을 어떻게 설계할 것인가?