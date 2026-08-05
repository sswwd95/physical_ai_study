import pandas as pd
import pymc as pm
from common.bayes_slip_utils import load_data, sample_model, output_path
y = load_data()["distance_error_m"].to_numpy()
with pm.Model() as model:
    bias = pm.Normal("bias", 0.0, 0.20)
    sigma = pm.HalfNormal("sigma", 0.20)
    pm.Normal("obs", mu=bias, sigma=sigma, observed=y)
    idata = sample_model(model)
    ppc = pm.sample_posterior_predictive(idata, random_seed=42, progressbar=False, return_inferencedata=False)
pred = ppc["obs"].reshape(-1)
path = output_path("ex197_distance_error_ppc.csv")
pd.DataFrame({"predicted_distance_error_m":pred}).to_csv(path,index=False,encoding="utf-8-sig")
print("mean:", pred.mean(), "std:", pred.std())
print("saved:", path)
