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

codes,types=pd.factorize(life_df["chamber_type"],sort=True)
y=np.log(life_df["observed_cycles"].to_numpy())
with pm.Model(coords={"type":types}) as model:
    a=pm.Normal("a",np.log(120),1)
    effect=pm.Normal("effect",0,.5,dims="type")
    sigma=pm.HalfNormal("sigma",.5)
    pm.Normal("log_life",a+effect[codes],sigma,observed=y)
    idata=pm.sample(1000,tune=1000,chains=2,cores=1,random_seed=42,progressbar=False)
print(az.summary(idata,var_names=["effect"],hdi_prob=.94))
