# 실습 102 — feature_target_split

## 1. 학습 목표
입력 특징 X와 목표 라벨 y를 분리하고 사용하지 않을 식별 컬럼을 제외합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
timestamp, lot_id, defect_type은 모델 입력에서 제외하고 defect를 목표값 y로 분리하라.
입력 컬럼 목록, X 크기, y 클래스 건수를 출력하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage06
python examples\ex102_feature_target_split.py
```

## 4. 예상 결과
모델 입력 특징과 목표 라벨이 명확하게 분리됩니다.

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
| 17 | `drop_columns = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 18 | `    "timestamp",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 19 | `    "lot_id",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 20 | `    "defect",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 21 | `    "defect_type",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 22 | `]` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 23 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 24 | `x = sensor_df.drop(columns=drop_columns)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `y = sensor_df["defect"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 27 | `print("입력 컬럼:")` | 실행 결과를 콘솔에 출력합니다. |
| 28 | `print(x.columns.tolist())` | 실행 결과를 콘솔에 출력합니다. |
| 29 | `print("X 크기:", x.shape)` | 실행 결과를 콘솔에 출력합니다. |
| 30 | `print("y 클래스 건수:")` | 실행 결과를 콘솔에 출력합니다. |
| 31 | `print(y.value_counts())` | 실행 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 불량 라벨은 어떤 검사 장비와 판정 절차에서 생성되었는가?
2. LOT 단위 데이터 누수가 발생하지 않도록 어떻게 분할할 것인가?
3. 불량 미탐지와 정상 오탐 중 어느 비용이 더 큰가?