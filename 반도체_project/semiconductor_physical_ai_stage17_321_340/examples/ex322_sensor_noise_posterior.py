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

data=sensor_df[["temp_sensor_a_c","temp_sensor_b_c","true_temperature_c"]].dropna()
res_a=data["temp_sensor_a_c"]-data["true_temperature_c"]
res_b=data["temp_sensor_b_c"]-data["true_temperature_c"]
with pm.Model() as model:
    bias_a=pm.Normal("bias_a",0,2); bias_b=pm.Normal("bias_b",0,2)
    sigma_a=pm.HalfNormal("sigma_a",1); sigma_b=pm.HalfNormal("sigma_b",1)
    pm.Normal("a",bias_a,sigma_a,observed=res_a)
    pm.Normal("b",bias_b,sigma_b,observed=res_b)
    idata=pm.sample(1000,tune=1000,chains=2,cores=1,random_seed=42,progressbar=False)
print(az.summary(idata,var_names=["sigma_a","sigma_b"],hdi_prob=.94))
