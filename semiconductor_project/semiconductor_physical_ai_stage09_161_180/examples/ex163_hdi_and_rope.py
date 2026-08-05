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

observed = sensor_df["yield_percent"].to_numpy()
with pm.Model() as model:
    mu = pm.Normal("mu", 94, 5)
    sigma = pm.HalfNormal("sigma", 3)
    pm.Normal("y", mu, sigma, observed=observed)
    idata = pm.sample(1000, tune=1000, chains=2, cores=1, random_seed=42, progressbar=False)

samples = idata.posterior["mu"].values.ravel()
hdi = az.hdi(samples, hdi_prob=0.94)
print("94% HDI:", hdi)
print("P(mu > 94):", round((samples>94).mean(),4))
print("P(93.5 <= mu <= 94.5):", round(((samples>=93.5)&(samples<=94.5)).mean(),4))
