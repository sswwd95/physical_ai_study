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

x1=(sensor_df["particle_mean"]-sensor_df["particle_mean"].mean())/sensor_df["particle_mean"].std()
X=sensor_df[["particle_mean","maintenance_age_hours"]]
X=(X-X.mean())/X.std()
models={}
with pm.Model() as m1:
    a=pm.Normal("a",94,5); b=pm.Normal("b",0,2); s=pm.HalfNormal("s",3)
    pm.Normal("y",a+b*x1.to_numpy(),s,observed=sensor_df["yield_percent"])
    models["simple"]=pm.sample(600,tune=600,chains=2,cores=1,random_seed=42,progressbar=False,idata_kwargs={"log_likelihood":True})
with pm.Model() as m2:
    a=pm.Normal("a",94,5); b=pm.Normal("b",0,1,shape=2); s=pm.HalfNormal("s",3)
    pm.Normal("y",a+pm.math.dot(X.to_numpy(),b),s,observed=sensor_df["yield_percent"])
    models["multiple"]=pm.sample(600,tune=600,chains=2,cores=1,random_seed=42,progressbar=False,idata_kwargs={"log_likelihood":True})
print(az.compare(models))
