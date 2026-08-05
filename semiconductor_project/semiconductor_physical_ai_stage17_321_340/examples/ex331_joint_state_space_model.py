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

data=sensor_df[["temp_sensor_a_c","pressure_sensor_a_pa"]].interpolate(limit_direction="both").iloc[:140]
with pm.Model(coords={"time":np.arange(len(data))}) as model:
    temp_state=pm.GaussianRandomWalk("temp_state",sigma=pm.HalfNormal("temp_rw",1),init_dist=pm.Normal.dist(25,3),dims="time")
    pressure_state=pm.GaussianRandomWalk("pressure_state",sigma=pm.HalfNormal("pressure_rw",.5),init_dist=pm.Normal.dist(1,.5),dims="time")
    pm.Normal("temp_obs",temp_state,pm.HalfNormal("temp_sigma",1),observed=data["temp_sensor_a_c"],dims="time")
    pm.Normal("pressure_obs",pressure_state,pm.HalfNormal("pressure_sigma",.5),observed=data["pressure_sensor_a_pa"],dims="time")
    idata=pm.sample(600,tune=600,chains=2,cores=1,target_accept=.9,random_seed=42,progressbar=False)
print(az.summary(idata,var_names=["temp_rw","pressure_rw","temp_sigma","pressure_sigma"]))
