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

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
g=defect_df.groupby("recipe")[["wafer_count","defect_count"]].sum().sort_index()
with pm.Model(coords={"recipe":g.index.tolist()}) as model:
    p=pm.Beta("p",1,1,dims="recipe"); pm.Binomial("d",n=g["wafer_count"],p=p,observed=g["defect_count"],dims="recipe")
    idata=pm.sample(700,tune=700,chains=2,cores=1,random_seed=42,progressbar=False)
az.plot_posterior(idata,var_names=["p"],hdi_prob=.94); plt.tight_layout(); plt.savefig(OUTPUT_DIR/"ex198_recipe_posterior.png",dpi=150); plt.close(); print("저장 완료")
