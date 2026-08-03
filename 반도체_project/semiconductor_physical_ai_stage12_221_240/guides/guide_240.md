# 실습 240 — automated_pm_report

## 1. 학습 목표
자동 예지보전 Excel 보고서를 생성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
분류·회귀 성능, 예측, 정비 우선순위 Excel 보고서를 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage12
python examples\ex240_automated_pm_report.py
```

## 4. 예상 결과
요청한 예지보전 분석 결과가 출력 또는 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 모델을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 모델을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 모델을 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "predictive_maintenance_rul.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 예지보전 분석 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError(` | 예지보전 분석 단계를 수행합니다. |
| 12 | `        "data/predictive_maintenance_rul.csv 파일이 없습니다."` | 예지보전 분석 단계를 수행합니다. |
| 13 | `    )` | 예지보전 분석 단계를 수행합니다. |
| 14 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 15 | `from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor` | 필요한 라이브러리나 모델을 불러옵니다. |
| 16 | `from sklearn.metrics import classification_report,mean_absolute_error,r2_score` | 필요한 라이브러리나 모델을 불러옵니다. |
| 17 | `from sklearn.model_selection import GroupShuffleSplit` | 필요한 라이브러리나 모델을 불러옵니다. |
| 18 | `pm_df=pd.read_csv(DATA_FILE)` | 예지보전용 CSV를 DataFrame으로 읽습니다. |
| 19 | `features=["cycle","temperature_c","vibration_rms_g","motor_current_a","pressure_deviation","particle_count","health_index"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `X=pm_df[features]; groups=pm_df["equipment_id"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `tr,te=next(GroupShuffleSplit(n_splits=1,test_size=.25,random_state=42).split(X,pm_df["rul_cycles"],groups))` | 학습과 평가 데이터를 분리합니다. |
| 22 | `clf=RandomForestClassifier(n_estimators=300,class_weight="balanced",random_state=42,n_jobs=-1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `clf.fit(X.iloc[tr],pm_df["failure_within_20"].iloc[tr]); cp=clf.predict(X.iloc[te]); cprob=clf.predict_proba(X.iloc[te])[:,1]` | 학습 데이터로 모델을 학습합니다. |
| 24 | `reg=RandomForestRegressor(n_estimators=350,random_state=42,n_jobs=-1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `reg.fit(X.iloc[tr],pm_df["rul_cycles"].iloc[tr]); rp=reg.predict(X.iloc[te])` | 학습 데이터로 모델을 학습합니다. |
| 26 | `class_metrics=pd.DataFrame(classification_report(pm_df["failure_within_20"].iloc[te],cp,output_dict=True,zero_division=0)).T` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `reg_metrics=pd.DataFrame([{"mae":mean_absolute_error(pm_df["rul_cycles"].iloc[te],rp),"r2":r2_score(pm_df["rul_cycles"].iloc[te],rp)}])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `pred=pm_df.iloc[te][["equipment_id","cycle","health_index","rul_cycles","failure_within_20"]].copy(); pred["predicted_rul"]=rp; pred["failure_probability"]=cprob` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `latest=pm_df.sort_values("cycle").groupby("equipment_id").tail(1).copy(); latest["priority_score"]=(1-latest["health_index"])*50+(20-latest["rul_cycles"]).clip(lower=0)*2` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `with pd.ExcelWriter(OUTPUT_DIR/"ex240_predictive_maintenance_report.xlsx",engine="openpyxl") as w:` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `    class_metrics.to_excel(w,sheet_name="classification_metrics"); reg_metrics.to_excel(w,sheet_name="regression_metrics",index=False); pred.to_excel(w,sheet_name="predictions",index=False); latest.to_excel(w,sheet_name="maintenance_priority",index=False)` | 결과를 Excel 보고서로 저장합니다. |
| 32 | `print("보고서 저장 완료")` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. RUL 라벨은 실제 고장 또는 교체 시점과 어떻게 연결되었는가?
2. 장비 단위 데이터 누수를 방지했는가?
3. 정비 임계값은 비용과 안전을 함께 반영하는가?