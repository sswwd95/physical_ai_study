import pymc as pm
from common.risk_utils import load_data,standardize,sample_model,save_summary
df=load_data(); x=standardize(df["ttc_s"]).to_numpy(); y=df["risk_label"].to_numpy()
with pm.Model() as model:
    a=pm.Normal("intercept",0,2)
    b=pm.Normal("ttc_coef",0,2)
    p=pm.math.sigmoid(a+b*x)
    pm.Bernoulli("obs",p=p,observed=y)
idata=sample_model(model)
s,pth=save_summary(idata,["intercept","ttc_coef"],"ex248_ttc_logistic.csv")
print(s); print(pth)
