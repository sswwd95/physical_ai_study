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

data=sensor_df[["temp_sensor_a_c","temp_sensor_b_c"]].dropna().iloc[:140]
a=data["temp_sensor_a_c"].to_numpy(); b=data["temp_sensor_b_c"].to_numpy()
with pm.Model(coords={"obs":np.arange(len(data))}) as model:
    latent=pm.Normal("latent",50,30,dims="obs")
    ba=pm.Normal("ba",0,2); bb=pm.Normal("bb",0,2)
    sa=pm.HalfNormal("sa",1); sb=pm.HalfNormal("sb",1)
    nu=pm.Exponential("nu_minus_one",1/10)+1
    pm.StudentT("a",nu=nu,mu=latent+ba,sigma=sa,observed=a,dims="obs")
    pm.StudentT("b",nu=nu,mu=latent+bb,sigma=sb,observed=b,dims="obs")
    idata=pm.sample(700,tune=700,chains=2,cores=1,target_accept=.9,random_seed=42,progressbar=False)
print(az.summary(idata,var_names=["ba","bb","sa","sb"]))
