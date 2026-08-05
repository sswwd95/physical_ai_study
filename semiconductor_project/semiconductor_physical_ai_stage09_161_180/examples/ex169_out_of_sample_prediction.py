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

m=sensor_df["particle_mean"].mean(); s=sensor_df["particle_mean"].std()
x=(sensor_df["particle_mean"]-m)/s
x_new=(8.0-m)/s
with pm.Model() as model:
    alpha=pm.Normal("alpha",94,5); beta=pm.Normal("beta",0,2); sigma=pm.HalfNormal("sigma",3)
    mu_new=pm.Deterministic("mu_new",alpha+beta*x_new)
    pm.Normal("y",alpha+beta*x.to_numpy(),sigma,observed=sensor_df["yield_percent"])
    idata=pm.sample(1000,tune=1000,chains=2,cores=1,random_seed=42,progressbar=False)

v=idata.posterior["mu_new"].values.ravel()
print("새 조건 평균 예측:",round(v.mean(),3))
print("94% HDI:",az.hdi(v,hdi_prob=0.94))
