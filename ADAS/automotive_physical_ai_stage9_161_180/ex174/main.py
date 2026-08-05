import pymc as pm
from common.bayes_utils import load_data,sample_model,save_json
d=load_data(); x=(d["temperature_c"]-25).to_numpy(); y=d["accel_temp_measurement_mps2"].to_numpy()
with pm.Model() as model:
    intercept=pm.Normal("intercept",0,.1); coef=pm.Normal("temp_coef",0,.01); sigma=pm.HalfNormal("sigma",.1); pm.Normal("obs",intercept+coef*x,sigma,observed=y)
i=sample_model(model); r={"intercept":float(i.posterior["intercept"].mean()),"temp_coef":float(i.posterior["temp_coef"].mean())}; print(r); print(save_json(r,"ex174_temperature_correction.json"))
