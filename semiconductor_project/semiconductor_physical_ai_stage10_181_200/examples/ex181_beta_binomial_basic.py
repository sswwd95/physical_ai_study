from pathlib import Path
import numpy as np
import pandas as pd
import pymc as pm
import arviz as az

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "bayesian_defect_rate_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)
defect_df = pd.read_csv(DATA_FILE)

total_n = int(defect_df["wafer_count"].sum())
total_k = int(defect_df["defect_count"].sum())

with pm.Model() as model:
    p = pm.Beta("p", alpha=1, beta=1)
    pm.Binomial("defects", n=total_n, p=p, observed=total_k)
    idata = pm.sample(1000, tune=1000, chains=2, cores=1, random_seed=42, progressbar=False)

samples = idata.posterior["p"].values.ravel()
print("사후 평균:", round(samples.mean(), 5))
print("94% HDI:", az.hdi(samples, hdi_prob=0.94))
