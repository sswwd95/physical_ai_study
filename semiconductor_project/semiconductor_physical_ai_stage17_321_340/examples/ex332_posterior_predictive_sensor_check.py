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

data=sensor_df[["temp_sensor_a_c","true_temperature_c"]].dropna()
res=(data["temp_sensor_a_c"]-data["true_temperature_c"]).to_numpy()
with pm.Model() as model:
    bias=pm.Normal("bias",0,2); sigma=pm.HalfNormal("sigma",1)
    pm.Normal("r",bias,sigma,observed=res)
    idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)
    ppc=pm.sample_posterior_predictive(idata,random_seed=42,progressbar=False)
pred=ppc.posterior_predictive["r"].values
print("관측 평균:",round(res.mean(),4))
print("예측 평균:",round(pred.mean(),4))
print("관측 표준편차:",round(res.std(),4))
print("예측 표준편차:",round(pred.std(),4))
