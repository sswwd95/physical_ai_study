from pathlib import Path
import numpy as np
import pandas as pd
import pymc as pm
import arviz as az

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "bayesian_yield_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)
sensor_df = pd.read_csv(DATA_FILE)

codes,recipes=pd.factorize(sensor_df["recipe"],sort=True)
with pm.Model(coords={"recipe":recipes}) as model:
    mu_recipe=pm.Normal("mu_recipe",94,4,dims="recipe"); sigma=pm.HalfNormal("sigma",3)
    pm.Normal("y",mu_recipe[codes],sigma,observed=sensor_df["yield_percent"])
    idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)
    ppc=pm.sample_posterior_predictive(idata,random_seed=42,progressbar=False)
summary=az.summary(idata,var_names=["mu_recipe","sigma"],hdi_prob=0.94)
diag=pd.DataFrame([{"divergence_count":int(idata.sample_stats["diverging"].sum()),"max_rhat":float(summary["r_hat"].max())}])
means=idata.posterior["mu_recipe"].mean(("chain","draw")).values
recipe_df=pd.DataFrame({"recipe":recipes,"posterior_mean":means})
pred=ppc.posterior_predictive["y"].values.reshape(-1,len(sensor_df))
pred_df=pd.DataFrame({"lot_id":sensor_df["lot_id"].head(20),"actual":sensor_df["yield_percent"].head(20),"pred_mean":pred[:,:20].mean(0),"pred_p03":np.quantile(pred[:,:20],.03,axis=0),"pred_p97":np.quantile(pred[:,:20],.97,axis=0)})
with pd.ExcelWriter(OUTPUT_DIR/"ex180_bayesian_report.xlsx",engine="openpyxl") as w:
    summary.to_excel(w,sheet_name="summary"); diag.to_excel(w,sheet_name="diagnostics",index=False); recipe_df.to_excel(w,sheet_name="recipe_comparison",index=False); pred_df.to_excel(w,sheet_name="prediction_interval",index=False)
print("보고서 저장 완료")
