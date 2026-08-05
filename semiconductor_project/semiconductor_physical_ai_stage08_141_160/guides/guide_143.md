# 실습 143 — regression_train_test_split

## 1. 학습 목표
학습·평가 데이터로 분할하고 수율 분포를 비교합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
train_test_split을 test_size=0.25, random_state=42로 적용하라.
학습과 평가 데이터의 수율 평균과 표준편차를 비교하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage08
python examples\ex143_regression_train_test_split.py
```

## 4. 예상 결과
학습·평가 데이터의 수율 분포가 유사한지 확인합니다.

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
| 15 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리나 회귀 모델을 불러옵니다. |
| 16 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 17 | `sensor_df = pd.read_csv(DATA_FILE)` | 수율 예측용 CSV를 DataFrame으로 읽습니다. |
| 18 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 19 | `x = sensor_df.drop(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `    columns=["timestamp", "lot_id", "yield_percent"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `)` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 22 | `y = sensor_df["yield_percent"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 24 | `x_train, x_test, y_train, y_test = train_test_split(` | 학습용 데이터와 평가용 데이터를 분리합니다. |
| 25 | `    x,` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 26 | `    y,` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 27 | `    test_size=0.25,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `    random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `)` | 수율 회귀 모델의 학습·평가 단계를 수행합니다. |
| 30 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 31 | `print("학습 수율 평균:", round(y_train.mean(), 3))` | 실행 결과를 콘솔에 출력합니다. |
| 32 | `print("평가 수율 평균:", round(y_test.mean(), 3))` | 실행 결과를 콘솔에 출력합니다. |
| 33 | `print("학습 수율 표준편차:", round(y_train.std(), 3))` | 실행 결과를 콘솔에 출력합니다. |
| 34 | `print("평가 수율 표준편차:", round(y_test.std(), 3))` | 실행 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 수율 라벨이 어떤 검사 시점과 기준으로 계산되었는가?
2. LOT·레시피·챔버 정보가 누수 없이 분할되었는가?
3. 평균 오차뿐 아니라 저수율 구간의 오차를 별도로 확인해야 하는가?