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
a = recipes.index("ETCH-A")
c = recipes.index("ETCH-C")

with pm.Model(coords={"recipe":recipes}) as model:
    p = pm.Beta("p",1,1,dims="recipe")
    diff = pm.Deterministic("diff_C_A", p[c]-p[a])
    pm.Binomial("d", n=group["wafer_count"].to_numpy(), p=p,
                observed=group["defect_count"].to_numpy(), dims="recipe")
    idata = pm.sample(1000,tune=1000,chains=2,cores=1,random_seed=42,progressbar=False)

s = idata.posterior["diff_C_A"].values.ravel()
print("평균 차이:", round(s.mean(),5))
print("P(C>A):", round((s>0).mean(),4))
print("94% HDI:", az.hdi(s,hdi_prob=0.94))
