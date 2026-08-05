import json, numpy as np, pandas as pd, pymc as pm, arviz as az
from common.risk_utils import load_data,standardize,sample_model,classification_metrics,output_path
df=load_data()
x1=standardize(df["speed_mps"]).to_numpy()
x2=standardize(df["abs_accel_mps2"]).to_numpy()
x3=standardize(df["ttc_s"]).to_numpy()
x4=standardize(df["slip_ratio"]).to_numpy()
y=df["risk_label"].to_numpy()
with pm.Model() as model:
    a=pm.Normal("intercept",0,2)
    b1=pm.Normal("b_speed",0,2); b2=pm.Normal("b_accel",0,2)
    b3=pm.Normal("b_ttc",0,2); b4=pm.Normal("b_slip",0,2)
    p=pm.Deterministic("risk_probability",pm.math.sigmoid(a+b1*x1+b2*x2+b3*x3+b4*x4))
    pm.Bernoulli("obs",p=p,observed=y)
idata=sample_model(model)
summary=az.summary(idata,var_names=["intercept","b_speed","b_accel","b_ttc","b_slip"],round_to=6)
summary_path=output_path("ex260_posterior_summary.csv"); summary.to_csv(summary_path,encoding="utf-8-sig")
prob=idata.posterior["risk_probability"].mean(dim=("chain","draw")).values
best=None
for th in [i/100 for i in range(5,96,5)]:
    m=classification_metrics(y,prob,th); m["cost"]=m["fn"]*10+m["fp"]*2
    if best is None or m["cost"]<best["cost"]: best=m
pred=df[["sample_id","driver","surface","risk_label","severity"]].copy()
pred["posterior_risk_probability"]=prob
pred["predicted_risk"]=(prob>=best["threshold"]).astype(int)
pred_path=output_path("ex260_risk_predictions.csv"); pred.to_csv(pred_path,index=False,encoding="utf-8-sig")
report={
    "samples":len(df),
    "observed_risk_rate":float(df["risk_label"].mean()),
    "best_threshold":best["threshold"],
    "cost_metrics":best,
    "max_r_hat":float(summary["r_hat"].max()),
    "min_ess_bulk":float(summary["ess_bulk"].min()),
    "coef_probability":{
        "speed_positive":float(np.mean(idata.posterior["b_speed"].values.reshape(-1)>0)),
        "accel_positive":float(np.mean(idata.posterior["b_accel"].values.reshape(-1)>0)),
        "ttc_negative":float(np.mean(idata.posterior["b_ttc"].values.reshape(-1)<0)),
        "slip_positive":float(np.mean(idata.posterior["b_slip"].values.reshape(-1)>0))
    }
}
report_path=output_path("ex260_integrated_report.json")
report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
print(report)
print("saved:",summary_path,pred_path,report_path)
