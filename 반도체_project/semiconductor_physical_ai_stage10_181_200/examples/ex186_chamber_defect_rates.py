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

g=defect_df.groupby("chamber_id")[["wafer_count","defect_count"]].sum().sort_index()
chs=g.index.tolist()
with pm.Model(coords={"chamber":chs}) as model:
    p=pm.Beta("p",1,1,dims="chamber")
    pm.Binomial("d",n=g["wafer_count"].to_numpy(),p=p,observed=g["defect_count"].to_numpy(),dims="chamber")
    idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)
summary=az.summary(idata,var_names=["p"],hdi_prob=.94)
print(summary); summary.to_csv(OUTPUT_DIR/"ex186_chamber_rates.csv",encoding="utf-8-sig")
