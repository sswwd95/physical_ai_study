import pymc as pm
from common.risk_utils import load_data,standardize,sample_model,save_summary
df=load_data(); x=standardize(df["speed_mps"]).to_numpy(); y=df["risk_label"].to_numpy()
with pm.Model() as model:
    a=pm.Normal("intercept",0,2)
    b=pm.Normal("speed_coef",0,2)
    p=pm.math.sigmoid(a+b*x)
    pm.Bernoulli("obs",p=p,observed=y)
idata=sample_model(model)
s,pth=save_summary(idata,["intercept","speed_coef"],"ex247_speed_logistic.csv")
print(s); print(pth)
