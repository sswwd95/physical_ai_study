import pymc as pm
from common.reliability_utils import load_rul,standardize,sample_model,save_summary
df=load_rul()
x1=standardize(df["age_h"]).to_numpy()
x2=standardize(df["health_score"]).to_numpy()
y=df["observed_rul_h"].to_numpy()
with pm.Model() as model:
    a=pm.Normal("intercept",600,500)
    b1=pm.Normal("age_coef",0,300)
    b2=pm.Normal("health_coef",0,300)
    sigma=pm.HalfNormal("sigma",200)
    pm.Normal("obs",mu=a+b1*x1+b2*x2,sigma=sigma,observed=y)
idata=sample_model(model)
s,pth=save_summary(idata,["intercept","age_coef","health_coef","sigma"],"ex295_rul_regression.csv")
print(s); print(pth)
