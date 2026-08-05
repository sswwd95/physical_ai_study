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

x = (sensor_df["particle_mean"]-sensor_df["particle_mean"].mean())/sensor_df["particle_mean"].std()
y_obs = sensor_df["yield_percent"].to_numpy()
with pm.Model() as model:
    alpha = pm.Normal("alpha",94,5)
    beta = pm.Normal("beta",0,2)
    sigma = pm.HalfNormal("sigma",3)
    mu = alpha + beta*x.to_numpy()
    pm.Normal("y",mu,sigma,observed=y_obs)
    idata = pm.sample(1000,tune=1000,chains=2,cores=1,random_seed=42,progressbar=False)

summary=az.summary(idata,var_names=["alpha","beta","sigma"],hdi_prob=0.94)
print(summary)
