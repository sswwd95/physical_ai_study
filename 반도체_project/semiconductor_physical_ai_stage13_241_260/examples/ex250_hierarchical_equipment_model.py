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

codes,eqs=pd.factorize(life_df["equipment_id"],sort=True)
y=np.log(life_df["observed_cycles"].to_numpy())
with pm.Model(coords={"equipment":eqs}) as model:
    mu=pm.Normal("mu",np.log(120),1); tau=pm.HalfNormal("tau",.5); z=pm.Normal("z",0,1,dims="equipment")
    sigma=pm.HalfNormal("sigma",.5)
    eq_effect=pm.Deterministic("eq_effect",z*tau,dims="equipment")
    pm.Normal("log_life",mu+eq_effect[codes],sigma,observed=y)
    idata=pm.sample(1000,tune=1000,chains=2,cores=1,target_accept=.9,random_seed=42,progressbar=False)
print(az.summary(idata,var_names=["mu","tau","eq_effect"],hdi_prob=.94))
