from pathlib import Path
import numpy as np
import pandas as pd
import pymc as pm
import arviz as az

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "bayesian_defect_rate_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)
defect_df = pd.read_csv(DATA_FILE)

g=defect_df.groupby("recipe")[["wafer_count","defect_count"]].sum().sort_index()
with pm.Model(coords={"recipe":g.index.tolist()}) as model:
    p=pm.Beta("p",1,1,dims="recipe")
    pm.Binomial("d",n=g["wafer_count"],p=p,observed=g["defect_count"],dims="recipe")
    idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)
summary=az.summary(idata,var_names=["p"],hdi_prob=.94)
means=idata.posterior["p"].mean(("chain","draw")).values
recipe_df=pd.DataFrame({"recipe":g.index,"posterior_mean":means})
overall_p=idata.posterior["p"].values.reshape(-1,len(g)).mean(axis=1)
keep=100*overall_p*200; inspect=250+100*overall_p*.65*200
decision=pd.DataFrame([{"expected_keep_cost":keep.mean(),"expected_inspect_cost":inspect.mean(),"p_inspection_better":(inspect<keep).mean()}])
risk=defect_df[["lot_id","recipe","chamber_id","defect_rate"]].copy()
risk["simple_risk_score"]=defect_df["temp_abs_deviation"]+defect_df["pressure_abs_deviation"]+defect_df["particle_mean"]/10
risk=risk.sort_values("simple_risk_score",ascending=False)
with pd.ExcelWriter(OUTPUT_DIR/"ex200_defect_decision_report.xlsx",engine="openpyxl") as w:
    summary.to_excel(w,sheet_name="summary"); recipe_df.to_excel(w,sheet_name="recipe_rates",index=False); decision.to_excel(w,sheet_name="decision_analysis",index=False); risk.to_excel(w,sheet_name="lot_risk",index=False)
print("보고서 저장 완료")
