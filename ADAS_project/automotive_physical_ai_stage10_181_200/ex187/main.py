import pymc as pm
from common.bayes_slip_utils import load_data, sample_model, save_summary
df = load_data()
sid = df["surface_id"].to_numpy()
y = df["slip_ratio"].to_numpy()
n_surface = int(df["surface_id"].nunique())
with pm.Model() as model:
    surface_mu = pm.Normal("surface_mu", mu=0.08, sigma=0.08, shape=n_surface)
    sigma = pm.HalfNormal("sigma", sigma=0.08)
    pm.Normal("obs", mu=surface_mu[sid], sigma=sigma, observed=y)
idata = sample_model(model)
summary, path = save_summary(idata, ["surface_mu","sigma"], "ex187_surface_compare.csv")
print(summary)
print("saved:", path)
