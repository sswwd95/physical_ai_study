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
    latent=pm.Normal("latent",50,30,dims="obs")
    ba=pm.Normal("ba",0,2); bb=pm.Normal("bb",0,2)
    sa=pm.HalfNormal("sa",1); sb=pm.HalfNormal("sb",1)
    pm.Normal("a",latent+ba,sa,observed=a,dims="obs")
    pm.Normal("b",latent+bb,sb,observed=b,dims="obs")
    idata=pm.sample(700,tune=700,chains=2,cores=1,random_seed=42,progressbar=False)
arr=idata.posterior["latent"].stack(sample=("chain","draw")).values
h=az.hdi(arr.T,hdi_prob=.94)
out=pd.DataFrame({"fused_mean":arr.mean(axis=1),"hdi_low":h[:,0],"hdi_high":h[:,1]})
out.to_csv(OUTPUT_DIR/"ex336_credible_interval_fusion.csv",index=False,encoding="utf-8-sig")
print(out.head(10).round(3))
