# 실습 217 — model_comparison

## 1. 학습 목표
여러 고장 분류 모델을 비교합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
Logistic, RandomForest, HistGradientBoosting 성능을 비교하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage11
python examples\ex217_model_comparison.py
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
| 16 | `from sklearn.ensemble import RandomForestClassifier,HistGradientBoostingClassifier` | 필요한 라이브러리나 분류 모델을 불러옵니다. |
| 17 | `from sklearn.linear_model import LogisticRegression` | 필요한 라이브러리나 분류 모델을 불러옵니다. |
| 18 | `from sklearn.metrics import f1_score,accuracy_score` | 필요한 라이브러리나 분류 모델을 불러옵니다. |
| 19 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리나 분류 모델을 불러옵니다. |
| 20 | `from sklearn.pipeline import Pipeline` | 필요한 라이브러리나 분류 모델을 불러옵니다. |
| 21 | `from sklearn.preprocessing import OneHotEncoder,StandardScaler` | 필요한 라이브러리나 분류 모델을 불러옵니다. |
| 22 | `sensor_df=pd.read_csv(DATA_FILE)` | 장비 상태 진단 CSV를 DataFrame으로 읽습니다. |
| 23 | `features=["equipment_id","operation_mode","temperature_c","pressure_pa","vibration_rms_g","vibration_peak_g","motor_current_a","pump_speed_rpm","gas_flow_sccm","particle_count","maintenance_age_hours"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `X=sensor_df[features]; y=sensor_df["fault_type"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)` | 학습용 데이터와 평가용 데이터를 분리합니다. |
| 26 | `lin=ColumnTransformer([("num",StandardScaler(),features[2:]),("cat",OneHotEncoder(handle_unknown="ignore"),features[:2])])` | 숫자형과 범주형 특징의 전처리를 묶습니다. |
| 27 | `tree=ColumnTransformer([("num","passthrough",features[2:]),("cat",OneHotEncoder(handle_unknown="ignore",sparse_output=False),features[:2])])` | 숫자형과 범주형 특징의 전처리를 묶습니다. |
| 28 | `models={"Logistic":Pipeline([("preprocess",lin),("classifier",LogisticRegression(max_iter=2000,class_weight="balanced",random_state=42))]),` | 전처리와 고장 분류 모델을 하나로 연결합니다. |
| 29 | `"RandomForest":Pipeline([("preprocess",tree),("classifier",RandomForestClassifier(n_estimators=350,class_weight="balanced",random_state=42,n_jobs=-1))]),` | 전처리와 고장 분류 모델을 하나로 연결합니다. |
| 30 | `"HistGB":Pipeline([("preprocess",tree),("classifier",HistGradientBoostingClassifier(max_iter=200,random_state=42))])}` | 전처리와 고장 분류 모델을 하나로 연결합니다. |
| 31 | `rows=[]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `for name,m in models.items():` | 여러 모델이나 설정에 같은 작업을 반복합니다. |
| 33 | `    m.fit(Xtr,ytr); p=m.predict(Xte); rows.append({"model":name,"accuracy":accuracy_score(yte,p),"macro_f1":f1_score(yte,p,average="macro")})` | 학습 데이터로 모델을 학습합니다. |
| 34 | `out=pd.DataFrame(rows).sort_values("macro_f1",ascending=False); print(out.round(4)); out.to_csv(OUTPUT_DIR/"ex217_model_comparison.csv",index=False,encoding="utf-8-sig")` | 결과를 CSV 파일로 저장합니다. |

## 6. 실무 확인 질문
1. 고장 라벨은 정비 이력과 어떤 규칙으로 연결되었는가?
2. 장비별 편차와 운전모드 차이를 모델이 구분하는가?
3. 고장 확률이 낮을 때 자동 정지보다 재검사가 적절한가?