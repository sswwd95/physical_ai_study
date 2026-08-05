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

codes,recipes=pd.factorize(experiment_df["recipe"],sort=True)
with pm.Model(coords={"recipe":recipes}) as model:
    mu=pm.Normal("mu",95,3,dims="recipe"); sigma=pm.HalfNormal("sigma",2)
    pm.Normal("y",mu[codes],sigma,observed=experiment_df["uniformity_percent"])
    idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)
    ppc=pm.sample_posterior_predictive(idata,random_seed=42,progressbar=False)
pred=ppc.posterior_predictive["y"].values
print("관측 평균:",round(experiment_df["uniformity_percent"].mean(),4))
print("예측 평균:",round(pred.mean(),4))
print("관측 표준편차:",round(experiment_df["uniformity_percent"].std(),4))
print("예측 표준편차:",round(pred.std(),4))
