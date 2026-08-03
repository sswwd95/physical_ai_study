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

r_codes,recipes=pd.factorize(experiment_df["recipe"],sort=True)
c_codes,chambers=pd.factorize(experiment_df["chamber_id"],sort=True)
with pm.Model(coords={"recipe":recipes,"chamber":chambers}) as model:
    a=pm.Normal("a",95,3); r=pm.Normal("r",0,1,dims="recipe"); c=pm.Normal("c",0,1,dims="chamber")
    interaction=pm.Normal("interaction",0,.7,dims=("recipe","chamber"))
    sigma=pm.HalfNormal("sigma",2)
    pm.Normal("y",a+r[r_codes]+c[c_codes]+interaction[r_codes,c_codes],sigma,observed=experiment_df["uniformity_percent"])
    idata=pm.sample(900,tune=900,chains=2,cores=1,target_accept=.9,random_seed=42,progressbar=False)
print(az.summary(idata,var_names=["interaction"],hdi_prob=.94))
