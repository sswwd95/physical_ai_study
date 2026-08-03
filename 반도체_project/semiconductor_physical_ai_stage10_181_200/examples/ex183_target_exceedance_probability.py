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

n = int(defect_df["wafer_count"].sum())
k = int(defect_df["defect_count"].sum())
with pm.Model() as model:
    p = pm.Beta("p", 1, 1)
    pm.Binomial("d", n=n, p=p, observed=k)
    idata = pm.sample(1000, tune=1000, chains=2, cores=1, random_seed=42, progressbar=False)

s = idata.posterior["p"].values.ravel()
print("P(p>0.04):", round((s>0.04).mean(),4))
print("P(p>0.05):", round((s>0.05).mean(),4))
