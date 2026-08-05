import pymc as pm
import arviz as az
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common.bayes_slip_utils import load_data, sample_model, output_path
df = load_data()
with pm.Model() as model:
    slip_mu = pm.Normal("slip_mu", 0.08, 0.08)
    slip_sigma = pm.HalfNormal("slip_sigma", 0.08)
    dist_bias = pm.Normal("dist_bias", 0.0, 0.20)
    dist_sigma = pm.HalfNormal("dist_sigma", 0.20)
    pm.Normal("slip_obs", slip_mu, slip_sigma, observed=df["slip_ratio"].to_numpy())
    pm.Normal("dist_obs", dist_bias, dist_sigma, observed=df["distance_error_m"].to_numpy())
idata = sample_model(model)
az.plot_posterior(idata, var_names=["slip_mu","dist_bias"], hdi_prob=0.95)
path = output_path("ex199_posterior_plot.png")
plt.tight_layout()
plt.savefig(path, dpi=140)
plt.close("all")
print("saved:", path)
