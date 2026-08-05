import numpy as np, pymc as pm
from common.bayes_utils import load_data,sample_model
d=load_data(); a=d["sensor_a_mps2"].to_numpy(); b=d["sensor_b_mps2"].to_numpy()
with pm.Model() as model:
    ma=pm.Normal("mu_a",0,.1); mb=pm.Normal("mu_b",0,.1); sa=pm.HalfNormal("sigma_a",.1); sb=pm.HalfNormal("sigma_b",.1); delta=pm.Deterministic("delta",mb-ma); pm.Normal("a",ma,sa,observed=a); pm.Normal("b",mb,sb,observed=b)
s=sample_model(model).posterior["delta"].values.reshape(-1); print("P(B>A):",np.mean(s>0))
