from pathlib import Path
import numpy as np
import pandas as pd
import pymc as pm
import arviz as az

ROOT = Path(__file__).resolve().parents[1]
LIFE_FILE = ROOT / "data" / "bayesian_equipment_lifetime.csv"
RUL_FILE = ROOT / "data" / "bayesian_rul_snapshots.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

life_df = pd.read_csv(LIFE_FILE)
rul_df = pd.read_csv(RUL_FILE)

features=["cycle","vibration_rms_g","temperature_c","motor_current_a","particle_count"]
X=rul_df[features]; X=(X-X.mean())/X.std(); y=rul_df["rul_cycles"].to_numpy()
with pm.Model(coords={"feature":features}) as model:
    a=pm.Normal("a",80,40); beta=pm.Normal("beta",0,20,dims="feature"); sigma=pm.HalfNormal("sigma",20)
    mu=a+pm.math.dot(X.to_numpy(),beta)
    pm.Normal("rul",mu,sigma,observed=y)
    idata=pm.sample(1000,tune=1000,chains=2,cores=1,random_seed=42,progressbar=False)
print(az.summary(idata,var_names=["a","beta","sigma"],hdi_prob=.94))
