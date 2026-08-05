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

obs=life_df.loc[life_df["event_observed"]==1,"observed_cycles"].to_numpy()
rows=[]
for prior_scale in [80,150,250]:
    with pm.Model() as model:
        alpha=pm.HalfNormal("alpha",3); beta=pm.HalfNormal("beta",prior_scale)
        pm.Weibull("life",alpha=alpha,beta=beta,observed=obs)
        idata=pm.sample(600,tune=600,chains=2,cores=1,random_seed=42,progressbar=False)
    rows.append({"prior_scale":prior_scale,"beta_mean":float(idata.posterior["beta"].mean())})
out=pd.DataFrame(rows); print(out.round(3)); out.to_csv(OUTPUT_DIR/"ex256_prior_sensitivity.csv",index=False,encoding="utf-8-sig")
