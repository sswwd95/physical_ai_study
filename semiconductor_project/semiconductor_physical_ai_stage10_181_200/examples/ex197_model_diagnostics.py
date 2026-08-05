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

codes,recipes=pd.factorize(defect_df["recipe"],sort=True)
with pm.Model(coords={"recipe":recipes}) as model:
    a=pm.Normal("a",-3,1); tau=pm.HalfNormal("tau",1); z=pm.Normal("z",0,1,dims="recipe")
    p=pm.math.sigmoid(a+z[codes]*tau)
    pm.Binomial("d",n=defect_df["wafer_count"],p=p,observed=defect_df["defect_count"])
    idata=pm.sample(800,tune=800,chains=2,cores=1,target_accept=.9,random_seed=42,progressbar=False)
summary=az.summary(idata,var_names=["a","tau","z"]); div=int(idata.sample_stats["diverging"].sum())
print(summary); print("divergence:",div); summary.assign(divergence_count=div).to_csv(OUTPUT_DIR/"ex197_diagnostics.csv",encoding="utf-8-sig")
