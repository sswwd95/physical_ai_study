# 실습 104 — lot_group_split

## 1. 학습 목표
같은 LOT가 학습과 평가에 동시에 들어가는 데이터 누수를 방지합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
GroupShuffleSplit을 사용하여 lot_id 단위로 학습과 평가 데이터를 분리하라.
test_size=0.25, random_state=42를 사용하고 두 집합의 LOT 교집합이 비어 있는지 확인하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage06
python examples\ex104_lot_group_split.py
```

## 4. 예상 결과
학습 LOT와 평가 LOT가 겹치지 않는 그룹 분할이 생성됩니다.

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
| 15 | `from sklearn.model_selection import GroupShuffleSplit` | 필요한 라이브러리나 모델을 불러옵니다. |
| 16 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 17 | `sensor_df = pd.read_csv(DATA_FILE)` | 불량 분류용 CSV를 DataFrame으로 읽습니다. |
| 18 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 19 | `x = sensor_df.drop(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `    columns=["timestamp", "lot_id", "defect", "defect_type"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 22 | `y = sensor_df["defect"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `groups = sensor_df["lot_id"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 25 | `splitter = GroupShuffleSplit(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `    n_splits=1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `    test_size=0.25,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `    random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 30 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 31 | `train_index, test_index = next(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `    splitter.split(x, y, groups=groups)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 33 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 34 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 35 | `train_lots = set(groups.iloc[train_index])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 36 | `test_lots = set(groups.iloc[test_index])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 37 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 38 | `print("학습 LOT 수:", len(train_lots))` | 실행 결과를 콘솔에 출력합니다. |
| 39 | `print("평가 LOT 수:", len(test_lots))` | 실행 결과를 콘솔에 출력합니다. |
| 40 | `print("LOT 교집합:", train_lots & test_lots)` | 실행 결과를 콘솔에 출력합니다. |
| 41 | `print("학습 행 수:", len(train_index))` | 실행 결과를 콘솔에 출력합니다. |
| 42 | `print("평가 행 수:", len(test_index))` | 실행 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 불량 라벨은 어떤 검사 장비와 판정 절차에서 생성되었는가?
2. LOT 단위 데이터 누수가 발생하지 않도록 어떻게 분할할 것인가?
3. 불량 미탐지와 정상 오탐 중 어느 비용이 더 큰가?