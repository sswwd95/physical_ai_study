# 실습 280 — automated_bayesian_experiment_report

## 1. 학습 목표
조건 비교·우월확률·효용·추천 Excel 보고서를 생성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
조건 비교·우월확률·효용·추천 Excel 보고서를 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage14
python examples\ex280_automated_bayesian_experiment_report.py
```

## 4. 예상 결과
요청한 베이지안 실험분석 결과가 출력 또는 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리를 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리를 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리를 불러옵니다. |
| 4 | `import pymc as pm` | 필요한 라이브러리를 불러옵니다. |
| 5 | `import arviz as az` | 필요한 라이브러리를 불러옵니다. |
| 6 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 7 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 8 | `DATA_FILE = ROOT / "data" / "bayesian_process_experiment.csv"` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 9 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 10 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 11 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 12 | `experiment_df = pd.read_csv(DATA_FILE)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 13 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 14 | `group=experiment_df.groupby(["recipe","pressure_level","rf_level"]).agg(` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 15 | `    uniformity_mean=("uniformity_percent","mean"),` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 16 | `    defect_rate_mean=("defect_rate","mean"),` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 17 | `    etch_rate_mean=("etch_rate_nm_min","mean"),` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 18 | `    n=("lot_id","count")` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 19 | `).reset_index()` | 베이지안 실험분석 단계를 수행합니다. |
| 20 | `group["utility"]=(` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 21 | `    0.5*(group["uniformity_mean"]-group["uniformity_mean"].mean())/group["uniformity_mean"].std()` | 베이지안 실험분석 단계를 수행합니다. |
| 22 | `    -0.35*(group["defect_rate_mean"]-group["defect_rate_mean"].mean())/group["defect_rate_mean"].std()` | 베이지안 실험분석 단계를 수행합니다. |
| 23 | `    +0.15*(group["etch_rate_mean"]-group["etch_rate_mean"].mean())/group["etch_rate_mean"].std()` | 베이지안 실험분석 단계를 수행합니다. |
| 24 | `)` | 베이지안 실험분석 단계를 수행합니다. |
| 25 | `group=group.sort_values("utility",ascending=False)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 26 | `recipe_summary=experiment_df.groupby("recipe")[["uniformity_percent","defect_rate","etch_rate_nm_min"]].mean()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 27 | `pairwise=[]` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 28 | `for a in ["ETCH-A","ETCH-B","ETCH-C"]:` | 여러 조건이나 그룹을 반복 분석합니다. |
| 29 | `    for b in ["ETCH-A","ETCH-B","ETCH-C"]:` | 여러 조건이나 그룹을 반복 분석합니다. |
| 30 | `        if a<b:` | 베이지안 실험분석 단계를 수행합니다. |
| 31 | `            da=experiment_df.loc[experiment_df["recipe"]==a,"uniformity_percent"].to_numpy()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 32 | `            db=experiment_df.loc[experiment_df["recipe"]==b,"uniformity_percent"].to_numpy()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 33 | `            draws_a=np.random.default_rng(42).normal(da.mean(),da.std()/np.sqrt(len(da)),4000)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 34 | `            draws_b=np.random.default_rng(43).normal(db.mean(),db.std()/np.sqrt(len(db)),4000)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 35 | `            pairwise.append({"a":a,"b":b,"p_a_better":float((draws_a>draws_b).mean()),"mean_difference":float(draws_a.mean()-draws_b.mean())})` | 베이지안 실험분석 단계를 수행합니다. |
| 36 | `pairwise_df=pd.DataFrame(pairwise)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 37 | `recommendation=group.head(10).copy()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 38 | `with pd.ExcelWriter(OUTPUT_DIR/"ex280_bayesian_experiment_report.xlsx",engine="openpyxl") as w:` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 39 | `    recipe_summary.to_excel(w,sheet_name="recipe_summary")` | 결과를 Excel 보고서로 저장합니다. |
| 40 | `    pairwise_df.to_excel(w,sheet_name="pairwise_probability",index=False)` | 결과를 Excel 보고서로 저장합니다. |
| 41 | `    group.to_excel(w,sheet_name="condition_utility",index=False)` | 결과를 Excel 보고서로 저장합니다. |
| 42 | `    recommendation.to_excel(w,sheet_name="recommendation",index=False)` | 결과를 Excel 보고서로 저장합니다. |
| 43 | `print("보고서 저장 완료")` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 실험 조건이 무작위화·반복·블로킹 원칙을 만족하는가?
2. 통계적 우월성과 공정상 의미 있는 효과크기를 구분했는가?
3. 최적 조건 선정 시 수율·불량률·안전·원가를 함께 고려했는가?