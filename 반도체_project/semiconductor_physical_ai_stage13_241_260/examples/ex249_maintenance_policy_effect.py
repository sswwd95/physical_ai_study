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

codes,policies=pd.factorize(life_df["maintenance_policy"],sort=True)
y=np.log(life_df["observed_cycles"].to_numpy())
with pm.Model(coords={"policy":policies}) as model:
    a=pm.Normal("a",np.log(120),1); effect=pm.Normal("effect",0,.5,dims="policy"); sigma=pm.HalfNormal("sigma",.5)
    pm.Normal("log_life",a+effect[codes],sigma,observed=y)
    idata=pm.sample(1000,tune=1000,chains=2,cores=1,random_seed=42,progressbar=False)
arr=idata.posterior["effect"].stack(sample=("chain","draw")).values
cb=list(policies).index("condition_based"); reactive=list(policies).index("reactive")
diff=arr[cb]-arr[reactive]
print("P(condition_based > reactive):",round((diff>0).mean(),4))
print("94% HDI:",az.hdi(diff,hdi_prob=.94))
