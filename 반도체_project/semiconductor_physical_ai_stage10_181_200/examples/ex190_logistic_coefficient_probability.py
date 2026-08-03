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

features=["temp_abs_deviation","pressure_abs_deviation","particle_mean"]
X=defect_df[features]; X=(X-X.mean())/X.std(); y=(defect_df["defect_count"]>0).astype(int)
with pm.Model(coords={"feature":features}) as model:
    a=pm.Normal("a",0,2); beta=pm.Normal("beta",0,1,dims="feature")
    pm.Bernoulli("y",logit_p=a+pm.math.dot(X.to_numpy(),beta),observed=y)
    idata=pm.sample(900,tune=900,chains=2,cores=1,random_seed=42,progressbar=False)
arr=idata.posterior["beta"].stack(sample=("chain","draw")).values
rows=[]
for i,f in enumerate(features):
    h=az.hdi(arr[i],hdi_prob=.94); rows.append({"feature":f,"mean":arr[i].mean(),"p_positive":(arr[i]>0).mean(),"hdi_low":h[0],"hdi_high":h[1]})
out=pd.DataFrame(rows); print(out.round(4)); out.to_csv(OUTPUT_DIR/"ex190_beta_probabilities.csv",index=False,encoding="utf-8-sig")
