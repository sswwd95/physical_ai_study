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
with pm.Model() as model:
    bias=pm.Normal("bias",0,2); sigma=pm.HalfNormal("sigma",1)
    pm.Normal("r",bias,sigma,observed=res)
    idata=pm.sample(900,tune=900,chains=2,cores=1,random_seed=42,progressbar=False)
s=idata.posterior["bias"].values.ravel()
print("P(|bias|>1.0):",round((np.abs(s)>1.0).mean(),4))
print("P(|bias|>2.0):",round((np.abs(s)>2.0).mean(),4))
