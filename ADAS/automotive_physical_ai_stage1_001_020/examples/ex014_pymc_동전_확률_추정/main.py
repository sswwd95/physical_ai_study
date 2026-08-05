import numpy as np
import pymc as pm

observed = np.array([1, 1, 0, 1, 0, 1, 1, 1, 0, 1])
with pm.Model() as model:
    theta = pm.Beta("theta", alpha=1, beta=1)
    pm.Bernoulli("obs", p=theta, observed=observed)
    idata = pm.sample(500, tune=500, chains=2, cores=1, random_seed=42, progressbar=False)
print("posterior mean:", float(idata.posterior["theta"].mean()))
