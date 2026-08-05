import pymc as pm
from common.risk_utils import load_data,sample_model,save_summary
df=load_data(); sid=df["surface_id"].to_numpy(); y=df["risk_label"].to_numpy(); n=int(df["surface_id"].nunique())
with pm.Model() as model:
    logits=pm.Normal("surface_logit",0,2,shape=n)
    p=pm.Deterministic("surface_p",pm.math.sigmoid(logits))
    pm.Bernoulli("obs",p=p[sid],observed=y)
idata=sample_model(model)
s,pth=save_summary(idata,["surface_p"],"ex251_surface_risk.csv")
print(s); print(pth)
