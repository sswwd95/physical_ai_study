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
rows = []

for name, alpha, beta in [("uniform",1,1),("informative",3,97)]:
    with pm.Model() as model:
        p = pm.Beta("p", alpha=alpha, beta=beta)
        pm.Binomial("defects", n=total_n, p=p, observed=total_k)
        idata = pm.sample(800, tune=800, chains=2, cores=1, random_seed=42, progressbar=False)
    s = idata.posterior["p"].values.ravel()
    hdi = az.hdi(s, hdi_prob=0.94)
    rows.append({"prior":name,"posterior_mean":s.mean(),"hdi_low":hdi[0],"hdi_high":hdi[1]})

result = pd.DataFrame(rows)
print(result.round(5))
