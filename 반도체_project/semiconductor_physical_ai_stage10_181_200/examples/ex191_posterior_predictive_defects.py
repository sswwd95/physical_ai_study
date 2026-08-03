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
pred=np.random.default_rng(42).binomial(100,p_s)
print("예측 평균 불량수:",round(pred.mean(),3)); print("94% HDI:",az.hdi(pred,hdi_prob=.94))
