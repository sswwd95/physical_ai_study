from pathlib import Path
import numpy as np
import pandas as pd
import pymc as pm
import arviz as az

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "bayesian_defect_rate_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)
defect_df = pd.read_csv(DATA_FILE)

features=["temp_abs_deviation","pressure_abs_deviation","particle_mean"]
X=defect_df[features]; mean=X.mean(); std=X.std(); Xs=(X-mean)/std; y=(defect_df["defect_count"]>0).astype(int)
with pm.Model(coords={"feature":features}) as model:
    a=pm.Normal("a",0,2); beta=pm.Normal("beta",0,1,dims="feature")
    p=pm.Deterministic("p",pm.math.sigmoid(a+pm.math.dot(Xs.to_numpy(),beta)))
    pm.Bernoulli("y",p=p,observed=y)
    idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)
risk=idata.posterior["p"].mean(("chain","draw")).values
out=defect_df[["lot_id","recipe","chamber_id","defect_rate"]].copy(); out["posterior_risk"]=risk; out=out.sort_values("posterior_risk",ascending=False)
print(out.head(15).round(4)); out.to_csv(OUTPUT_DIR/"ex199_lot_risk.csv",index=False,encoding="utf-8-sig")
