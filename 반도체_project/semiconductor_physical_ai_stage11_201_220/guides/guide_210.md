# 실습 210 — gradient_boosting_faults

## 1. 학습 목표
Gradient Boosting으로 고장 유형을 분류합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
HistGradientBoosting으로 장비 고장 유형을 분류하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage11
python examples\ex210_gradient_boosting_faults.py
```

## 4. 예상 결과
요청한 장비 상태 진단 결과가 출력 또는 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 분류 모델을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 분류 모델을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 분류 모델을 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "equipment_fault_diagnosis.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 장비 상태 진단 또는 고장 분류 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError(` | 장비 상태 진단 또는 고장 분류 단계를 수행합니다. |
| 12 | `        "data/equipment_fault_diagnosis.csv 파일이 없습니다."` | 장비 상태 진단 또는 고장 분류 단계를 수행합니다. |
| 13 | `    )` | 장비 상태 진단 또는 고장 분류 단계를 수행합니다. |
| 14 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 15 | `from sklearn.compose import ColumnTransformer` | 필요한 라이브러리나 분류 모델을 불러옵니다. |
| 16 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리나 분류 모델을 불러옵니다. |
| 17 | `from sklearn.pipeline import Pipeline` | 필요한 라이브러리나 분류 모델을 불러옵니다. |
| 18 | `from sklearn.preprocessing import OneHotEncoder, StandardScaler` | 필요한 라이브러리나 분류 모델을 불러옵니다. |
| 19 | `from sklearn.metrics import classification_report, f1_score, accuracy_score` | 필요한 라이브러리나 분류 모델을 불러옵니다. |
| 20 | `from sklearn.ensemble import HistGradientBoostingClassifier` | 필요한 라이브러리나 분류 모델을 불러옵니다. |
| 21 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 22 | `sensor_df=pd.read_csv(DATA_FILE)` | 장비 상태 진단 CSV를 DataFrame으로 읽습니다. |
| 23 | `features=[` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `"equipment_id","operation_mode","temperature_c","pressure_pa","vibration_rms_g",` | 장비 상태 진단 또는 고장 분류 단계를 수행합니다. |
| 25 | `"vibration_peak_g","motor_current_a","pump_speed_rpm","gas_flow_sccm",` | 장비 상태 진단 또는 고장 분류 단계를 수행합니다. |
| 26 | `"particle_count","maintenance_age_hours"]` | 장비 상태 진단 또는 고장 분류 단계를 수행합니다. |
| 27 | `X=sensor_df[features]; y=sensor_df["fault_type"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `X_train,X_test,y_train,y_test=train_test_split(` | 학습용 데이터와 평가용 데이터를 분리합니다. |
| 29 | `    X,y,test_size=.25,random_state=42,stratify=y)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `num=features[2:]; cat=features[:2]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `pre=ColumnTransformer([` | 숫자형과 범주형 특징의 전처리를 묶습니다. |
| 32 | `    ("num","passthrough",num),` | 장비 상태 진단 또는 고장 분류 단계를 수행합니다. |
| 33 | `    ("cat",OneHotEncoder(handle_unknown="ignore"),cat)])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 34 | `model=Pipeline([` | 전처리와 고장 분류 모델을 하나로 연결합니다. |
| 35 | `    ("preprocess",pre),` | 장비 상태 진단 또는 고장 분류 단계를 수행합니다. |
| 36 | `    ("classifier",HistGradientBoostingClassifier(max_iter=220,learning_rate=.08,max_depth=7,random_state=42))])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 37 | `model.fit(X_train,y_train)` | 학습 데이터로 모델을 학습합니다. |
| 38 | `pred=model.predict(X_test)` | 장비 상태 또는 고장 유형을 예측합니다. |
| 39 | `print("Macro F1:",round(f1_score(y_test,pred,average="macro"),4))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 고장 라벨은 정비 이력과 어떤 규칙으로 연결되었는가?
2. 장비별 편차와 운전모드 차이를 모델이 구분하는가?
3. 고장 확률이 낮을 때 자동 정지보다 재검사가 적절한가?