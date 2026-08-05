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

x=(sensor_df["particle_mean"]-sensor_df["particle_mean"].mean())/sensor_df["particle_mean"].std()
with pm.Model() as model:
    a=pm.Normal("a",94,5); b=pm.Normal("b",0,2); s=pm.HalfNormal("s",3)
    mu=a+b*x.to_numpy()
    r2=pm.Deterministic("r2",pm.math.var(mu)/(pm.math.var(mu)+s**2))
    pm.Normal("y",mu,s,observed=sensor_df["yield_percent"])
    idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)
print(az.summary(idata,var_names=["r2"]))
