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

c_codes,chambers=pd.factorize(experiment_df["chamber_id"],sort=True)
r_codes,recipes=pd.factorize(experiment_df["recipe"],sort=True)
with pm.Model(coords={"chamber":chambers,"recipe":recipes}) as model:
    a=pm.Normal("a",95,3); tau=pm.HalfNormal("tau",1); z=pm.Normal("z",0,1,dims="chamber")
    chamber_eff=pm.Deterministic("chamber_eff",z*tau,dims="chamber")
    recipe_eff=pm.Normal("recipe_eff",0,1,dims="recipe")
    sigma=pm.HalfNormal("sigma",2)
    pm.Normal("y",a+chamber_eff[c_codes]+recipe_eff[r_codes],sigma,observed=experiment_df["uniformity_percent"])
    idata=pm.sample(1000,tune=1000,chains=2,cores=1,target_accept=.9,random_seed=42,progressbar=False)
print(az.summary(idata,var_names=["tau","chamber_eff","recipe_eff"],hdi_prob=.94))
