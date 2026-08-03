from pathlib import Path
import numpy as np
import pandas as pd
import pymc as pm
import arviz as az

ROOT = Path(__file__).resolve().parents[1]
LIFE_FILE = ROOT / "data" / "bayesian_equipment_lifetime.csv"
RUL_FILE = ROOT / "data" / "bayesian_rul_snapshots.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

life_df = pd.read_csv(LIFE_FILE)
rul_df = pd.read_csv(RUL_FILE)

obs=life_df.loc[life_df["event_observed"]==1,"observed_cycles"].to_numpy()
models={}
with pm.Model() as exp_model:
    rate=pm.Exponential("rate",1/120); pm.Exponential("life",lam=rate,observed=obs)
    models["exponential"]=pm.sample(600,tune=600,chains=2,cores=1,random_seed=42,progressbar=False,idata_kwargs={"log_likelihood":True})
with pm.Model() as weib_model:
    alpha=pm.HalfNormal("alpha",3); beta=pm.HalfNormal("beta",150); pm.Weibull("life",alpha=alpha,beta=beta,observed=obs)
    models["weibull"]=pm.sample(600,tune=600,chains=2,cores=1,random_seed=42,progressbar=False,idata_kwargs={"log_likelihood":True})
print(az.compare(models))
