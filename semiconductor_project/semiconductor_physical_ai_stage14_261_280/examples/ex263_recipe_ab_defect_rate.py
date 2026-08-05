from pathlib import Path
import numpy as np
import pandas as pd
import pymc as pm
import arviz as az

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "bayesian_process_experiment.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

experiment_df = pd.read_csv(DATA_FILE)

group=experiment_df.loc[experiment_df["recipe"].isin(["ETCH-A","ETCH-B"])].groupby("recipe")[["wafer_count","defect_count"]].sum()
with pm.Model() as model:
    p_a=pm.Beta("p_a",1,1); p_b=pm.Beta("p_b",1,1)
    pm.Binomial("d_a",n=int(group.loc["ETCH-A","wafer_count"]),p=p_a,observed=int(group.loc["ETCH-A","defect_count"]))
    pm.Binomial("d_b",n=int(group.loc["ETCH-B","wafer_count"]),p=p_b,observed=int(group.loc["ETCH-B","defect_count"]))
    diff=pm.Deterministic("diff",p_b-p_a)
    idata=pm.sample(1000,tune=1000,chains=2,cores=1,random_seed=42,progressbar=False)
s=idata.posterior["diff"].values.ravel()
print("P(B defect rate > A):",round((s>0).mean(),4))
print("평균 차이:",round(s.mean(),5))
