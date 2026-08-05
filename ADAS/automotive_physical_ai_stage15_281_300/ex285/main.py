import pymc as pm
from common.reliability_utils import load_lifetime,sample_model,save_summary
df=load_lifetime(); cid=df["component_id"].to_numpy(); y=df["failure_event"].to_numpy(); n=int(df["component_id"].nunique())
with pm.Model() as model:
    p=pm.Beta("component_failure_probability",2,18,shape=n)
    pm.Bernoulli("obs",p=p[cid],observed=y)
idata=sample_model(model)
s,pth=save_summary(idata,["component_failure_probability"],"ex285_component_failure_probability.csv")
print(s); print(pth)
