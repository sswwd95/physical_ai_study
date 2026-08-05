import pymc as pm
from common.reliability_utils import load_lifetime,sample_model,save_summary
y=load_lifetime()["failure_event"].to_numpy()
with pm.Model() as model:
    p=pm.Beta("failure_probability",2,18)
    pm.Bernoulli("obs",p=p,observed=y)
idata=sample_model(model)
s,pth=save_summary(idata,["failure_probability"],"ex284_failure_probability.csv")
print(s); print(pth)
