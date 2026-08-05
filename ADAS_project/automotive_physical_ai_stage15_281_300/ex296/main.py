import pymc as pm
from common.reliability_utils import load_rul,standardize,sample_model,save_summary
df=load_rul()
x1=standardize(df["age_h"]).to_numpy()
x2=standardize(df["health_score"]).to_numpy()
x3=standardize(df["vibration_g"]).to_numpy()
x4=standardize(df["temperature_c"]).to_numpy()
x5=standardize(df["internal_resistance_ohm"]).to_numpy()
y=df["observed_rul_h"].to_numpy()
with pm.Model() as model:
    a=pm.Normal("intercept",600,500)
    b1=pm.Normal("b_age",0,300); b2=pm.Normal("b_health",0,300)
    b3=pm.Normal("b_vibration",0,300); b4=pm.Normal("b_temperature",0,300)
    b5=pm.Normal("b_resistance",0,300); sigma=pm.HalfNormal("sigma",200)
    mu=a+b1*x1+b2*x2+b3*x3+b4*x4+b5*x5
    pm.Normal("obs",mu=mu,sigma=sigma,observed=y)
idata=sample_model(model)
vars=["intercept","b_age","b_health","b_vibration","b_temperature","b_resistance","sigma"]
s,pth=save_summary(idata,vars,"ex296_multisensor_rul.csv")
print(s); print(pth)
