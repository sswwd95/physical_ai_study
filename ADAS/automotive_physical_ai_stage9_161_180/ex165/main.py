import pymc as pm
from common.bayes_utils import load_data,sample_model,save_summary
x=load_data()["accel_measurement_mps2"].to_numpy()
with pm.Model() as model:
    bias=pm.Normal("bias",0,.1); sigma=pm.HalfNormal("sigma",.1); pm.Normal("obs",bias,sigma,observed=x)
idata=sample_model(model); s,p=save_summary(idata,["bias","sigma"],"ex165_bias_sigma_summary.csv"); print(s); print(p)
