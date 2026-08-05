import pymc as pm
from common.bayes_slip_utils import load_data, sample_model, save_summary
y = load_data()["distance_error_m"].to_numpy()
with pm.Model() as model:
    bias = pm.Normal("bias", mu=0.0, sigma=0.20)
    sigma = pm.HalfNormal("sigma", sigma=0.20)
    pm.Normal("obs", mu=bias, sigma=sigma, observed=y)
idata = sample_model(model)
summary, path = save_summary(idata, ["bias","sigma"], "ex189_distance_error.csv")
print(summary)
print("saved:", path)
