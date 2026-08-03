# 실습 233 — rul_model_comparison

## 1. 학습 목표
여러 RUL 회귀 모델을 비교합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
Linear·RandomForest·GradientBoosting RUL 모델을 비교하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage12
python examples\ex233_rul_model_comparison.py
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
| 15 | `from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor` | 필요한 라이브러리나 모델을 불러옵니다. |
| 16 | `from sklearn.linear_model import LinearRegression` | 필요한 라이브러리나 모델을 불러옵니다. |
| 17 | `from sklearn.metrics import mean_absolute_error,r2_score` | 필요한 라이브러리나 모델을 불러옵니다. |
| 18 | `from sklearn.model_selection import GroupShuffleSplit` | 필요한 라이브러리나 모델을 불러옵니다. |
| 19 | `from sklearn.pipeline import Pipeline` | 필요한 라이브러리나 모델을 불러옵니다. |
| 20 | `from sklearn.preprocessing import StandardScaler` | 필요한 라이브러리나 모델을 불러옵니다. |
| 21 | `pm_df=pd.read_csv(DATA_FILE)` | 예지보전용 CSV를 DataFrame으로 읽습니다. |
| 22 | `features=["cycle","temperature_c","vibration_rms_g","motor_current_a","pressure_deviation","particle_count","health_index"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `X=pm_df[features]; y=pm_df["rul_cycles"]; groups=pm_df["equipment_id"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `tr,te=next(GroupShuffleSplit(n_splits=1,test_size=.25,random_state=42).split(X,y,groups))` | 학습과 평가 데이터를 분리합니다. |
| 25 | `models={"Linear":Pipeline([("scale",StandardScaler()),("regressor",LinearRegression())]),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `"RandomForest":RandomForestRegressor(n_estimators=300,random_state=42,n_jobs=-1),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `"GradientBoosting":GradientBoostingRegressor(n_estimators=250,learning_rate=.05,random_state=42)}` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `rows=[]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `for name,m in models.items():` | 여러 장비 또는 설정에 같은 작업을 반복합니다. |
| 30 | `    m.fit(X.iloc[tr],y.iloc[tr]); p=m.predict(X.iloc[te])` | 학습 데이터로 모델을 학습합니다. |
| 31 | `    rows.append({"model":name,"mae":mean_absolute_error(y.iloc[te],p),"r2":r2_score(y.iloc[te],p)})` | 예지보전 분석 단계를 수행합니다. |
| 32 | `out=pd.DataFrame(rows).sort_values("mae"); print(out.round(4)); out.to_csv(OUTPUT_DIR/"ex233_rul_model_comparison.csv",index=False,encoding="utf-8-sig")` | 결과를 CSV로 저장합니다. |

## 6. 실무 확인 질문
1. RUL 라벨은 실제 고장 또는 교체 시점과 어떻게 연결되었는가?
2. 장비 단위 데이터 누수를 방지했는가?
3. 정비 임계값은 비용과 안전을 함께 반영하는가?