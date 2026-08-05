import pymc as pm
from common.risk_utils import load_data,sample_model,save_summary
df=load_data(); did=df["driver_id"].to_numpy(); y=df["risk_label"].to_numpy(); n=int(df["driver_id"].nunique())
with pm.Model() as model:
    logits=pm.Normal("driver_logit",0,2,shape=n)
    p=pm.Deterministic("driver_p",pm.math.sigmoid(logits))
    pm.Bernoulli("obs",p=p[did],observed=y)
idata=sample_model(model)
s,pth=save_summary(idata,["driver_p"],"ex252_driver_risk.csv")
print(s); print(pth)
