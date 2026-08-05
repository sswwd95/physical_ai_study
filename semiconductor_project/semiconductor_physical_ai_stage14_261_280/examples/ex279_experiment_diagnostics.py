from pathlib import Path
import numpy as np
import pandas as pd
import pymc as pm
import arviz as az

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "bayesian_process_experiment.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

experiment_df = pd.read_csv(DATA_FILE)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
codes,recipes=pd.factorize(experiment_df["recipe"],sort=True)
with pm.Model(coords={"recipe":recipes}) as model:
    mu=pm.Normal("mu",95,3,dims="recipe"); sigma=pm.HalfNormal("sigma",2)
    pm.Normal("y",mu[codes],sigma,observed=experiment_df["uniformity_percent"])
    idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)
summary=az.summary(idata,var_names=["mu","sigma"])
div=int(idata.sample_stats["diverging"].sum())
summary.assign(divergence_count=div).to_csv(OUTPUT_DIR/"ex279_diagnostics.csv",encoding="utf-8-sig")
az.plot_posterior(idata,var_names=["mu"],hdi_prob=.94)
plt.tight_layout(); plt.savefig(OUTPUT_DIR/"ex279_recipe_posterior.png",dpi=150); plt.close()
print(summary)
