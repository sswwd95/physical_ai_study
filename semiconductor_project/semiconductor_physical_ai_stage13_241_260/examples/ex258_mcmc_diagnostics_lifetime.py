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
    alpha=pm.HalfNormal("alpha",3); beta=pm.HalfNormal("beta",150); pm.Weibull("life",alpha=alpha,beta=beta,observed=obs)
    idata=pm.sample(800,tune=800,chains=2,cores=1,target_accept=.9,random_seed=42,progressbar=False)
summary=az.summary(idata,var_names=["alpha","beta"]); div=int(idata.sample_stats["diverging"].sum())
print(summary); print("divergence:",div)
summary.assign(divergence_count=div).to_csv(OUTPUT_DIR/"ex258_mcmc_diagnostics.csv",encoding="utf-8-sig")
