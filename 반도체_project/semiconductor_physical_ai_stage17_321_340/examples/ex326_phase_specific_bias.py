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

data=sensor_df.dropna(subset=["temp_sensor_b_c"]).copy()
phases=sorted(data["process_phase"].unique())
codes=pd.Categorical(data["process_phase"],categories=phases).codes
res=(data["temp_sensor_b_c"]-data["true_temperature_c"]).to_numpy()
with pm.Model(coords={"phase":phases}) as model:
    bias=pm.Normal("bias",0,2,dims="phase")
    sigma=pm.HalfNormal("sigma",1)
    pm.Normal("r",bias[codes],sigma,observed=res)
    idata=pm.sample(900,tune=900,chains=2,cores=1,random_seed=42,progressbar=False)
print(az.summary(idata,var_names=["bias"],hdi_prob=.94))
