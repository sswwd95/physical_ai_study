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

g=defect_df.groupby("recipe")[["wafer_count","defect_count"]].sum()
with pm.Model() as model:
    pA=pm.Beta("pA",1,1); pC=pm.Beta("pC",1,1)
    pm.Binomial("dA",n=int(g.loc["ETCH-A","wafer_count"]),p=pA,observed=int(g.loc["ETCH-A","defect_count"]))
    pm.Binomial("dC",n=int(g.loc["ETCH-C","wafer_count"]),p=pC,observed=int(g.loc["ETCH-C","defect_count"]))
    rr=pm.Deterministic("rr",pC/pA)
    idata=pm.sample(1000,tune=1000,chains=2,cores=1,random_seed=42,progressbar=False)
s=idata.posterior["rr"].values.ravel(); print("RR mean:",round(s.mean(),4)); print("94% HDI:",az.hdi(s,hdi_prob=.94)); print("P(RR<1.2):",round((s<1.2).mean(),4))
