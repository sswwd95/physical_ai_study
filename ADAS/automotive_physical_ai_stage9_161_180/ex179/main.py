import pymc as pm, arviz as az
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common.bayes_utils import load_data,sample_model,output_path
x=load_data()["accel_measurement_mps2"].to_numpy()
with pm.Model() as model:
    bias=pm.Normal("bias",0,.1); sigma=pm.HalfNormal("sigma",.1); pm.Normal("obs",bias,sigma,observed=x)
i=sample_model(model); az.plot_posterior(i,var_names=["bias","sigma"]); p=output_path("ex179_posterior.png"); plt.savefig(p,dpi=140); plt.close("all"); print(p)
