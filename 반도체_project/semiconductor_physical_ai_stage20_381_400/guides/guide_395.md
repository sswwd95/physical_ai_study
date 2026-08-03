# 실습 395 — kpi_scorecard

## 1. 학습 목표
프로젝트 KPI 스코어카드를 생성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
수율 MAE·R², 고장 Recall, RUL MAE KPI 스코어카드를 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage20
python examples\ex395_kpi_scorecard.py
```

## 4. 예상 결과
요청한 종합 프로젝트·포트폴리오 산출물이 생성됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 모델을 불러옵니다. |
| 2 | `import json` | 필요한 라이브러리나 모델을 불러옵니다. |
| 3 | `import numpy as np` | 필요한 라이브러리나 모델을 불러옵니다. |
| 4 | `import pandas as pd` | 필요한 라이브러리나 모델을 불러옵니다. |
| 5 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 6 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `DATA_FILE = ROOT / "data" / "final_project_data.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `CONFIG_FILE = ROOT / "config" / "project_config.json"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 10 | `MODEL_DIR = ROOT / "models"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 11 | `REPORT_DIR = ROOT / "reports"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 12 | `PORTFOLIO_DIR = ROOT / "portfolio"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 13 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 14 | `for directory in [OUTPUT_DIR, MODEL_DIR, REPORT_DIR, PORTFOLIO_DIR]:` | 여러 모델·지표·장비를 반복 처리합니다. |
| 15 | `    directory.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 16 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 17 | `from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor` | 필요한 라이브러리나 모델을 불러옵니다. |
| 18 | `from sklearn.metrics import mean_absolute_error,recall_score,r2_score` | 필요한 라이브러리나 모델을 불러옵니다. |
| 19 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리나 모델을 불러옵니다. |
| 20 | `data=pd.read_csv(DATA_FILE)` | 종합 프로젝트 데이터를 읽습니다. |
| 21 | `features=["temperature_c","pressure_pa","vibration_rms_g","particle_count","rf_power_w","gas_flow_sccm","cycle_time_min","maintenance_age_hours"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `X=data[features]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `tr,te=train_test_split(np.arange(len(data)),test_size=.25,random_state=42,stratify=data["fault_flag"])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `yield_model=RandomForestRegressor(n_estimators=250,random_state=42,n_jobs=-1).fit(X.iloc[tr],data["yield_percent"].iloc[tr])` | 학습 데이터로 모델을 학습합니다. |
| 25 | `fault_model=RandomForestClassifier(n_estimators=250,class_weight="balanced",random_state=42,n_jobs=-1).fit(X.iloc[tr],data["fault_flag"].iloc[tr])` | 학습 데이터로 모델을 학습합니다. |
| 26 | `rul_model=RandomForestRegressor(n_estimators=250,random_state=42,n_jobs=-1).fit(X.iloc[tr],data["rul_cycles"].iloc[tr])` | 학습 데이터로 모델을 학습합니다. |
| 27 | `yp=yield_model.predict(X.iloc[te]); fp=fault_model.predict(X.iloc[te]); rp=rul_model.predict(X.iloc[te])` | 수율·고장·RUL 예측값을 계산합니다. |
| 28 | `scorecard=pd.DataFrame([` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `    {"kpi":"yield_mae","value":mean_absolute_error(data["yield_percent"].iloc[te],yp),"target":1.5},` | 종합 프로젝트 통합 단계를 수행합니다. |
| 30 | `    {"kpi":"yield_r2","value":r2_score(data["yield_percent"].iloc[te],yp),"target":.7},` | 종합 프로젝트 통합 단계를 수행합니다. |
| 31 | `    {"kpi":"fault_recall","value":recall_score(data["fault_flag"].iloc[te],fp,zero_division=0),"target":.8},` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `    {"kpi":"rul_mae","value":mean_absolute_error(data["rul_cycles"].iloc[te],rp),"target":20.0},` | 종합 프로젝트 통합 단계를 수행합니다. |
| 33 | `])` | 종합 프로젝트 통합 단계를 수행합니다. |
| 34 | `scorecard["passed"]=np.where(scorecard["kpi"].str.contains("mae"),scorecard["value"]<=scorecard["target"],scorecard["value"]>=scorecard["target"])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 35 | `print(scorecard.round(4))` | 결과를 콘솔에 출력합니다. |
| 36 | `scorecard.to_csv(REPORT_DIR/"kpi_scorecard.csv",index=False,encoding="utf-8-sig")` | 결과를 CSV로 저장합니다. |

## 6. 실무 확인 질문
1. 요구사항과 구현·평가 결과가 추적 가능한가?
2. 데이터 누수·안전·운영 실패 시나리오를 검토했는가?
3. 포트폴리오에서 문제·해결·성과를 수치로 설명할 수 있는가?