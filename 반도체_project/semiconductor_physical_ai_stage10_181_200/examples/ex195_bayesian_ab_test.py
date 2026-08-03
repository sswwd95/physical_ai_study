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
    pA=pm.Beta("pA",1,1); pB=pm.Beta("pB",1,1)
    pm.Binomial("dA",n=int(g.loc["ETCH-A","wafer_count"]),p=pA,observed=int(g.loc["ETCH-A","defect_count"]))
    pm.Binomial("dB",n=int(g.loc["ETCH-B","wafer_count"]),p=pB,observed=int(g.loc["ETCH-B","defect_count"]))
    rr=pm.Deterministic("rr",pB/pA)
    idata=pm.sample(1000,tune=1000,chains=2,cores=1,random_seed=42,progressbar=False)
s=idata.posterior; print("P(B<A):",round((s["pB"]<s["pA"]).mean().item(),4)); print("RR mean:",round(s["rr"].mean().item(),4))
