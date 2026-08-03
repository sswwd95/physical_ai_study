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
    nu_minus_one=pm.Exponential("nu_minus_one",1/10)
    nu=pm.Deterministic("nu",nu_minus_one+1)
    pm.StudentT("y",nu=nu,mu=mu,sigma=sigma,observed=obs)
    idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)
print(az.summary(idata,var_names=["mu","sigma","nu"]))
