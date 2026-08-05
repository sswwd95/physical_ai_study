# 실습 388 — rul_model_training

## 1. 학습 목표
RUL 예측 모델을 학습·평가합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
GradientBoosting 기반 RUL 예측 모델을 작성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage20
python examples\ex388_rul_model_training.py
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
| 17 | `from sklearn.compose import ColumnTransformer` | 필요한 라이브러리나 모델을 불러옵니다. |
| 18 | `from sklearn.ensemble import GradientBoostingRegressor` | 필요한 라이브러리나 모델을 불러옵니다. |
| 19 | `from sklearn.metrics import mean_absolute_error,r2_score` | 필요한 라이브러리나 모델을 불러옵니다. |
| 20 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리나 모델을 불러옵니다. |
| 21 | `from sklearn.pipeline import Pipeline` | 필요한 라이브러리나 모델을 불러옵니다. |
| 22 | `from sklearn.preprocessing import OneHotEncoder` | 필요한 라이브러리나 모델을 불러옵니다. |
| 23 | `data=pd.read_csv(DATA_FILE)` | 종합 프로젝트 데이터를 읽습니다. |
| 24 | `features=["recipe","chamber_id","temperature_c","pressure_pa","vibration_rms_g","particle_count","rf_power_w","gas_flow_sccm","cycle_time_min","maintenance_age_hours"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `X=data[features]; y=data["rul_cycles"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=42)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `pre=ColumnTransformer([("num","passthrough",features[2:]),("cat",OneHotEncoder(handle_unknown="ignore",sparse_output=False),features[:2])])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `model=Pipeline([("preprocess",pre),("regressor",GradientBoostingRegressor(n_estimators=250,learning_rate=.05,random_state=42))])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `model.fit(Xtr,ytr); pred=model.predict(Xte)` | 학습 데이터로 모델을 학습합니다. |
| 30 | `print({"mae":mean_absolute_error(yte,pred),"r2":r2_score(yte,pred)})` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 요구사항과 구현·평가 결과가 추적 가능한가?
2. 데이터 누수·안전·운영 실패 시나리오를 검토했는가?
3. 포트폴리오에서 문제·해결·성과를 수치로 설명할 수 있는가?