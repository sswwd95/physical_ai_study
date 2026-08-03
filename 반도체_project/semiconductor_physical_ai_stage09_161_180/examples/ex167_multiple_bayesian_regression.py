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

features=["temp_mean_c","pressure_mean_pa","particle_mean","vibration_rms_g","maintenance_age_hours"]
X=sensor_df[features]
X=(X-X.mean())/X.std()
with pm.Model(coords={"feature":features}) as model:
    alpha=pm.Normal("alpha",94,5)
    beta=pm.Normal("beta",0,1,dims="feature")
    sigma=pm.HalfNormal("sigma",3)
    mu=alpha+pm.math.dot(X.to_numpy(),beta)
    pm.Normal("y",mu,sigma,observed=sensor_df["yield_percent"])
    idata=pm.sample(1000,tune=1000,chains=2,cores=1,random_seed=42,progressbar=False)

summary=az.summary(idata,var_names=["beta"],hdi_prob=0.94)
print(summary)
summary.to_csv(OUTPUT_DIR/"ex167_multiple_regression.csv",encoding="utf-8-sig")
