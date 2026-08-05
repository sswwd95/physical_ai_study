import pymc as pm, arviz as az
from common.bayes_utils import load_data,sample_model,output_path
x=load_data()["accel_measurement_mps2"].to_numpy()
with pm.Model() as model:
    bias=pm.Normal("bias",0,.1); sigma=pm.HalfNormal("sigma",.1); pm.Normal("obs",bias,sigma,observed=x)
i=sample_model(model); s=az.summary(i,var_names=["bias","sigma"]); p=output_path("ex178_diagnostics.csv"); s.to_csv(p); print(s[["r_hat","ess_bulk","ess_tail"]]); print(p)
