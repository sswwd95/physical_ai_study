from pathlib import Path
import numpy as np
import pandas as pd
import pymc as pm
import arviz as az

ROOT = Path(__file__).resolve().parents[1]
LIFE_FILE = ROOT / "data" / "bayesian_equipment_lifetime.csv"
RUL_FILE = ROOT / "data" / "bayesian_rul_snapshots.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

life_df = pd.read_csv(LIFE_FILE)
rul_df = pd.read_csv(RUL_FILE)

features=["cycle","vibration_rms_g","temperature_c","motor_current_a","particle_count"]
X=rul_df[features]; mean=X.mean(); std=X.std(); Xs=(X-mean)/std; y=rul_df["rul_cycles"].to_numpy()
with pm.Model(coords={"feature":features}) as model:
    a=pm.Normal("a",80,40); beta=pm.Normal("beta",0,20,dims="feature"); sigma=pm.HalfNormal("sigma",20)
    pm.Normal("rul",a+pm.math.dot(Xs.to_numpy(),beta),sigma,observed=y)
    idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)
    ppc=pm.sample_posterior_predictive(idata,random_seed=42,progressbar=False)
pred=ppc.posterior_predictive["rul"].values.reshape(-1,len(rul_df))
out=rul_df[["equipment_id","cycle","rul_cycles"]].copy()
out["pred_mean"]=pred.mean(0); out["pred_p03"]=np.quantile(pred,.03,axis=0); out["pred_p97"]=np.quantile(pred,.97,axis=0)
out.to_csv(OUTPUT_DIR/"ex254_rul_intervals.csv",index=False,encoding="utf-8-sig")
print(out.head(10).round(2))
