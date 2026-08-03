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

a=experiment_df.loc[experiment_df["recipe"]=="ETCH-A","uniformity_percent"].to_numpy()
first=a[:len(a)//2]; second=a
rows=[]
for name,data in [("phase1",first),("phase1_plus_phase2",second)]:
    with pm.Model() as model:
        mu=pm.Normal("mu",95,3); sigma=pm.HalfNormal("sigma",2)
        pm.Normal("y",mu,sigma,observed=data)
        idata=pm.sample(700,tune=700,chains=2,cores=1,random_seed=42,progressbar=False)
    s=idata.posterior["mu"].values.ravel()
    h=az.hdi(s,hdi_prob=.94)
    rows.append({"phase":name,"posterior_mean":s.mean(),"hdi_low":h[0],"hdi_high":h[1]})
out=pd.DataFrame(rows)
print(out.round(4))
