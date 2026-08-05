import pymc as pm
from common.bayes_slip_utils import load_data, sample_model, save_summary
df = load_data()
y = df.loc[df["surface"]=="wet", "slip_ratio"].to_numpy()
with pm.Model() as model:
    mu = pm.Normal("mu", mu=0.10, sigma=0.08)
    sigma = pm.HalfNormal("sigma", sigma=0.08)
    pm.Normal("obs", mu=mu, sigma=sigma, observed=y)
idata = sample_model(model)
summary, path = save_summary(idata, ["mu","sigma"], "ex186_wet_surface.csv")
print(summary)
print("saved:", path)
