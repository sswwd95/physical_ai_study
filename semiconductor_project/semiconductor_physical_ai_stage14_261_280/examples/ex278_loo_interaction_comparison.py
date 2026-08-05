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
p_codes,pressures=pd.factorize(experiment_df["pressure_level"],sort=True)
models={}
with pm.Model(coords={"recipe":recipes,"pressure":pressures}) as additive:
    a=pm.Normal("a",95,3); r=pm.Normal("r",0,1,dims="recipe"); p=pm.Normal("p",0,1,dims="pressure"); s=pm.HalfNormal("s",2)
    pm.Normal("y",a+r[r_codes]+p[p_codes],s,observed=experiment_df["uniformity_percent"])
    models["additive"]=pm.sample(700,tune=700,chains=2,cores=1,random_seed=42,progressbar=False,idata_kwargs={"log_likelihood":True})
with pm.Model(coords={"recipe":recipes,"pressure":pressures}) as interaction_model:
    a=pm.Normal("a",95,3); r=pm.Normal("r",0,1,dims="recipe"); p=pm.Normal("p",0,1,dims="pressure")
    inter=pm.Normal("inter",0,.7,dims=("recipe","pressure")); s=pm.HalfNormal("s",2)
    pm.Normal("y",a+r[r_codes]+p[p_codes]+inter[r_codes,p_codes],s,observed=experiment_df["uniformity_percent"])
    models["interaction"]=pm.sample(700,tune=700,chains=2,cores=1,random_seed=42,progressbar=False,idata_kwargs={"log_likelihood":True})
print(az.compare(models))
