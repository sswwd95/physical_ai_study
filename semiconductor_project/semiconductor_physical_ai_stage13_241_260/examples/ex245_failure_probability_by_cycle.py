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
for cycle in [80,100,120,150]:
    p=1-np.exp(-(cycle/b)**a)
    print(cycle,"주기 이전 고장확률:",round(p.mean(),4))
