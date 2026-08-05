# 실습 360 — automated_safety_report

## 1. 학습 목표
자동 안전 의사결정 Excel 보고서를 생성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
모델지표·혼동행렬·사건요약·의사결정 Excel 보고서를 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage18
python examples\ex360_automated_safety_report.py
```

## 4. 예상 결과
요청한 이상 대응·안전 의사결정 결과가 출력 또는 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리를 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리를 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리를 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "safety_decision_stream.csv"` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 이상 대응 또는 안전 의사결정 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError("data/safety_decision_stream.csv 파일이 없습니다.")` | 이상 대응 또는 안전 의사결정 단계를 수행합니다. |
| 12 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 13 | `from sklearn.ensemble import RandomForestClassifier` | 필요한 라이브러리를 불러옵니다. |
| 14 | `from sklearn.metrics import classification_report,confusion_matrix` | 필요한 라이브러리를 불러옵니다. |
| 15 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리를 불러옵니다. |
| 16 | `safe_df=pd.read_csv(DATA_FILE,parse_dates=["timestamp"])` | 안전 의사결정 센서 스트림을 읽습니다. |
| 17 | `features=["temperature_c","pressure_pa","vibration_rms_g","gas_flow_sccm","particle_count","door_closed","cooling_ok","vacuum_ok"]` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 18 | `X=safe_df[features]; y=safe_df["anomaly_type"].ne("normal").astype(int)` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 19 | `idx=np.arange(len(safe_df))` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 20 | `tr,te=train_test_split(idx,test_size=.25,random_state=42,stratify=y)` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 21 | `m=RandomForestClassifier(n_estimators=350,class_weight="balanced",random_state=42,n_jobs=-1)` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 22 | `m.fit(X.iloc[tr],y.iloc[tr]); pred=m.predict(X.iloc[te]); prob=m.predict_proba(X.iloc[te])[:,1]` | 과거 데이터로 위험 분류 모델을 학습합니다. |
| 23 | `metrics=pd.DataFrame(classification_report(y.iloc[te],pred,output_dict=True,zero_division=0)).T` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 24 | `matrix=pd.DataFrame(confusion_matrix(y.iloc[te],pred),index=["actual_normal","actual_anomaly"],columns=["pred_normal","pred_anomaly"])` | 실제 이상과 판단 결과를 혼동행렬로 계산합니다. |
| 25 | `decisions=safe_df.iloc[te][["timestamp","equipment_id","anomaly_type","severity_level"]].copy()` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 26 | `decisions["risk_probability"]=prob` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 27 | `decisions["action"]=np.select([prob>=.9,prob>=.7,prob>=.4],["STOP","SLOWDOWN","REINSPECT"],default="CONTINUE")` | 여러 안전 조건에 따라 행동을 선택합니다. |
| 28 | `incidents=safe_df.loc[safe_df["anomaly_type"].ne("normal")].groupby("anomaly_type").agg(count=("timestamp","count"),max_severity=("severity_level","max"))` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 29 | `with pd.ExcelWriter(OUTPUT_DIR/"ex360_safety_decision_report.xlsx",engine="openpyxl") as w:` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 30 | `    metrics.to_excel(w,sheet_name="model_metrics")` | 결과를 Excel 보고서로 저장합니다. |
| 31 | `    matrix.to_excel(w,sheet_name="confusion_matrix")` | 실제 이상과 판단 결과를 혼동행렬로 계산합니다. |
| 32 | `    incidents.to_excel(w,sheet_name="incident_summary")` | 결과를 Excel 보고서로 저장합니다. |
| 33 | `    decisions.to_excel(w,sheet_name="decisions",index=False)` | 결과를 Excel 보고서로 저장합니다. |
| 34 | `print("보고서 저장 완료")` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 자동 정지 조건이 안전 규정과 일치하는가?
2. 경보 미탐과 오탐의 비용을 별도로 평가했는가?
3. 센서 불확실성·통신지연·수동 개입 절차를 반영했는가?