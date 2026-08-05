from pathlib import Path
import numpy as np
import pandas as pd
import pymc as pm
import arviz as az

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "bayesian_yield_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)
sensor_df = pd.read_csv(DATA_FILE)

obs=sensor_df["yield_percent"].to_numpy()
with pm.Model() as model:
    mu=pm.Normal("mu",94,5); sigma=pm.HalfNormal("sigma",3)
    pm.Normal("y",mu,sigma,observed=obs)
    idata=pm.sample(600,tune=600,chains=2,cores=1,random_seed=42,progressbar=False)
    ppc=pm.sample_posterior_predictive(idata,random_seed=42,progressbar=False)
pred=ppc.posterior_predictive["y"].values.reshape(-1,len(obs))
out=sensor_df.head(20)[["lot_id","yield_percent"]].copy()
out["pred_mean"]=pred[:,:20].mean(axis=0); out["pred_p03"]=np.quantile(pred[:,:20],0.03,axis=0); out["pred_p97"]=np.quantile(pred[:,:20],0.97,axis=0)
print(out.round(3)); out.to_csv(OUTPUT_DIR/"ex179_prediction_table.csv",index=False,encoding="utf-8-sig")
