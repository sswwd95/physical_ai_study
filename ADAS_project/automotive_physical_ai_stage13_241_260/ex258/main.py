import pymc as pm, arviz as az
from common.risk_utils import load_data,standardize,sample_model,output_path
df=load_data(); x=standardize(df["ttc_s"]).to_numpy(); y=df["risk_label"].to_numpy()
with pm.Model() as model:
    a=pm.Normal("intercept",0,2); b=pm.Normal("ttc_coef",0,2)
    p=pm.math.sigmoid(a+b*x); pm.Bernoulli("obs",p=p,observed=y)
idata=sample_model(model)
s=az.summary(idata,var_names=["intercept","ttc_coef"],round_to=6)
pth=output_path("ex258_diagnostics.csv"); s.to_csv(pth,encoding="utf-8-sig")
print(s[["r_hat","ess_bulk","ess_tail"]]); print(pth)
