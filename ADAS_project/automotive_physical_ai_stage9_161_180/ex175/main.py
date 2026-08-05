import pymc as pm
from common.bayes_utils import load_data,sample_model,save_summary
d=load_data(); dev=d["device_id"].to_numpy(); y=d["hier_measurement_mps2"].to_numpy(); n=int(d["device_id"].nunique())
with pm.Model() as model:
    gm=pm.Normal("group_mu",0,.1); gs=pm.HalfNormal("group_sigma",.05); db=pm.Normal("device_bias",gm,gs,shape=n); sigma=pm.HalfNormal("sigma",.1); pm.Normal("obs",db[dev],sigma,observed=y)
i=sample_model(model); s,p=save_summary(i,["group_mu","group_sigma","device_bias"],"ex175_hierarchical.csv"); print(s); print(p)
