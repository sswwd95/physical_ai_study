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
keep=100*p_s*200; inspect=250+100*p_s*.65*200
saving=keep-inspect
print("P(inspection better):",round((saving>0).mean(),4)); print("Expected saving:",round(saving.mean(),2))
