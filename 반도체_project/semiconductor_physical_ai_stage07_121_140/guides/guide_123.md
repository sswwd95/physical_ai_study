# 실습 123 — multiclass_stratified_split

## 1. 학습 목표
다중 클래스 비율을 유지하는 층화 분할을 수행합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
defect_type을 목표값으로 하고 train_test_split에서 stratify=y를 사용하라.
테스트 비율 0.25, random_state=42로 분할하고 전체·학습·평가 클래스 비율을 비교하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage07
python examples\ex123_multiclass_stratified_split.py
```

## 4. 예상 결과
학습·평가 데이터의 클래스 비율이 전체 비율과 유사하게 유지됩니다.

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
| 15 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리나 모델을 불러옵니다. |
| 16 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 17 | `sensor_df = pd.read_csv(DATA_FILE)` | 다중 불량 유형 CSV를 DataFrame으로 읽습니다. |
| 18 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 19 | `x = sensor_df.drop(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `    columns=["timestamp", "lot_id", "defect_type"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 22 | `y = sensor_df["defect_type"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 24 | `x_train, x_test, y_train, y_test = train_test_split(` | 학습용과 평가용 데이터를 분리합니다. |
| 25 | `    x,` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 26 | `    y,` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 27 | `    test_size=0.25,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `    random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `    stratify=y,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 31 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 32 | `ratio_df = pd.DataFrame({` | 계산 결과나 설정값을 변수에 저장합니다. |
| 33 | `    "overall": y.value_counts(normalize=True),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 34 | `    "train": y_train.value_counts(normalize=True),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 35 | `    "test": y_test.value_counts(normalize=True),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 36 | `}).fillna(0)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 37 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 38 | `print(ratio_df.round(4))` | 실행 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 가장 희소한 불량 유형의 재현율이 낮으면 어떤 위험이 있는가?
2. macro F1과 weighted F1 중 어떤 지표가 더 적합한가?
3. 클래스 확률이 낮을 때 보류 또는 재검사 정책을 어떻게 설계할 것인가?