from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
HISTORY_FILE = ROOT / "data" / "process_optimization_history.csv"
CANDIDATE_FILE = ROOT / "data" / "optimization_candidates.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

history_df = pd.read_csv(HISTORY_FILE)
candidate_df = pd.read_csv(CANDIDATE_FILE)

import pymc as pm
import arviz as az

features=["pressure_pa","rf_power_w","gas_flow_sccm","temperature_c"]
X=history_df[features]
X=(X-X.mean())/X.std()
y=history_df["uniformity_percent"].to_numpy()

with pm.Model(coords={"feature":features}) as model:
    alpha=pm.Normal("alpha",96,3)
    beta=pm.Normal("beta",0,1,dims="feature")
    sigma=pm.HalfNormal("sigma",2)
    mu=alpha+pm.math.dot(X.to_numpy(),beta)
    pm.Normal("y",mu,sigma,observed=y)
    idata=pm.sample(1000,tune=1000,chains=2,cores=1,random_seed=42,progressbar=False)

summary=az.summary(idata,var_names=["alpha","beta","sigma"],hdi_prob=.94)
print(summary)
summary.to_csv(OUTPUT_DIR/"ex295_bayesian_surrogate.csv",encoding="utf-8-sig")
