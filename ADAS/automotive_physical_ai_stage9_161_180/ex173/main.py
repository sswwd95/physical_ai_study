import pymc as pm
from common.bayes_utils import load_data,sample_model,save_summary
d=load_data(); x=(d["temperature_c"]-25).to_numpy(); y=d["accel_temp_measurement_mps2"].to_numpy()
with pm.Model() as model:
    intercept=pm.Normal("intercept",0,.1); coef=pm.Normal("temp_coef",0,.01); sigma=pm.HalfNormal("sigma",.1); pm.Normal("obs",intercept+coef*x,sigma,observed=y)
idata=sample_model(model); s,p=save_summary(idata,["intercept","temp_coef","sigma"],"ex173_temperature.csv"); print(s); print(p)
