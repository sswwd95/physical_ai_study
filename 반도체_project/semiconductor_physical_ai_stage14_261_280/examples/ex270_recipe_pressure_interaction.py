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
with pm.Model(coords={"recipe":recipes,"pressure":pressures}) as model:
    a=pm.Normal("a",95,3)
    r_eff=pm.Normal("r_eff",0,1,dims="recipe")
    p_eff=pm.Normal("p_eff",0,1,dims="pressure")
    interaction=pm.Normal("interaction",0,.7,dims=("recipe","pressure"))
    sigma=pm.HalfNormal("sigma",2)
    mu=a+r_eff[r_codes]+p_eff[p_codes]+interaction[r_codes,p_codes]
    pm.Normal("y",mu,sigma,observed=experiment_df["uniformity_percent"])
    idata=pm.sample(1000,tune=1000,chains=2,cores=1,target_accept=.9,random_seed=42,progressbar=False)
print(az.summary(idata,var_names=["interaction"],hdi_prob=.94))
