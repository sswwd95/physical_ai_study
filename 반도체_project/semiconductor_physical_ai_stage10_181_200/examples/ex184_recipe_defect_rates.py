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

group = defect_df.groupby("recipe")[["wafer_count","defect_count"]].sum().sort_index()
recipes = group.index.tolist()

with pm.Model(coords={"recipe":recipes}) as model:
    p_recipe = pm.Beta("p_recipe", 1, 1, dims="recipe")
    pm.Binomial("d", n=group["wafer_count"].to_numpy(), p=p_recipe,
                observed=group["defect_count"].to_numpy(), dims="recipe")
    idata = pm.sample(1000, tune=1000, chains=2, cores=1, random_seed=42, progressbar=False)

summary = az.summary(idata, var_names=["p_recipe"], hdi_prob=0.94)
print(summary)
summary.to_csv(OUTPUT_DIR/"ex184_recipe_defect_rates.csv",encoding="utf-8-sig")
