# 실습 200 — automated_defect_decision_report

## 1. 학습 목표
사후요약·그룹비교·의사결정·LOT위험을 Excel 보고서로 생성합니다.

## 2. Antigravity용 하네스 프롬프트
```text
summary, recipe_rates, decision_analysis, lot_risk 네 시트를 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage10
python examples\ex200_automated_defect_decision_report.py
```

## 4. 예상 결과
요청한 베이지안 불량률 분석 결과가 출력 또는 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리를 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리를 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리를 불러옵니다. |
| 4 | `import pymc as pm` | 필요한 라이브러리를 불러옵니다. |
| 5 | `import arviz as az` | 필요한 라이브러리를 불러옵니다. |
| 6 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 7 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `DATA_FILE = ROOT / "data" / "bayesian_defect_rate_data.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 10 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 11 | `defect_df = pd.read_csv(DATA_FILE)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 12 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 13 | `g=defect_df.groupby("recipe")[["wafer_count","defect_count"]].sum().sort_index()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 14 | `with pm.Model(coords={"recipe":g.index.tolist()}) as model:` | PyMC 확률모형 범위를 시작합니다. |
| 15 | `    p=pm.Beta("p",1,1,dims="recipe")` | 0~1 확률용 베타 사전분포를 정의합니다. |
| 16 | `    pm.Binomial("d",n=g["wafer_count"],p=p,observed=g["defect_count"],dims="recipe")` | 불량 개수를 이항분포 관측값으로 연결합니다. |
| 17 | `    idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 18 | `summary=az.summary(idata,var_names=["p"],hdi_prob=.94)` | 사후요약과 MCMC 진단값을 계산합니다. |
| 19 | `means=idata.posterior["p"].mean(("chain","draw")).values` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `recipe_df=pd.DataFrame({"recipe":g.index,"posterior_mean":means})` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `overall_p=idata.posterior["p"].values.reshape(-1,len(g)).mean(axis=1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `keep=100*overall_p*200; inspect=250+100*overall_p*.65*200` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `decision=pd.DataFrame([{"expected_keep_cost":keep.mean(),"expected_inspect_cost":inspect.mean(),"p_inspection_better":(inspect<keep).mean()}])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `risk=defect_df[["lot_id","recipe","chamber_id","defect_rate"]].copy()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `risk["simple_risk_score"]=defect_df["temp_abs_deviation"]+defect_df["pressure_abs_deviation"]+defect_df["particle_mean"]/10` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `risk=risk.sort_values("simple_risk_score",ascending=False)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `with pd.ExcelWriter(OUTPUT_DIR/"ex200_defect_decision_report.xlsx",engine="openpyxl") as w:` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `    summary.to_excel(w,sheet_name="summary"); recipe_df.to_excel(w,sheet_name="recipe_rates",index=False); decision.to_excel(w,sheet_name="decision_analysis",index=False); risk.to_excel(w,sheet_name="lot_risk",index=False)` | 결과를 Excel 파일로 저장합니다. |
| 29 | `print("보고서 저장 완료")` | 계산 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 사전분포가 기존 품질 수준을 과도하게 반영하지 않는가?
2. 불량률 차이가 통계적으로뿐 아니라 비용 측면에서도 중요한가?
3. 모델 결과를 자동 정지 기준으로 사용할 때 어떤 안전장치가 필요한가?