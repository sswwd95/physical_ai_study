import numpy as np
import pymc as pm

rng = np.random.default_rng(42)
speed = rng.normal(0.50, 0.03, size=30)
with pm.Model() as model:
    mu = pm.Normal("mu", mu=0.5, sigma=0.2)
    sigma = pm.HalfNormal("sigma", sigma=0.1)
    pm.Normal("speed", mu=mu, sigma=sigma, observed=speed)
    idata = pm.sample(500, tune=500, chains=2, cores=1, random_seed=42, progressbar=False)
print("mu mean:", float(idata.posterior["mu"].mean()))
print("sigma mean:", float(idata.posterior["sigma"].mean()))
