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
c=experiment_df.loc[experiment_df["recipe"]=="ETCH-C","uniformity_percent"].to_numpy()
with pm.Model() as model:
    mu_a=pm.Normal("mu_a",95,3); mu_c=pm.Normal("mu_c",95,3)
    sigma=pm.HalfNormal("sigma",2)
    effect=pm.Deterministic("effect",(mu_a-mu_c)/sigma)
    pm.Normal("a",mu_a,sigma,observed=a); pm.Normal("c",mu_c,sigma,observed=c)
    idata=pm.sample(900,tune=900,chains=2,cores=1,random_seed=42,progressbar=False)
s=idata.posterior["effect"].values.ravel()
print("표준화 효과크기:",round(s.mean(),4))
print("P(|effect|<0.1):",round((np.abs(s)<.1).mean(),4))
print("94% HDI:",az.hdi(s,hdi_prob=.94))
