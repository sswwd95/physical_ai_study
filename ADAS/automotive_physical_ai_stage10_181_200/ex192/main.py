import pymc as pm
from common.bayes_slip_utils import load_data, sample_model, save_summary
df = load_data()
x = df["imu_accel_std"].to_numpy()
y = df["slip_ratio"].to_numpy()
x = (x - x.mean()) / x.std()
with pm.Model() as model:
    intercept = pm.Normal("intercept", 0.08, 0.08)
    slope = pm.Normal("slope", 0.0, 0.20)
    sigma = pm.HalfNormal("sigma", 0.08)
    pm.Normal("obs", mu=intercept+slope*x, sigma=sigma, observed=y)
idata = sample_model(model)
summary, path = save_summary(idata, ["intercept","slope","sigma"], "ex192_imu_slip_regression.csv")
print(summary)
print("saved:", path)
