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
    alpha=pm.Normal("alpha",94,5); beta=pm.Normal("beta",0,2); sigma=pm.HalfNormal("sigma",3)
    pm.Normal("y",alpha+beta*x.to_numpy(),sigma,observed=sensor_df["yield_percent"])
    idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)
    ppc=pm.sample_posterior_predictive(idata,random_seed=42,progressbar=False)

pred=ppc.posterior_predictive["y"].values
print("관측 평균:",round(sensor_df["yield_percent"].mean(),3))
print("예측 평균:",round(pred.mean(),3))
print("관측 표준편차:",round(sensor_df["yield_percent"].std(),3))
print("예측 표준편차:",round(pred.std(),3))
