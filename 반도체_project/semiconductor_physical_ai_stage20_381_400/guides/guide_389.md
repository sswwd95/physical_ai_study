# 실습 389 — model_registry

## 1. 학습 목표
세 모델과 메타데이터를 등록합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
수율·고장·RUL 모델과 특징·버전을 registry JSON으로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage20
python examples\ex389_model_registry.py
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
| 17 | `import joblib` | 필요한 라이브러리나 모델을 불러옵니다. |
| 18 | `from datetime import datetime` | 필요한 라이브러리나 모델을 불러옵니다. |
| 19 | `from sklearn.compose import ColumnTransformer` | 필요한 라이브러리나 모델을 불러옵니다. |
| 20 | `from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor,GradientBoostingRegressor` | 필요한 라이브러리나 모델을 불러옵니다. |
| 21 | `from sklearn.pipeline import Pipeline` | 필요한 라이브러리나 모델을 불러옵니다. |
| 22 | `from sklearn.preprocessing import OneHotEncoder` | 필요한 라이브러리나 모델을 불러옵니다. |
| 23 | `data=pd.read_csv(DATA_FILE)` | 종합 프로젝트 데이터를 읽습니다. |
| 24 | `features=["recipe","chamber_id","temperature_c","pressure_pa","vibration_rms_g","particle_count","rf_power_w","gas_flow_sccm","cycle_time_min","maintenance_age_hours"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `pre_sparse=ColumnTransformer([("num","passthrough",features[2:]),("cat",OneHotEncoder(handle_unknown="ignore"),features[:2])])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `pre_dense=ColumnTransformer([("num","passthrough",features[2:]),("cat",OneHotEncoder(handle_unknown="ignore",sparse_output=False),features[:2])])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `models={` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `    "yield":Pipeline([("preprocess",pre_sparse),("model",RandomForestRegressor(n_estimators=350,random_state=42,n_jobs=-1))]),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `    "fault":Pipeline([("preprocess",pre_sparse),("model",RandomForestClassifier(n_estimators=350,class_weight="balanced",random_state=42,n_jobs=-1))]),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `    "rul":Pipeline([("preprocess",pre_dense),("model",GradientBoostingRegressor(n_estimators=250,learning_rate=.05,random_state=42))])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `}` | 종합 프로젝트 통합 단계를 수행합니다. |
| 32 | `targets={"yield":"yield_percent","fault":"fault_flag","rul":"rul_cycles"}` | 계산 결과나 설정값을 변수에 저장합니다. |
| 33 | `version=datetime.now().strftime("%Y%m%d_%H%M%S")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 34 | `registry=[]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 35 | `for name,model in models.items():` | 여러 모델·지표·장비를 반복 처리합니다. |
| 36 | `    model.fit(data[features],data[targets[name]])` | 학습 데이터로 모델을 학습합니다. |
| 37 | `    file=MODEL_DIR/f"{name}_model_{version}.joblib"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 38 | `    joblib.dump(model,file)` | 학습된 모델을 파일로 저장합니다. |
| 39 | `    registry.append({"name":name,"version":version,"file":file.name,"target":targets[name],"features":features})` | 종합 프로젝트 통합 단계를 수행합니다. |
| 40 | `registry_file=MODEL_DIR/"model_registry.json"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 41 | `registry_file.write_text(json.dumps(registry,ensure_ascii=False,indent=2),encoding="utf-8")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `print(registry_file.read_text(encoding="utf-8"))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 요구사항과 구현·평가 결과가 추적 가능한가?
2. 데이터 누수·안전·운영 실패 시나리오를 검토했는가?
3. 포트폴리오에서 문제·해결·성과를 수치로 설명할 수 있는가?