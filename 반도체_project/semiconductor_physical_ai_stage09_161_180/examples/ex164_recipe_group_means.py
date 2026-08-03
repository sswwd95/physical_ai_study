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
with pm.Model(coords={"recipe": recipes}) as model:
    mu_recipe = pm.Normal("mu_recipe", 94, 4, dims="recipe")
    sigma = pm.HalfNormal("sigma", 3)
    pm.Normal("y", mu=mu_recipe[codes], sigma=sigma, observed=sensor_df["yield_percent"])
    idata = pm.sample(1000, tune=1000, chains=2, cores=1, random_seed=42, progressbar=False)

summary = az.summary(idata, var_names=["mu_recipe"], hdi_prob=0.94)
print(summary)
summary.to_csv(OUTPUT_DIR/"ex164_recipe_means.csv",encoding="utf-8-sig")
