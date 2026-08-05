import pymc as pm
from common.risk_utils import load_data,sample_model,save_summary
df=load_data(); did=df["driver_id"].to_numpy(); y=df["risk_label"].to_numpy(); n=int(df["driver_id"].nunique())
with pm.Model() as model:
    group_mu=pm.Normal("group_mu",0,1.5)
    group_sigma=pm.HalfNormal("group_sigma",1)
    driver_logit=pm.Normal("driver_logit",group_mu,group_sigma,shape=n)
    p=pm.math.sigmoid(driver_logit[did])
    pm.Bernoulli("obs",p=p,observed=y)
idata=sample_model(model)
s,pth=save_summary(idata,["group_mu","group_sigma","driver_logit"],"ex253_driver_hierarchical.csv")
print(s); print(pth)
