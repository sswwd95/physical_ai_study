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
ra=data["temp_sensor_a_c"]-data["true_temperature_c"]; rb=data["temp_sensor_b_c"]-data["true_temperature_c"]
with pm.Model() as model:
    sa=pm.HalfNormal("sa",1); sb=pm.HalfNormal("sb",1)
    ba=pm.Normal("ba",0,2); bb=pm.Normal("bb",0,2)
    pm.Normal("a",ba,sa,observed=ra); pm.Normal("b",bb,sb,observed=rb)
    idata=pm.sample(900,tune=900,chains=2,cores=1,random_seed=42,progressbar=False)
sa=idata.posterior["sa"].values.ravel(); sb=idata.posterior["sb"].values.ravel()
wa=(1/sa**2)/((1/sa**2)+(1/sb**2))
print("센서 A 평균 가중치:",round(wa.mean(),4))
print("94% HDI:",az.hdi(wa,hdi_prob=.94))
