import pandas as pd, pymc as pm
from common.risk_utils import load_data,standardize,sample_model,output_path
df=load_data(); x1=standardize(df["ttc_s"]).to_numpy(); x2=standardize(df["slip_ratio"]).to_numpy(); y=df["risk_label"].to_numpy()
with pm.Model() as model:
    a=pm.Normal("intercept",0,2); b1=pm.Normal("b_ttc",0,2); b2=pm.Normal("b_slip",0,2)
    p=pm.Deterministic("risk_probability",pm.math.sigmoid(a+b1*x1+b2*x2))
    pm.Bernoulli("obs",p=p,observed=y)
idata=sample_model(model)
prob=idata.posterior["risk_probability"].mean(dim=("chain","draw")).values
out=df[["sample_id","risk_label"]].copy(); out["posterior_risk_probability"]=prob
pth=output_path("ex255_posterior_risk_probability.csv"); out.to_csv(pth,index=False,encoding="utf-8-sig")
print(out.head()); print(pth)
