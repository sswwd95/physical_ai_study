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
rows=[]
for prior_sigma in [5.0,0.5]:
    with pm.Model() as model:
        a=pm.Normal("a",94,5); b=pm.Normal("b",0,prior_sigma); s=pm.HalfNormal("s",3)
        pm.Normal("y",a+b*x.to_numpy(),s,observed=sensor_df["yield_percent"])
        idata=pm.sample(600,tune=600,chains=2,cores=1,random_seed=42,progressbar=False)
    rows.append({"prior_sigma":prior_sigma,"beta_mean":float(idata.posterior["b"].mean())})
print(pd.DataFrame(rows))
