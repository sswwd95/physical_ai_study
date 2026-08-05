from pathlib import Path
import numpy as np
import pandas as pd
import pymc as pm
import arviz as az

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "bayesian_yield_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)
sensor_df = pd.read_csv(DATA_FILE)

r_codes,recipes=pd.factorize(sensor_df["recipe"],sort=True)
c_codes,chambers=pd.factorize(sensor_df["chamber_id"],sort=True)
with pm.Model(coords={"recipe":recipes,"chamber":chambers}) as model:
    a=pm.Normal("a",94,5); br=pm.Normal("br",0,1,dims="recipe")
    tau=pm.HalfNormal("tau",1); z=pm.Normal("z",0,1,dims="chamber")
    bc=pm.Deterministic("bc",z*tau,dims="chamber")
    s=pm.HalfNormal("s",3)
    pm.Normal("y",a+br[r_codes]+bc[c_codes],s,observed=sensor_df["yield_percent"])
    idata=pm.sample(800,tune=800,chains=2,cores=1,target_accept=0.9,random_seed=42,progressbar=False)
print(az.summary(idata,var_names=["a","br","tau","bc"]))
