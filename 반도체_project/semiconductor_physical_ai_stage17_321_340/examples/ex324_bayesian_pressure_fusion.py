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

data=sensor_df[["pressure_sensor_a_pa","pressure_sensor_b_pa"]].dropna().iloc[:120]
a=data["pressure_sensor_a_pa"].to_numpy(); b=data["pressure_sensor_b_pa"].to_numpy()
with pm.Model(coords={"obs":np.arange(len(data))}) as model:
    latent=pm.Normal("latent",mu=10,sigma=10,dims="obs")
    bias_a=pm.Normal("bias_a",0,1); bias_b=pm.Normal("bias_b",0,1)
    sigma_a=pm.HalfNormal("sigma_a",.5); sigma_b=pm.HalfNormal("sigma_b",.5)
    pm.Normal("a",latent+bias_a,sigma_a,observed=a,dims="obs")
    pm.Normal("b",latent+bias_b,sigma_b,observed=b,dims="obs")
    idata=pm.sample(700,tune=700,chains=2,cores=1,random_seed=42,progressbar=False)
print(az.summary(idata,var_names=["bias_a","bias_b","sigma_a","sigma_b"]))
