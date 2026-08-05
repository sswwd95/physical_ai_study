from pathlib import Path
import numpy as np
import pandas as pd
import pymc as pm
import arviz as az

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "bayesian_process_experiment.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

experiment_df = pd.read_csv(DATA_FILE)

codes,recipes=pd.factorize(experiment_df["recipe"],sort=True)
with pm.Model(coords={"recipe":recipes}) as model:
    mu=pm.Normal("mu",95,3,dims="recipe"); sigma=pm.HalfNormal("sigma",2)
    pm.Normal("y",mu[codes],sigma,observed=experiment_df["uniformity_percent"])
    idata=pm.sample(900,tune=900,chains=2,cores=1,random_seed=42,progressbar=False)
arr=idata.posterior["mu"].stack(sample=("chain","draw")).values
rows=[]
for i in range(len(recipes)):
    for j in range(i+1,len(recipes)):
        d=arr[i]-arr[j]
        rows.append({"condition_a":recipes[i],"condition_b":recipes[j],"p_a_better":float((d>0).mean()),"mean_difference":float(d.mean())})
out=pd.DataFrame(rows)
print(out.round(4)); out.to_csv(OUTPUT_DIR/"ex265_pairwise_superiority.csv",index=False,encoding="utf-8-sig")
