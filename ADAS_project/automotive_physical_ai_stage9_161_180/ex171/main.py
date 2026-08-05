import pymc as pm
from common.bayes_utils import load_data,sample_model,save_summary
d=load_data(); a=d["sensor_a_mps2"].to_numpy(); b=d["sensor_b_mps2"].to_numpy()
with pm.Model() as model:
    ma=pm.Normal("mu_a",0,.1); mb=pm.Normal("mu_b",0,.1); sa=pm.HalfNormal("sigma_a",.1); sb=pm.HalfNormal("sigma_b",.1); delta=pm.Deterministic("delta",mb-ma); pm.Normal("obs_a",ma,sa,observed=a); pm.Normal("obs_b",mb,sb,observed=b)
idata=sample_model(model); s,p=save_summary(idata,["mu_a","mu_b","delta"],"ex171_sensor_compare.csv"); print(s); print(p)
