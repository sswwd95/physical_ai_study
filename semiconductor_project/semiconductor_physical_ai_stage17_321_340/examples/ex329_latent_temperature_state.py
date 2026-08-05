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

data=sensor_df[["temp_sensor_a_c","temp_sensor_b_c"]].interpolate(limit_direction="both").iloc[:160]
with pm.Model(coords={"time":np.arange(len(data))}) as model:
    sigma_state=pm.HalfNormal("sigma_state",1)
    latent=pm.GaussianRandomWalk("latent",sigma=sigma_state,init_dist=pm.Normal.dist(25,3),dims="time")
    ba=pm.Normal("ba",0,2); bb=pm.Normal("bb",0,2)
    sa=pm.HalfNormal("sa",1); sb=pm.HalfNormal("sb",1)
    pm.Normal("a",latent+ba,sa,observed=data["temp_sensor_a_c"],dims="time")
    pm.Normal("b",latent+bb,sb,observed=data["temp_sensor_b_c"],dims="time")
    idata=pm.sample(700,tune=700,chains=2,cores=1,target_accept=.9,random_seed=42,progressbar=False)
print(az.summary(idata,var_names=["sigma_state","ba","bb","sa","sb"]))
