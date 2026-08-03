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

res=(sensor_df["temp_sensor_b_c"]-sensor_df["true_temperature_c"]).dropna().to_numpy()
models={}
with pm.Model() as normal_model:
    mu=pm.Normal("mu",0,2); sigma=pm.HalfNormal("sigma",1)
    pm.Normal("r",mu,sigma,observed=res)
    models["normal"]=pm.sample(700,tune=700,chains=2,cores=1,random_seed=42,progressbar=False,idata_kwargs={"log_likelihood":True})
with pm.Model() as student_model:
    mu=pm.Normal("mu",0,2); sigma=pm.HalfNormal("sigma",1)
    nu=pm.Exponential("nu_minus_one",1/10)+1
    pm.StudentT("r",nu=nu,mu=mu,sigma=sigma,observed=res)
    models["student_t"]=pm.sample(700,tune=700,chains=2,cores=1,random_seed=42,progressbar=False,idata_kwargs={"log_likelihood":True})
print(az.compare(models))
