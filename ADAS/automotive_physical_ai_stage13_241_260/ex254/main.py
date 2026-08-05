import pymc as pm
from common.risk_utils import load_data,sample_model,save_summary
df=load_data(); sid=df["surface_id"].to_numpy(); did=df["driver_id"].to_numpy(); y=df["risk_label"].to_numpy()
ns=int(df["surface_id"].nunique()); nd=int(df["driver_id"].nunique())
with pm.Model() as model:
    a=pm.Normal("intercept",0,2)
    se=pm.Normal("surface_effect",0,1,shape=ns)
    de=pm.Normal("driver_effect",0,1,shape=nd)
    p=pm.math.sigmoid(a+se[sid]+de[did])
    pm.Bernoulli("obs",p=p,observed=y)
idata=sample_model(model)
s,pth=save_summary(idata,["intercept","surface_effect","driver_effect"],"ex254_surface_driver_effects.csv")
print(s); print(pth)
