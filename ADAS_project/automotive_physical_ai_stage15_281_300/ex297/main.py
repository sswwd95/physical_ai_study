import pandas as pd, pymc as pm
from common.reliability_utils import load_rul,standardize,sample_model,output_path
df=load_rul()
x1=standardize(df["age_h"]).to_numpy(); x2=standardize(df["health_score"]).to_numpy(); y=df["observed_rul_h"].to_numpy()
with pm.Model() as model:
    a=pm.Normal("intercept",600,500); b1=pm.Normal("age_coef",0,300); b2=pm.Normal("health_coef",0,300); sigma=pm.HalfNormal("sigma",200)
    pm.Normal("obs",mu=a+b1*x1+b2*x2,sigma=sigma,observed=y)
    idata=sample_model(model)
    ppc=pm.sample_posterior_predictive(idata,random_seed=42,progressbar=False,return_inferencedata=False)
pred=ppc["obs"].reshape(-1)
p=output_path("ex297_rul_posterior_predictive.csv")
pd.DataFrame({"predicted_rul_h":pred}).to_csv(p,index=False,encoding="utf-8-sig")
print(pred.mean(),pred.std(),p)
