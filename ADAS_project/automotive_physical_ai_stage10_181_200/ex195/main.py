import pymc as pm
from common.bayes_slip_utils import load_data, sample_model, save_summary
df = load_data()
sid = df["surface_id"].to_numpy()
y = df["slip_ratio"].to_numpy()
n = int(df["surface_id"].nunique())
with pm.Model() as model:
    group_mu = pm.Normal("group_mu", 0.08, 0.08)
    group_sigma = pm.HalfNormal("group_sigma", 0.08)
    surface_mu = pm.Normal("surface_mu", group_mu, group_sigma, shape=n)
    sigma = pm.HalfNormal("sigma", 0.08)
    pm.Normal("obs", mu=surface_mu[sid], sigma=sigma, observed=y)
idata = sample_model(model)
summary, path = save_summary(idata, ["group_mu","group_sigma","surface_mu","sigma"], "ex195_hierarchical_surface.csv")
print(summary)
print("saved:", path)
