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

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
obs=sensor_df["yield_percent"].to_numpy()
with pm.Model() as model:
    mu=pm.Normal("mu",94,5); sigma=pm.HalfNormal("sigma",3)
    pm.Normal("y",mu,sigma,observed=obs)
    idata=pm.sample(600,tune=600,chains=2,cores=1,random_seed=42,progressbar=False)
az.plot_trace(idata,var_names=["mu","sigma"]); plt.tight_layout(); plt.savefig(OUTPUT_DIR/"ex177_trace.png",dpi=150); plt.close()
az.plot_posterior(idata,var_names=["mu","sigma"],hdi_prob=0.94); plt.tight_layout(); plt.savefig(OUTPUT_DIR/"ex177_posterior.png",dpi=150); plt.close()
print("그래프 저장 완료")
