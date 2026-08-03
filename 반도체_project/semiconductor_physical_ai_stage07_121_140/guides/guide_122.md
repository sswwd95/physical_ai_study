# 실습 122 — label_encoding

## 1. 학습 목표
문자열 불량 유형을 정수 라벨로 변환하고 역변환 방법을 익힙니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
LabelEncoder로 defect_type을 정수 라벨로 변환하라.
classes_, 원본과 정수 라벨의 매핑, inverse_transform 예시를 출력하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage07
python examples\ex122_label_encoding.py
```

## 4. 예상 결과
문자열 클래스와 정수 라벨의 대응 관계가 저장됩니다.

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
| 15 | `from sklearn.preprocessing import LabelEncoder` | 필요한 라이브러리나 모델을 불러옵니다. |
| 16 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 17 | `sensor_df = pd.read_csv(DATA_FILE)` | 다중 불량 유형 CSV를 DataFrame으로 읽습니다. |
| 18 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 19 | `encoder = LabelEncoder()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `encoded = encoder.fit_transform(sensor_df["defect_type"])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 22 | `mapping_df = pd.DataFrame({` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `    "class_name": encoder.classes_,` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 24 | `    "encoded_value": np.arange(len(encoder.classes_)),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 25 | `})` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 26 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 27 | `print(mapping_df)` | 실행 결과를 콘솔에 출력합니다. |
| 28 | `print("처음 10개 정수 라벨:", encoded[:10])` | 실행 결과를 콘솔에 출력합니다. |
| 29 | `print(` | 실행 결과를 콘솔에 출력합니다. |
| 30 | `    "역변환 예시:",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 31 | `    encoder.inverse_transform(encoded[:10]),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 32 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 33 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 34 | `mapping_df.to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 35 | `    OUTPUT_DIR / "ex122_label_mapping.csv",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 36 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 37 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 38 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 가장 희소한 불량 유형의 재현율이 낮으면 어떤 위험이 있는가?
2. macro F1과 weighted F1 중 어떤 지표가 더 적합한가?
3. 클래스 확률이 낮을 때 보류 또는 재검사 정책을 어떻게 설계할 것인가?