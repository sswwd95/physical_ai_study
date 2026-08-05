import pymc as pm
from common.bayes_slip_utils import load_data, sample_model, save_summary
y = load_data()["slip_ratio"].to_numpy()
with pm.Model() as model:
    mu = pm.Normal("mu", mu=0.08, sigma=0.08)
    sigma = pm.HalfNormal("sigma", sigma=0.08)
    pm.Normal("obs", mu=mu, sigma=sigma, observed=y)
idata = sample_model(model)
summary, path = save_summary(idata, ["mu","sigma"], "ex184_slip_mean_sigma.csv")
print(summary)
print("saved:", path)
