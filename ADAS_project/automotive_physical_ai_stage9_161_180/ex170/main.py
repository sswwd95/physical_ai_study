import pandas as pd, pymc as pm
from common.bayes_utils import load_data,sample_model,output_path
x=load_data()["accel_measurement_mps2"].to_numpy()
with pm.Model() as model:
    bias=pm.Normal("bias",0,.1); sigma=pm.HalfNormal("sigma",.1); pm.Normal("obs",bias,sigma,observed=x); idata=sample_model(model); ppc=pm.sample_posterior_predictive(idata,random_seed=42,progressbar=False,return_inferencedata=False)
p=output_path("ex170_posterior_predictive.csv"); pd.DataFrame({"predicted":ppc["obs"].reshape(-1)}).to_csv(p,index=False); print(p)
