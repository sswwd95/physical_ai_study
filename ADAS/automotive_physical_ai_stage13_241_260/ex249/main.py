import pymc as pm
from common.risk_utils import load_data,standardize,sample_model,save_summary
df=load_data()
X={
"speed":standardize(df["speed_mps"]).to_numpy(),
"accel":standardize(df["abs_accel_mps2"]).to_numpy(),
"steer":standardize(df["abs_steering_deg"]).to_numpy(),
"ttc":standardize(df["ttc_s"]).to_numpy(),
"slip":standardize(df["slip_ratio"]).to_numpy()}
y=df["risk_label"].to_numpy()
with pm.Model() as model:
    a=pm.Normal("intercept",0,2)
    bs=pm.Normal("b_speed",0,2); ba=pm.Normal("b_accel",0,2); bt=pm.Normal("b_steer",0,2)
    bttc=pm.Normal("b_ttc",0,2); bslip=pm.Normal("b_slip",0,2)
    p=pm.math.sigmoid(a+bs*X["speed"]+ba*X["accel"]+bt*X["steer"]+bttc*X["ttc"]+bslip*X["slip"])
    pm.Bernoulli("obs",p=p,observed=y)
idata=sample_model(model)
vars=["intercept","b_speed","b_accel","b_steer","b_ttc","b_slip"]
s,pth=save_summary(idata,vars,"ex249_multifeature_logistic.csv")
print(s); print(pth)
