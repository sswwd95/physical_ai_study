import pymc as pm
from common.reliability_utils import load_lifetime,sample_model,save_summary
df=load_lifetime()
y=df.loc[df["failure_event"]==1,"observed_time_h"].to_numpy()
with pm.Model() as model:
    alpha=pm.HalfNormal("shape_alpha",5)
    beta=pm.HalfNormal("scale_beta",2000)
    pm.Weibull("obs",alpha=alpha,beta=beta,observed=y)
idata=sample_model(model)
s,pth=save_summary(idata,["shape_alpha","scale_beta"],"ex286_weibull_summary.csv")
print(s); print(pth)
