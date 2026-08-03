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

codes,levels=pd.factorize(experiment_df["pressure_level"],sort=True)
with pm.Model(coords={"level":levels}) as model:
    mu=pm.Normal("mu",95,3,dims="level"); sigma=pm.HalfNormal("sigma",2)
    pm.Normal("y",mu[codes],sigma,observed=experiment_df["uniformity_percent"])
    idata=pm.sample(900,tune=900,chains=2,cores=1,random_seed=42,progressbar=False)
print(az.summary(idata,var_names=["mu"],hdi_prob=.94))
