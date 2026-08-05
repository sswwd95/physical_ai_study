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

data = experiment_df.loc[experiment_df["recipe"].isin(["ETCH-A","ETCH-B"])]
a = data.loc[data["recipe"]=="ETCH-A","uniformity_percent"].to_numpy()
b = data.loc[data["recipe"]=="ETCH-B","uniformity_percent"].to_numpy()
with pm.Model() as model:
    mu_a=pm.Normal("mu_a",95,3); mu_b=pm.Normal("mu_b",95,3)
    sigma_a=pm.HalfNormal("sigma_a",2); sigma_b=pm.HalfNormal("sigma_b",2)
    diff=pm.Deterministic("diff",mu_a-mu_b)
    pm.Normal("y_a",mu_a,sigma_a,observed=a)
    pm.Normal("y_b",mu_b,sigma_b,observed=b)
    idata=pm.sample(1000,tune=1000,chains=2,cores=1,random_seed=42,progressbar=False)
s=idata.posterior["diff"].values.ravel()
print("평균 차이:",round(s.mean(),4))
print("P(A>B):",round((s>0).mean(),4))
print("94% HDI:",az.hdi(s,hdi_prob=.94))
