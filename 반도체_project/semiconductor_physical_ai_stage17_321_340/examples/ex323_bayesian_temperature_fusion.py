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

data=sensor_df[["temp_sensor_a_c","temp_sensor_b_c"]].dropna().iloc[:120]
a=data["temp_sensor_a_c"].to_numpy(); b=data["temp_sensor_b_c"].to_numpy()
with pm.Model(coords={"obs":np.arange(len(data))}) as model:
    latent=pm.Normal("latent",mu=50,sigma=30,dims="obs")
    bias_a=pm.Normal("bias_a",0,2); bias_b=pm.Normal("bias_b",0,2)
    sigma_a=pm.HalfNormal("sigma_a",1); sigma_b=pm.HalfNormal("sigma_b",1)
    pm.Normal("a",latent+bias_a,sigma_a,observed=a,dims="obs")
    pm.Normal("b",latent+bias_b,sigma_b,observed=b,dims="obs")
    idata=pm.sample(700,tune=700,chains=2,cores=1,random_seed=42,progressbar=False)
mean=idata.posterior["latent"].mean(("chain","draw")).values
print("융합 온도 처음 10개:",np.round(mean[:10],3))
