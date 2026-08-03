from pathlib import Path
import numpy as np
import pandas as pd
import pymc as pm
import arviz as az

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "bayesian_yield_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)
sensor_df = pd.read_csv(DATA_FILE)

codes,chambers=pd.factorize(sensor_df["chamber_id"],sort=True)
with pm.Model(coords={"chamber":chambers}) as model:
    mu_global=pm.Normal("mu_global",94,5)
    tau=pm.HalfNormal("tau",2)
    z=pm.Normal("z",0,1,dims="chamber")
    mu_chamber=pm.Deterministic("mu_chamber",mu_global+z*tau,dims="chamber")
    sigma=pm.HalfNormal("sigma",3)
    pm.Normal("y",mu_chamber[codes],sigma,observed=sensor_df["yield_percent"])
    idata=pm.sample(1000,tune=1000,chains=2,cores=1,random_seed=42,progressbar=False,target_accept=0.9)

summary=az.summary(idata,var_names=["mu_global","tau","mu_chamber"],hdi_prob=0.94)
print(summary)
summary.to_csv(OUTPUT_DIR/"ex170_hierarchical_chamber.csv",encoding="utf-8-sig")
