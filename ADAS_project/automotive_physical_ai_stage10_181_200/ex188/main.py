import numpy as np
import pymc as pm
from common.bayes_slip_utils import load_data, sample_model
y = load_data()["slip_ratio"].to_numpy()
with pm.Model() as model:
    mu = pm.Normal("mu", mu=0.08, sigma=0.08)
    sigma = pm.HalfNormal("sigma", sigma=0.08)
    pm.Normal("obs", mu=mu, sigma=sigma, observed=y)
idata = sample_model(model)
samples = idata.posterior["mu"].values.reshape(-1)
print("P(mean slip > 0.08):", float(np.mean(samples > 0.08)))
