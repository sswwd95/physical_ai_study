# 실습 300 — automated_optimization_report

## 1. 학습 목표
자동 공정 최적화 Excel 보고서를 생성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
후보예측·추천·확인실험·특징중요도 Excel 보고서를 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage15
python examples\ex300_automated_optimization_report.py
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
| 40 | `models={}` | 계산 결과나 설정값을 변수에 저장합니다. |
| 41 | `for target in ["uniformity_percent","defect_rate","cycle_time_min"]:` | 여러 후보나 가중치 조합을 반복 계산합니다. |
| 42 | `    m=make_model(); m.fit(history_df[features],history_df[target]); models[target]=m` | 과거 공정 데이터로 대리모델을 학습합니다. |
| 43 | `    candidate_df[f"predicted_{target}"]=m.predict(candidate_df[features])` | 후보 공정 조건의 품질·불량률·시간을 예측합니다. |
| 44 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 45 | `def z(s):` | 공정 최적화 또는 베이지안 의사결정 단계를 수행합니다. |
| 46 | `    return (s-s.mean())/s.std()` | 공정 최적화 또는 베이지안 의사결정 단계를 수행합니다. |
| 47 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 48 | `candidate_df["utility"]=(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 49 | `    .55*z(candidate_df["predicted_uniformity_percent"])` | 공정 최적화 또는 베이지안 의사결정 단계를 수행합니다. |
| 50 | `    -.30*z(candidate_df["predicted_defect_rate"])` | 공정 최적화 또는 베이지안 의사결정 단계를 수행합니다. |
| 51 | `    -.15*z(candidate_df["predicted_cycle_time_min"])` | 공정 최적화 또는 베이지안 의사결정 단계를 수행합니다. |
| 52 | `)` | 공정 최적화 또는 베이지안 의사결정 단계를 수행합니다. |
| 53 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 54 | `safe=candidate_df.loc[` | 계산 결과나 설정값을 변수에 저장합니다. |
| 55 | `    (candidate_df["predicted_defect_rate"]<.04)` | 공정 최적화 또는 베이지안 의사결정 단계를 수행합니다. |
| 56 | `    & (candidate_df["predicted_uniformity_percent"]>96)` | 공정 최적화 또는 베이지안 의사결정 단계를 수행합니다. |
| 57 | `].copy()` | 공정 최적화 또는 베이지안 의사결정 단계를 수행합니다. |
| 58 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 59 | `recommendation=safe.sort_values("utility",ascending=False).head(20)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 60 | `confirmation=pd.concat(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 61 | `    [recommendation.head(5).assign(replicate=i+1) for i in range(3)],` | 계산 결과나 설정값을 변수에 저장합니다. |
| 62 | `    ignore_index=True` | 계산 결과나 설정값을 변수에 저장합니다. |
| 63 | `)` | 공정 최적화 또는 베이지안 의사결정 단계를 수행합니다. |
| 64 | `confirmation["random_order"]=np.random.default_rng(42).permutation(np.arange(1,len(confirmation)+1))` | 계산 결과나 설정값을 변수에 저장합니다. |
| 65 | `feature_importance=[]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 66 | `for target,m in models.items():` | 여러 후보나 가중치 조합을 반복 계산합니다. |
| 67 | `    names=m.named_steps["preprocess"].get_feature_names_out()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 68 | `    imp=m.named_steps["regressor"].feature_importances_` | 계산 결과나 설정값을 변수에 저장합니다. |
| 69 | `    feature_importance.extend(` | 공정 최적화 또는 베이지안 의사결정 단계를 수행합니다. |
| 70 | `        {"target":target,"feature":name,"importance":value}` | 공정 최적화 또는 베이지안 의사결정 단계를 수행합니다. |
| 71 | `        for name,value in zip(names,imp)` | 여러 후보나 가중치 조합을 반복 계산합니다. |
| 72 | `    )` | 공정 최적화 또는 베이지안 의사결정 단계를 수행합니다. |
| 73 | `importance_df=pd.DataFrame(feature_importance)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 74 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 75 | `with pd.ExcelWriter(OUTPUT_DIR/"ex300_process_optimization_report.xlsx",engine="openpyxl") as w:` | 계산 결과나 설정값을 변수에 저장합니다. |
| 76 | `    candidate_df.to_excel(w,sheet_name="candidate_predictions",index=False)` | 최적화 보고서를 Excel로 저장합니다. |
| 77 | `    recommendation.to_excel(w,sheet_name="recommendation",index=False)` | 최적화 보고서를 Excel로 저장합니다. |
| 78 | `    confirmation.to_excel(w,sheet_name="confirmation_plan",index=False)` | 최적화 보고서를 Excel로 저장합니다. |
| 79 | `    importance_df.to_excel(w,sheet_name="feature_importance",index=False)` | 최적화 보고서를 Excel로 저장합니다. |
| 80 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 81 | `print("보고서 저장 완료")` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 목적함수와 제약조건이 실제 품질·안전 기준을 반영하는가?
2. 추천 조건이 과거 운전 범위를 벗어나지 않는가?
3. 최적 조건을 바로 양산에 적용하지 않고 확인 실험을 거치는가?