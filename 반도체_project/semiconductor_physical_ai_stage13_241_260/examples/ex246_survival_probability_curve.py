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
with pm.Model() as model:
    alpha=pm.HalfNormal("alpha",3); beta=pm.HalfNormal("beta",150)
    pm.Weibull("lifetime",alpha=alpha,beta=beta,observed=obs)
    idata=pm.sample(900,tune=900,chains=2,cores=1,random_seed=42,progressbar=False)
a=idata.posterior["alpha"].values.ravel(); b=idata.posterior["beta"].values.ravel()
rows=[]
for cycle in range(20,201,20):
    s=np.exp(-(cycle/b)**a)
    h=az.hdi(s,hdi_prob=.94)
    rows.append({"cycle":cycle,"survival_mean":s.mean(),"hdi_low":h[0],"hdi_high":h[1]})
out=pd.DataFrame(rows); print(out.round(4)); out.to_csv(OUTPUT_DIR/"ex246_survival_curve.csv",index=False,encoding="utf-8-sig")
