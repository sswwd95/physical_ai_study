import pymc as pm, arviz as az
from common.reliability_utils import load_rul,standardize,sample_model,output_path
df=load_rul(); x=standardize(df["age_h"]).to_numpy(); y=df["observed_rul_h"].to_numpy()
with pm.Model() as model:
    a=pm.Normal("intercept",600,500); b=pm.Normal("age_coef",0,300); sigma=pm.HalfNormal("sigma",200)
    pm.Normal("obs",mu=a+b*x,sigma=sigma,observed=y)
idata=sample_model(model)
s=az.summary(idata,var_names=["intercept","age_coef","sigma"],round_to=6)
p=output_path("ex299_diagnostics.csv"); s.to_csv(p,encoding="utf-8-sig")
print(s[["r_hat","ess_bulk","ess_tail"]]); print(p)
