import pymc as pm
from common.reliability_utils import load_lifetime,sample_model,save_summary
df=load_lifetime(); y=df[(df["component"]=="motor")&(df["failure_event"]==1)]["observed_time_h"].to_numpy()
with pm.Model() as model:
    alpha=pm.HalfNormal("alpha",5)
    beta=pm.HalfNormal("beta",2000)
    pm.Weibull("obs",alpha=alpha,beta=beta,observed=y)
idata=sample_model(model)
s,pth=save_summary(idata,["alpha","beta"],"ex287_motor_weibull.csv")
print(s); print(pth)
