from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

import arviz as az
import pymc as pm

sensor_df = pd.read_csv(DATA_FILE)
temperature_data = sensor_df["chamber_temp_c"].to_numpy()

with pm.Model() as temperature_model:
    mu = pm.Normal("mu", mu=72.0, sigma=5.0)
    sigma = pm.HalfNormal("sigma", sigma=5.0)
    pm.Normal(
        "temperature_obs",
        mu=mu,
        sigma=sigma,
        observed=temperature_data,
    )
    trace = pm.sample(
        draws=1000,
        tune=1000,
        chains=2,
        cores=1,
        random_seed=42,
        progressbar=False,
    )

summary = az.summary(trace, var_names=["mu", "sigma"], hdi_prob=0.94)
print(summary)
summary.to_csv(
    OUTPUT_DIR / "ex019_bayesian_temperature_summary.csv",
    encoding="utf-8-sig",
)
