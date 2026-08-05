# 실습 180 — automated_bayesian_report

## 1. 학습 목표
사후요약·진단·예측·그룹비교를 Excel 보고서로 생성합니다.

## 2. Antigravity용 하네스 프롬프트
```text
summary, diagnostics, recipe_comparison, prediction_interval 네 시트를 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage09
python examples\ex180_automated_bayesian_report.py
```

## 4. 예상 결과
요청한 베이지안 결과와 진단 자료가 출력 또는 저장됩니다.

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
| 8 | `DATA_FILE = ROOT / "data" / "bayesian_yield_data.csv"` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 9 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 10 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 11 | `sensor_df = pd.read_csv(DATA_FILE)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 12 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 13 | `codes,recipes=pd.factorize(sensor_df["recipe"],sort=True)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 14 | `with pm.Model(coords={"recipe":recipes}) as model:` | PyMC 확률모형의 범위를 시작합니다. |
| 15 | `    mu_recipe=pm.Normal("mu_recipe",94,4,dims="recipe"); sigma=pm.HalfNormal("sigma",3)` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 16 | `    pm.Normal("y",mu_recipe[codes],sigma,observed=sensor_df["yield_percent"])` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 17 | `    idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 18 | `    ppc=pm.sample_posterior_predictive(idata,random_seed=42,progressbar=False)` | 사후분포에서 새로운 관측값을 생성합니다. |
| 19 | `summary=az.summary(idata,var_names=["mu_recipe","sigma"],hdi_prob=0.94)` | 사후 평균, HDI, R-hat, 유효표본크기를 요약합니다. |
| 20 | `diag=pd.DataFrame([{"divergence_count":int(idata.sample_stats["diverging"].sum()),"max_rhat":float(summary["r_hat"].max())}])` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 21 | `means=idata.posterior["mu_recipe"].mean(("chain","draw")).values` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 22 | `recipe_df=pd.DataFrame({"recipe":recipes,"posterior_mean":means})` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 23 | `pred=ppc.posterior_predictive["y"].values.reshape(-1,len(sensor_df))` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 24 | `pred_df=pd.DataFrame({"lot_id":sensor_df["lot_id"].head(20),"actual":sensor_df["yield_percent"].head(20),"pred_mean":pred[:,:20].mean(0),"pred_p03":np.quantile(pred[:,:20],.03,axis=0),"pred_p97":np.quantile(pred[:,:20],.97,axis=0)})` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 25 | `with pd.ExcelWriter(OUTPUT_DIR/"ex180_bayesian_report.xlsx",engine="openpyxl") as w:` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 26 | `    summary.to_excel(w,sheet_name="summary"); diag.to_excel(w,sheet_name="diagnostics",index=False); recipe_df.to_excel(w,sheet_name="recipe_comparison",index=False); pred_df.to_excel(w,sheet_name="prediction_interval",index=False)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 27 | `print("보고서 저장 완료")` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 사전분포가 실제 공정 지식과 일치하는가?
2. R-hat과 유효표본크기가 충분한가?
3. 점 추정 대신 HDI와 사후예측분포를 함께 전달했는가?