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
X=defect_df[features]; X=(X-X.mean())/X.std()
y=(defect_df["defect_count"]>0).astype(int).to_numpy()
with pm.Model(coords={"feature":features}) as model:
    a=pm.Normal("a",0,2); beta=pm.Normal("beta",0,1,dims="feature")
    p=pm.Deterministic("p",pm.math.sigmoid(a+pm.math.dot(X.to_numpy(),beta)))
    pm.Bernoulli("y",p=p,observed=y)
    idata=pm.sample(1000,tune=1000,chains=2,cores=1,random_seed=42,progressbar=False)
print(az.summary(idata,var_names=["a","beta"]))
