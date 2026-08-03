from pathlib import Path
import numpy as np
import pandas as pd
import pymc as pm
import arviz as az

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "bayesian_sensor_fusion.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

sensor_df = pd.read_csv(DATA_FILE)

res=(sensor_df["temp_sensor_a_c"]-sensor_df["true_temperature_c"]).dropna().to_numpy()
with pm.Model() as model:
    mu=pm.Normal("mu",0,2); sigma=pm.HalfNormal("sigma",1)
    pm.Normal("residual",mu,sigma,observed=res)
    idata=pm.sample(900,tune=900,chains=2,cores=1,random_seed=42,progressbar=False)
summary=az.summary(idata,var_names=["mu","sigma"],hdi_prob=.94)
print(summary)
summary.to_csv(OUTPUT_DIR/"ex333_twin_residual_posterior.csv",encoding="utf-8-sig")
