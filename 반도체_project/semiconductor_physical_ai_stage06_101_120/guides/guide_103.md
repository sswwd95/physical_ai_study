# 실습 103 — stratified_train_test_split

## 1. 학습 목표
층화 분할로 학습·평가 데이터의 불량 비율을 유지합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
train_test_split을 사용해 테스트 비율 0.25, random_state=42로 분할하라.
stratify=y를 적용하고 전체·학습·평가 데이터의 불량 비율을 비교하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage06
python examples\ex103_stratified_train_test_split.py
```

## 4. 예상 결과
학습·평가 데이터의 불량 비율이 전체 데이터와 유사하게 유지됩니다.

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
| 15 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리나 모델을 불러옵니다. |
| 16 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 17 | `sensor_df = pd.read_csv(DATA_FILE)` | 불량 분류용 CSV를 DataFrame으로 읽습니다. |
| 18 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 19 | `x = sensor_df.drop(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `    columns=["timestamp", "lot_id", "defect", "defect_type"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 22 | `y = sensor_df["defect"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 24 | `x_train, x_test, y_train, y_test = train_test_split(` | 학습용 데이터와 평가용 데이터를 분리합니다. |
| 25 | `    x,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 26 | `    y,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 27 | `    test_size=0.25,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `    random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `    stratify=y,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 31 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 32 | `print("전체 불량 비율:", round(y.mean(), 4))` | 실행 결과를 콘솔에 출력합니다. |
| 33 | `print("학습 불량 비율:", round(y_train.mean(), 4))` | 실행 결과를 콘솔에 출력합니다. |
| 34 | `print("평가 불량 비율:", round(y_test.mean(), 4))` | 실행 결과를 콘솔에 출력합니다. |
| 35 | `print("학습 크기:", x_train.shape)` | 실행 결과를 콘솔에 출력합니다. |
| 36 | `print("평가 크기:", x_test.shape)` | 실행 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 불량 라벨은 어떤 검사 장비와 판정 절차에서 생성되었는가?
2. LOT 단위 데이터 누수가 발생하지 않도록 어떻게 분할할 것인가?
3. 불량 미탐지와 정상 오탐 중 어느 비용이 더 큰가?