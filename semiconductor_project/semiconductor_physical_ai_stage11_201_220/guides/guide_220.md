# 실습 220 — automated_fault_report

## 1. 학습 목표
자동 장비 고장 진단 Excel 보고서를 생성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
클래스지표, 혼동행렬, 예측, 특징중요도 Excel 보고서를 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage11
python examples\ex220_automated_fault_report.py
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
| 17 | `from sklearn.metrics import classification_report,confusion_matrix` | 필요한 라이브러리나 분류 모델을 불러옵니다. |
| 18 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리나 분류 모델을 불러옵니다. |
| 19 | `from sklearn.pipeline import Pipeline` | 필요한 라이브러리나 분류 모델을 불러옵니다. |
| 20 | `from sklearn.preprocessing import OneHotEncoder` | 필요한 라이브러리나 분류 모델을 불러옵니다. |
| 21 | `sensor_df=pd.read_csv(DATA_FILE,parse_dates=["timestamp"])` | 장비 상태 진단 CSV를 DataFrame으로 읽습니다. |
| 22 | `features=["equipment_id","operation_mode","temperature_c","pressure_pa","vibration_rms_g","vibration_peak_g","motor_current_a","pump_speed_rpm","gas_flow_sccm","particle_count","maintenance_age_hours"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `X=sensor_df[features]; y=sensor_df["fault_type"]; idx=np.arange(len(sensor_df)); tr,te=train_test_split(idx,test_size=.25,random_state=42,stratify=y)` | 학습용 데이터와 평가용 데이터를 분리합니다. |
| 24 | `pre=ColumnTransformer([("num","passthrough",features[2:]),("cat",OneHotEncoder(handle_unknown="ignore"),features[:2])])` | 숫자형과 범주형 특징의 전처리를 묶습니다. |
| 25 | `m=Pipeline([("preprocess",pre),("classifier",RandomForestClassifier(n_estimators=400,class_weight="balanced",random_state=42,n_jobs=-1))])` | 전처리와 고장 분류 모델을 하나로 연결합니다. |
| 26 | `m.fit(X.iloc[tr],y.iloc[tr]); pred=m.predict(X.iloc[te]); prob=m.predict_proba(X.iloc[te]); classes=m.classes_` | 학습 데이터로 모델을 학습합니다. |
| 27 | `metrics=pd.DataFrame(classification_report(y.iloc[te],pred,output_dict=True,zero_division=0)).T` | 클래스별 정밀도·재현율·F1을 요약합니다. |
| 28 | `matrix=pd.DataFrame(confusion_matrix(y.iloc[te],pred,labels=classes),index=[f"actual_{c}" for c in classes],columns=[f"pred_{c}" for c in classes])` | 실제 상태와 예측 상태의 조합을 표로 계산합니다. |
| 29 | `pred_df=sensor_df.iloc[te][["timestamp","equipment_id","operation_mode","fault_type"]].copy(); pred_df["predicted_fault"]=pred; pred_df["max_probability"]=prob.max(1); pred_df["review_required"]=pred_df["max_probability"]<.65` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `names=m.named_steps["preprocess"].get_feature_names_out(); imp=m.named_steps["classifier"].feature_importances_; importance=pd.DataFrame({"feature":names,"importance":imp}).sort_values("importance",ascending=False)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `with pd.ExcelWriter(OUTPUT_DIR/"ex220_fault_diagnosis_report.xlsx",engine="openpyxl") as w:` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `    metrics.to_excel(w,sheet_name="class_metrics"); matrix.to_excel(w,sheet_name="confusion_matrix"); pred_df.to_excel(w,sheet_name="predictions",index=False); importance.to_excel(w,sheet_name="feature_importance",index=False)` | 실제 상태와 예측 상태의 조합을 표로 계산합니다. |
| 33 | `print("보고서 저장 완료")` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 고장 라벨은 정비 이력과 어떤 규칙으로 연결되었는가?
2. 장비별 편차와 운전모드 차이를 모델이 구분하는가?
3. 고장 확률이 낮을 때 자동 정지보다 재검사가 적절한가?