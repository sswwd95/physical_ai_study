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

codes,chs=pd.factorize(defect_df["chamber_id"],sort=True)
with pm.Model(coords={"chamber":chs}) as model:
    a=pm.Normal("a",-3,1); tau=pm.HalfNormal("tau",1); z=pm.Normal("z",0,1,dims="chamber")
    p=pm.math.sigmoid(a+z[codes]*tau)
    pm.Binomial("d",n=defect_df["wafer_count"],p=p,observed=defect_df["defect_count"])
    idata=pm.sample(900,tune=900,chains=2,cores=1,target_accept=.9,random_seed=42,progressbar=False)
print(az.summary(idata,var_names=["a","tau","z"]))
