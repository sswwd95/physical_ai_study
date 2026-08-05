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

observed=life_df.loc[life_df["event_observed"]==1,"observed_cycles"].to_numpy()
with pm.Model() as model:
    alpha=pm.HalfNormal("alpha",3)
    beta=pm.HalfNormal("beta",150)
    pm.Weibull("lifetime",alpha=alpha,beta=beta,observed=observed)
    idata=pm.sample(1000,tune=1000,chains=2,cores=1,random_seed=42,progressbar=False,target_accept=.9)
print(az.summary(idata,var_names=["alpha","beta"],hdi_prob=.94))
