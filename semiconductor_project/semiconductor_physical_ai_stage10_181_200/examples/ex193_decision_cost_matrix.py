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

n=int(defect_df["wafer_count"].sum()); k=int(defect_df["defect_count"].sum())
with pm.Model() as model:
    p=pm.Beta("p",1,1); pm.Binomial("d",n=n,p=p,observed=k)
    idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)
p_s=idata.posterior["p"].values.ravel()
wafer_batch=100; defect_cost=200; inspection_cost=250; reduction=0.35
cost_keep=wafer_batch*p_s*defect_cost
cost_inspect=inspection_cost+wafer_batch*p_s*(1-reduction)*defect_cost
print("유지 기대비용:",round(cost_keep.mean(),2)); print("강화검사 기대비용:",round(cost_inspect.mean(),2))
