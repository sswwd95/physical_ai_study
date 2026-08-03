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
res=np.concatenate([
    (data["temp_sensor_a_c"]-data["true_temperature_c"]).to_numpy(),
    (data["temp_sensor_b_c"]-data["true_temperature_c"]).to_numpy()
])
sensor_code=np.concatenate([np.zeros(len(data),dtype=int),np.ones(len(data),dtype=int)])
with pm.Model(coords={"sensor":["A","B"]}) as model:
    mu_bias=pm.Normal("mu_bias",0,1)
    tau=pm.HalfNormal("tau",1)
    z=pm.Normal("z",0,1,dims="sensor")
    bias=pm.Deterministic("bias",mu_bias+z*tau,dims="sensor")
    sigma=pm.HalfNormal("sigma",1,dims="sensor")
    pm.Normal("r",bias[sensor_code],sigma[sensor_code],observed=res)
    idata=pm.sample(900,tune=900,chains=2,cores=1,target_accept=.9,random_seed=42,progressbar=False)
print(az.summary(idata,var_names=["mu_bias","tau","bias","sigma"]))
