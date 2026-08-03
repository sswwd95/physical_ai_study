# 실습 289 — pareto_front

## 1. 학습 목표
다목적 Pareto 후보를 계산합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
균일도 최대·불량률 최소·시간 최소 Pareto 후보를 계산하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage15
python examples\ex289_pareto_front.py
```

## 4. 예상 결과
요청한 공정 최적화·베이지안 의사결정 결과가 출력 또는 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 최적화 모델을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 최적화 모델을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 최적화 모델을 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 6 | `HISTORY_FILE = ROOT / "data" / "process_optimization_history.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `CANDIDATE_FILE = ROOT / "data" / "optimization_candidates.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 10 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 11 | `history_df = pd.read_csv(HISTORY_FILE)` | 과거 공정 기록 또는 후보 조건 CSV를 읽습니다. |
| 12 | `candidate_df = pd.read_csv(CANDIDATE_FILE)` | 과거 공정 기록 또는 후보 조건 CSV를 읽습니다. |
| 13 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 14 | `from sklearn.compose import ColumnTransformer` | 필요한 라이브러리나 최적화 모델을 불러옵니다. |
| 15 | `from sklearn.ensemble import RandomForestRegressor` | 필요한 라이브러리나 최적화 모델을 불러옵니다. |
| 16 | `from sklearn.pipeline import Pipeline` | 필요한 라이브러리나 최적화 모델을 불러옵니다. |
| 17 | `from sklearn.preprocessing import OneHotEncoder` | 필요한 라이브러리나 최적화 모델을 불러옵니다. |
| 18 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 19 | `features=["recipe","chamber_id","pressure_pa","rf_power_w","gas_flow_sccm","temperature_c"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `numeric=features[2:]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `categorical=features[:2]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 23 | `preprocessor=ColumnTransformer([` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `    ("num","passthrough",numeric),` | 공정 최적화 또는 베이지안 의사결정 단계를 수행합니다. |
| 25 | `    ("cat",OneHotEncoder(handle_unknown="ignore"),categorical)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `])` | 공정 최적화 또는 베이지안 의사결정 단계를 수행합니다. |
| 27 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 28 | `def make_model(seed=42):` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `    return Pipeline([` | 전처리와 예측 모델을 하나로 연결합니다. |
| 30 | `        ("preprocess",preprocessor),` | 공정 최적화 또는 베이지안 의사결정 단계를 수행합니다. |
| 31 | `        ("regressor",RandomForestRegressor(` | 공정 최적화 또는 베이지안 의사결정 단계를 수행합니다. |
| 32 | `            n_estimators=300,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 33 | `            max_depth=14,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 34 | `            min_samples_leaf=3,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 35 | `            random_state=seed,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 36 | `            n_jobs=-1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 37 | `        ))` | 공정 최적화 또는 베이지안 의사결정 단계를 수행합니다. |
| 38 | `    ])` | 공정 최적화 또는 베이지안 의사결정 단계를 수행합니다. |
| 39 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 40 | `for target in ["uniformity_percent","defect_rate","cycle_time_min"]:` | 여러 후보나 가중치 조합을 반복 계산합니다. |
| 41 | `    m=make_model(); m.fit(history_df[features],history_df[target])` | 과거 공정 데이터로 대리모델을 학습합니다. |
| 42 | `    candidate_df[target]=m.predict(candidate_df[features])` | 후보 공정 조건의 품질·불량률·시간을 예측합니다. |
| 43 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 44 | `values=candidate_df[["uniformity_percent","defect_rate","cycle_time_min"]].to_numpy()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 45 | `is_pareto=np.ones(len(values),dtype=bool)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 46 | `for i,v in enumerate(values):` | 여러 후보나 가중치 조합을 반복 계산합니다. |
| 47 | `    dominates=(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 48 | `        (values[:,0]>=v[0])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 49 | `        & (values[:,1]<=v[1])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 50 | `        & (values[:,2]<=v[2])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 51 | `        & ((values[:,0]>v[0]) \| (values[:,1]<v[1]) \| (values[:,2]<v[2]))` | 공정 최적화 또는 베이지안 의사결정 단계를 수행합니다. |
| 52 | `    )` | 공정 최적화 또는 베이지안 의사결정 단계를 수행합니다. |
| 53 | `    if dominates.any():` | 공정 최적화 또는 베이지안 의사결정 단계를 수행합니다. |
| 54 | `        is_pareto[i]=False` | 계산 결과나 설정값을 변수에 저장합니다. |
| 55 | `out=candidate_df.loc[is_pareto].copy()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 56 | `print("Pareto 후보:",len(out))` | 결과를 콘솔에 출력합니다. |
| 57 | `out.to_csv(OUTPUT_DIR/"ex289_pareto_front.csv",index=False,encoding="utf-8-sig")` | 추천 결과를 CSV로 저장합니다. |

## 6. 실무 확인 질문
1. 목적함수와 제약조건이 실제 품질·안전 기준을 반영하는가?
2. 추천 조건이 과거 운전 범위를 벗어나지 않는가?
3. 최적 조건을 바로 양산에 적용하지 않고 확인 실험을 거치는가?