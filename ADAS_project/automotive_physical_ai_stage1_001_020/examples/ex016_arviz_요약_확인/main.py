import numpy as np
import pymc as pm
import arviz as az

y = np.array([0.48, 0.51, 0.50, 0.47, 0.53])
with pm.Model():
    mu = pm.Normal("mu", 0.5, 0.1)
    sigma = pm.HalfNormal("sigma", 0.1)
    pm.Normal("y", mu, sigma, observed=y)
    idata = pm.sample(400, tune=400, chains=2, cores=1, random_seed=7, progressbar=False)
print(az.summary(idata, var_names=["mu", "sigma"]))
