# 실습 141 — yield_data_profile

## 1. 학습 목표
수율 분포와 공정 변수의 기본 통계를 확인합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
반도체 수율 회귀 CSV의 행·열 수, 수율 평균·표준편차·최소·최대,
레시피별 평균 수율을 출력하는 pandas 예제를 작성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage08
python examples\ex141_yield_data_profile.py
```

## 4. 예상 결과
전체 수율 분포와 레시피별 평균 수율이 출력됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "semiconductor_yield_regression.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError(` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 12 | `        "data/semiconductor_yield_regression.csv 파일이 없습니다."` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 13 | `    )` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 14 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 15 | `sensor_df = pd.read_csv(DATA_FILE)` | 수율 예측용 CSV를 DataFrame으로 읽습니다. |
| 16 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 17 | `print("데이터 크기:", sensor_df.shape)` | 실행 결과를 콘솔에 출력합니다. |
| 18 | `print("\n수율 요약:")` | 실행 결과를 콘솔에 출력합니다. |
| 19 | `print(sensor_df["yield_percent"].describe().round(3))` | 실행 결과를 콘솔에 출력합니다. |
| 20 | `print("\n레시피별 평균 수율:")` | 실행 결과를 콘솔에 출력합니다. |
| 21 | `print(` | 실행 결과를 콘솔에 출력합니다. |
| 22 | `    sensor_df.groupby("recipe")["yield_percent"]` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 23 | `    .mean()` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 24 | `    .sort_values(ascending=False)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `    .round(3)` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 26 | `)` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 수율 라벨이 어떤 검사 시점과 기준으로 계산되었는가?
2. LOT·레시피·챔버 정보가 누수 없이 분할되었는가?
3. 평균 오차뿐 아니라 저수율 구간의 오차를 별도로 확인해야 하는가?