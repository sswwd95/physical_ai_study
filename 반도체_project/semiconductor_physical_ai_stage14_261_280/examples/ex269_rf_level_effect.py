from pathlib import Path
import numpy as np
import pandas as pd
import pymc as pm
import arviz as az

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "bayesian_process_experiment.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

experiment_df = pd.read_csv(DATA_FILE)

codes,levels=pd.factorize(experiment_df["rf_level"],sort=True)
with pm.Model(coords={"level":levels}) as model:
    mu_u=pm.Normal("mu_uniformity",95,3,dims="level")
    mu_e=pm.Normal("mu_etch_rate",515,20,dims="level")
    su=pm.HalfNormal("sigma_u",2); se=pm.HalfNormal("sigma_e",10)
    pm.Normal("u",mu_u[codes],su,observed=experiment_df["uniformity_percent"])
    pm.Normal("e",mu_e[codes],se,observed=experiment_df["etch_rate_nm_min"])
    idata=pm.sample(900,tune=900,chains=2,cores=1,random_seed=42,progressbar=False)
print(az.summary(idata,var_names=["mu_uniformity","mu_etch_rate"],hdi_prob=.94))
