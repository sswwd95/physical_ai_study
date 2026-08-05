import numpy as np, pymc as pm
from common.risk_utils import load_data,sample_model
y=load_data()["risk_label"].to_numpy()
with pm.Model() as model:
    p=pm.Beta("p",2,8)
    pm.Bernoulli("obs",p=p,observed=y)
samples=sample_model(model).posterior["p"].values.reshape(-1)
print("mean:",samples.mean())
print("95% credible interval:",np.quantile(samples,[.025,.975]))
