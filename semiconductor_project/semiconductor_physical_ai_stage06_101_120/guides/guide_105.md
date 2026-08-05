# 실습 105 — preprocessing_pipeline

## 1. 학습 목표
숫자형 표준화와 범주형 One-Hot Encoding을 하나의 전처리기로 구성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
숫자형 컬럼에는 StandardScaler, recipe와 chamber_id에는 OneHotEncoder를 적용하는
ColumnTransformer를 작성하라. 학습 데이터에 fit_transform하고 변환 후 배열 크기를 출력하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage06
python examples\ex105_preprocessing_pipeline.py
```

## 4. 예상 결과
숫자형·범주형 전처리가 하나의 변환기로 구성됩니다.

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
| 15 | `from sklearn.compose import ColumnTransformer` | 필요한 라이브러리나 모델을 불러옵니다. |
| 16 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리나 모델을 불러옵니다. |
| 17 | `from sklearn.preprocessing import OneHotEncoder, StandardScaler` | 필요한 라이브러리나 모델을 불러옵니다. |
| 18 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 19 | `sensor_df = pd.read_csv(DATA_FILE)` | 불량 분류용 CSV를 DataFrame으로 읽습니다. |
| 20 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 21 | `x = sensor_df.drop(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `    columns=["timestamp", "lot_id", "defect", "defect_type"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 24 | `y = sensor_df["defect"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 26 | `numeric_features = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `    "chamber_temp_c",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 28 | `    "chamber_pressure_pa",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 29 | `    "rf_power_w",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 30 | `    "gas_flow_sccm",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 31 | `    "vibration_g",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 32 | `    "particle_count",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 33 | `    "etch_rate_nm_min",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 34 | `    "uniformity_percent",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 35 | `]` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 36 | `categorical_features = ["recipe", "chamber_id"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 37 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 38 | `x_train, x_test, y_train, y_test = train_test_split(` | 학습용 데이터와 평가용 데이터를 분리합니다. |
| 39 | `    x,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 40 | `    y,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 41 | `    test_size=0.25,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `    random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 43 | `    stratify=y,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 44 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 45 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 46 | `preprocessor = ColumnTransformer(` | 숫자형과 범주형 컬럼의 전처리를 하나로 묶습니다. |
| 47 | `    transformers=[` | 계산 결과나 설정값을 변수에 저장합니다. |
| 48 | `        ("numeric", StandardScaler(), numeric_features),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 49 | `        (` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 50 | `            "categorical",` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 51 | `            OneHotEncoder(handle_unknown="ignore"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 52 | `            categorical_features,` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 53 | `        ),` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 54 | `    ]` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 55 | `)` | 분류 모델의 전처리·학습·평가 단계를 수행합니다. |
| 56 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 57 | `x_train_transformed = preprocessor.fit_transform(x_train)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 58 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 59 | `print("원본 학습 크기:", x_train.shape)` | 실행 결과를 콘솔에 출력합니다. |
| 60 | `print("변환 후 크기:", x_train_transformed.shape)` | 실행 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 불량 라벨은 어떤 검사 장비와 판정 절차에서 생성되었는가?
2. LOT 단위 데이터 누수가 발생하지 않도록 어떻게 분할할 것인가?
3. 불량 미탐지와 정상 오탐 중 어느 비용이 더 큰가?