import numpy as np, pymc as pm
from common.reliability_utils import load_lifetime,standardize,sample_model,save_summary
df=load_lifetime().query("failure_event==1")
x=standardize(df["temperature_c"]).to_numpy()
y=np.log(df["observed_time_h"].to_numpy())
with pm.Model() as model:
    a=pm.Normal("intercept",7,1)
    b=pm.Normal("temperature_coef",0,1)
    sigma=pm.HalfNormal("sigma",1)
    pm.Normal("obs",mu=a+b*x,sigma=sigma,observed=y)
idata=sample_model(model)
s,pth=save_summary(idata,["intercept","temperature_coef","sigma"],"ex292_temperature_lifetime_regression.csv")
print(s); print(pth)
