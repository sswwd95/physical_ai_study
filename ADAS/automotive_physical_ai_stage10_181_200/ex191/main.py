import pymc as pm
from common.bayes_slip_utils import load_data, sample_model, save_summary
df = load_data()
x = df["slip_ratio"].to_numpy()
y = df["distance_error_m"].to_numpy()
with pm.Model() as model:
    intercept = pm.Normal("intercept", mu=0.0, sigma=0.10)
    slope = pm.Normal("slope", mu=1.0, sigma=1.0)
    sigma = pm.HalfNormal("sigma", sigma=0.10)
    pm.Normal("obs", mu=intercept+slope*x, sigma=sigma, observed=y)
idata = sample_model(model)
summary, path = save_summary(idata, ["intercept","slope","sigma"], "ex191_slip_distance_regression.csv")
print(summary)
print("saved:", path)
