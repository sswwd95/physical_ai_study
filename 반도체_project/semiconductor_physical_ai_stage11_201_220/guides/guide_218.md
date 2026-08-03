# 실습 218 — low_confidence_faults

## 1. 학습 목표
낮은 확률 예측을 재검사 대상으로 분리합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
최대 확률 0.65 미만을 재검사 대상으로 분리하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage11
python examples\ex218_low_confidence_faults.py
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
| 16 | `from sklearn.ensemble import RandomForestClassifier` | 필요한 라이브러리나 분류 모델을 불러옵니다. |
| 17 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리나 분류 모델을 불러옵니다. |
| 18 | `from sklearn.pipeline import Pipeline` | 필요한 라이브러리나 분류 모델을 불러옵니다. |
| 19 | `from sklearn.preprocessing import OneHotEncoder` | 필요한 라이브러리나 분류 모델을 불러옵니다. |
| 20 | `sensor_df=pd.read_csv(DATA_FILE)` | 장비 상태 진단 CSV를 DataFrame으로 읽습니다. |
| 21 | `features=["equipment_id","operation_mode","temperature_c","pressure_pa","vibration_rms_g","vibration_peak_g","motor_current_a","pump_speed_rpm","gas_flow_sccm","particle_count","maintenance_age_hours"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `X=sensor_df[features]; y=sensor_df["fault_type"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `idx=np.arange(len(sensor_df)); tr,te=train_test_split(idx,test_size=.25,random_state=42,stratify=y)` | 학습용 데이터와 평가용 데이터를 분리합니다. |
| 24 | `pre=ColumnTransformer([("num","passthrough",features[2:]),("cat",OneHotEncoder(handle_unknown="ignore"),features[:2])])` | 숫자형과 범주형 특징의 전처리를 묶습니다. |
| 25 | `m=Pipeline([("preprocess",pre),("classifier",RandomForestClassifier(n_estimators=350,class_weight="balanced",random_state=42,n_jobs=-1))])` | 전처리와 고장 분류 모델을 하나로 연결합니다. |
| 26 | `m.fit(X.iloc[tr],y.iloc[tr]); prob=m.predict_proba(X.iloc[te]); pred=m.predict(X.iloc[te])` | 학습 데이터로 모델을 학습합니다. |
| 27 | `out=sensor_df.iloc[te][["timestamp","equipment_id","fault_type"]].copy(); out["predicted_fault"]=pred; out["max_probability"]=prob.max(1); out["review_required"]=out["max_probability"]<.65` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `print("재검사:",int(out["review_required"].sum())); out.to_csv(OUTPUT_DIR/"ex218_low_confidence.csv",index=False,encoding="utf-8-sig")` | 결과를 CSV 파일로 저장합니다. |

## 6. 실무 확인 질문
1. 고장 라벨은 정비 이력과 어떤 규칙으로 연결되었는가?
2. 장비별 편차와 운전모드 차이를 모델이 구분하는가?
3. 고장 확률이 낮을 때 자동 정지보다 재검사가 적절한가?