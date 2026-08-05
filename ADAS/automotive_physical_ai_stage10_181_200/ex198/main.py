import pymc as pm
import arviz as az
from common.bayes_slip_utils import load_data, sample_model, output_path
y = load_data()["slip_ratio"].to_numpy()
with pm.Model() as model:
    mu = pm.Normal("mu", 0.08, 0.08)
    sigma = pm.HalfNormal("sigma", 0.08)
    pm.Normal("obs", mu=mu, sigma=sigma, observed=y)
idata = sample_model(model)
summary = az.summary(idata, var_names=["mu","sigma"], round_to=6)
path = output_path("ex198_diagnostics.csv")
summary.to_csv(path, encoding="utf-8-sig")
print(summary[["r_hat","ess_bulk","ess_tail"]])
print("saved:", path)
