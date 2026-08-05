from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

import arviz as az
import numpy as np
import pymc as pm

sensor_df = pd.read_csv(DATA_FILE)

alarm_mask = (
    (sensor_df["chamber_temp_c"] >= 75.0)
    | (sensor_df["chamber_pressure_pa"] >= 20.0)
    | (sensor_df["vibration_g"] >= 0.15)
)
alarm_count = int(alarm_mask.sum())
total_count = len(sensor_df)

with pm.Model() as alarm_model:
    p = pm.Beta("p", alpha=1.0, beta=1.0)
    pm.Binomial(
        "alarm_obs",
        n=total_count,
        p=p,
        observed=alarm_count,
    )
    trace = pm.sample(
        draws=2000,
        tune=1000,
        chains=2,
        cores=1,
        random_seed=42,
        progressbar=False,
    )

summary = az.summary(trace, var_names=["p"], hdi_prob=0.94)
posterior_p = trace.posterior["p"].values.reshape(-1)
probability_over_5_percent = np.mean(posterior_p > 0.05)

print(f"전체 관측 수: {total_count}")
print(f"경보 횟수: {alarm_count}")
print(summary)
print(f"P(p > 0.05) = {probability_over_5_percent:.4f}")
