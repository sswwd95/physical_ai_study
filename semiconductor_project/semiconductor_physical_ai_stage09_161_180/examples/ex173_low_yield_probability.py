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

obs=sensor_df["yield_percent"].to_numpy()
with pm.Model() as model:
    mu=pm.Normal("mu",94,5); sigma=pm.HalfNormal("sigma",3)
    pm.Normal("y",mu,sigma,observed=obs)
    idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)
    ppc=pm.sample_posterior_predictive(idata,random_seed=42,progressbar=False)
print("P(y_new<92):",round((ppc.posterior_predictive["y"].values<92).mean(),4))
