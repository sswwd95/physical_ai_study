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

with pm.Model() as model:
    mu = pm.Normal("mu", mu=94, sigma=3)
    sigma = pm.HalfNormal("sigma", sigma=2)
    y = pm.Normal("y", mu=mu, sigma=sigma)
    prior = pm.sample_prior_predictive(samples=1000, random_seed=42)

values = prior.prior_predictive["y"].values.ravel()
print("사전예측 평균:", round(values.mean(), 3))
print("사전예측 범위:", round(values.min(), 3), "~", round(values.max(), 3))
