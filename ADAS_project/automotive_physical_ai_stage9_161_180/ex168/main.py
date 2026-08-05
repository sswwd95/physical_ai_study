import numpy as np, pymc as pm
from common.bayes_utils import load_data,sample_model
x=load_data()["accel_measurement_mps2"].to_numpy()
with pm.Model() as model:
    bias=pm.Normal("bias",0,.1); sigma=pm.HalfNormal("sigma",.1); pm.Normal("obs",bias,sigma,observed=x)
s=sample_model(model).posterior["bias"].values.reshape(-1); p=float(np.mean(np.abs(s)>.04)); print("probability:",p,"decision:","RECALIBRATE" if p>.95 else "MONITOR")
