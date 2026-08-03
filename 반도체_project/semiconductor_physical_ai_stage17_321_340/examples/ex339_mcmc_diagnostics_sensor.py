from pathlib import Path
import numpy as np
import pandas as pd
import pymc as pm
import arviz as az

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "bayesian_sensor_fusion.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

sensor_df = pd.read_csv(DATA_FILE)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
res=(sensor_df["temp_sensor_a_c"]-sensor_df["true_temperature_c"]).dropna().to_numpy()
with pm.Model() as model:
    mu=pm.Normal("mu",0,2); sigma=pm.HalfNormal("sigma",1)
    pm.Normal("r",mu,sigma,observed=res)
    idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)
summary=az.summary(idata,var_names=["mu","sigma"])
div=int(idata.sample_stats["diverging"].sum())
summary.assign(divergence_count=div).to_csv(OUTPUT_DIR/"ex339_mcmc_diagnostics.csv",encoding="utf-8-sig")
az.plot_posterior(idata,var_names=["mu","sigma"],hdi_prob=.94)
plt.tight_layout(); plt.savefig(OUTPUT_DIR/"ex339_sensor_posterior.png",dpi=150); plt.close()
print(summary)
