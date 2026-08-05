import numpy as np, pymc as pm
from common.reliability_utils import load_lifetime,sample_model,save_summary
df=load_lifetime().query("failure_event==1")
cid=df["component_id"].to_numpy()
y=np.log(df["observed_time_h"].to_numpy())
n=int(df["component_id"].nunique())
with pm.Model() as model:
    group_mu=pm.Normal("group_mu",7,1)
    group_sigma=pm.HalfNormal("group_sigma",1)
    comp_mu=pm.Normal("component_mu",group_mu,group_sigma,shape=n)
    sigma=pm.HalfNormal("sigma",1)
    pm.Normal("obs",mu=comp_mu[cid],sigma=sigma,observed=y)
idata=sample_model(model)
s,pth=save_summary(idata,["group_mu","group_sigma","component_mu","sigma"],"ex293_hierarchical_lifetime.csv")
print(s); print(pth)
