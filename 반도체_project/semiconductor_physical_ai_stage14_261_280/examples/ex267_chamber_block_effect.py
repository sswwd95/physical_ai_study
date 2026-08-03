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
    a=pm.Normal("a",95,3)
    recipe_eff=pm.Normal("recipe_eff",0,1,dims="recipe")
    chamber_eff=pm.Normal("chamber_eff",0,1,dims="chamber")
    sigma=pm.HalfNormal("sigma",2)
    mu=a+recipe_eff[r_codes]+chamber_eff[c_codes]
    pm.Normal("y",mu,sigma,observed=experiment_df["uniformity_percent"])
    idata=pm.sample(1000,tune=1000,chains=2,cores=1,random_seed=42,progressbar=False)
print(az.summary(idata,var_names=["recipe_eff","chamber_eff"],hdi_prob=.94))
