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
    mu = pm.Normal("mu", mu=94, sigma=5)
    sigma = pm.HalfNormal("sigma", sigma=3)
    y = pm.Normal("y", mu=mu, sigma=sigma, observed=observed)
    idata = pm.sample(draws=1000, tune=1000, chains=2, cores=1, random_seed=42, progressbar=False)

summary = az.summary(idata, var_names=["mu","sigma"], hdi_prob=0.94)
print(summary)
summary.to_csv(OUTPUT_DIR/"ex162_posterior_summary.csv",encoding="utf-8-sig")
