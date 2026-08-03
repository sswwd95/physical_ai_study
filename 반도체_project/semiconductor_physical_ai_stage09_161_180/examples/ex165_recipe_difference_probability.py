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

codes, recipes = pd.factorize(sensor_df["recipe"], sort=True)
a_idx = list(recipes).index("ETCH-A")
c_idx = list(recipes).index("ETCH-C")
with pm.Model(coords={"recipe": recipes}) as model:
    mu_recipe = pm.Normal("mu_recipe", 94, 4, dims="recipe")
    sigma = pm.HalfNormal("sigma", 3)
    diff_A_C = pm.Deterministic("diff_A_C", mu_recipe[a_idx]-mu_recipe[c_idx])
    pm.Normal("y", mu_recipe[codes], sigma, observed=sensor_df["yield_percent"])
    idata = pm.sample(1000, tune=1000, chains=2, cores=1, random_seed=42, progressbar=False)

d = idata.posterior["diff_A_C"].values.ravel()
print("평균 차이:", round(d.mean(),4))
print("P(A>C):", round((d>0).mean(),4))
print("94% HDI:", az.hdi(d,hdi_prob=0.94))
