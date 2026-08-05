import numpy as np, pymc as pm
from common.risk_utils import load_data,standardize,sample_model
df=load_data(); x1=standardize(df["ttc_s"]).to_numpy(); x2=standardize(df["slip_ratio"]).to_numpy(); y=df["risk_label"].to_numpy()
with pm.Model() as model:
    a=pm.Normal("intercept",0,2); b1=pm.Normal("b_ttc",0,2); b2=pm.Normal("b_slip",0,2)
    p=pm.math.sigmoid(a+b1*x1+b2*x2); pm.Bernoulli("obs",p=p,observed=y)
idata=sample_model(model)
ttc=idata.posterior["b_ttc"].values.reshape(-1); slip=idata.posterior["b_slip"].values.reshape(-1)
print("P(TTC coefficient < 0):",np.mean(ttc<0))
print("P(slip coefficient > 0):",np.mean(slip>0))
