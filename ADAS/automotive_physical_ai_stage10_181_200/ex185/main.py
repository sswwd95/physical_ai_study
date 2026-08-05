import pymc as pm
from common.bayes_slip_utils import load_data, sample_model, save_summary
df = load_data()
y = df.loc[df["surface"]=="dry", "slip_ratio"].to_numpy()
with pm.Model() as model:
    mu = pm.Normal("mu", mu=0.03, sigma=0.05)
    sigma = pm.HalfNormal("sigma", sigma=0.05)
    pm.Normal("obs", mu=mu, sigma=sigma, observed=y)
idata = sample_model(model)
summary, path = save_summary(idata, ["mu","sigma"], "ex185_dry_surface.csv")
print(summary)
print("saved:", path)
