import json, numpy as np, pymc as pm, arviz as az
from common.reliability_utils import load_lifetime,load_rul,standardize,sample_model,output_path
life=load_lifetime(); rul=load_rul()
y_fail=life["failure_event"].to_numpy()
x_age=standardize(rul["age_h"]).to_numpy()
x_health=standardize(rul["health_score"]).to_numpy()
y_rul=rul["observed_rul_h"].to_numpy()
with pm.Model() as model:
    failure_p=pm.Beta("failure_probability",2,18)
    pm.Bernoulli("failure_obs",p=failure_p,observed=y_fail)
    a=pm.Normal("rul_intercept",600,500)
    b1=pm.Normal("b_age",0,300)
    b2=pm.Normal("b_health",0,300)
    sigma=pm.HalfNormal("rul_sigma",200)
    pm.Normal("rul_obs",mu=a+b1*x_age+b2*x_health,sigma=sigma,observed=y_rul)
idata=sample_model(model)
summary=az.summary(idata,var_names=["failure_probability","rul_intercept","b_age","b_health","rul_sigma"],round_to=6)
sp=output_path("ex300_posterior_summary.csv"); summary.to_csv(sp,encoding="utf-8-sig")
fp=idata.posterior["failure_probability"].values.reshape(-1)
report={
    "observed_failure_rate":float(life["failure_event"].mean()),
    "posterior_failure_probability_mean":float(fp.mean()),
    "posterior_failure_probability_hdi_95":[float(v) for v in np.quantile(fp,[.025,.975])],
    "prob_failure_probability_gt_0_20":float(np.mean(fp>.20)),
    "median_observed_rul_h":float(rul["observed_rul_h"].median()),
    "max_r_hat":float(summary["r_hat"].max()),
    "min_ess_bulk":float(summary["ess_bulk"].min()),
}
rp=output_path("ex300_integrated_report.json")
rp.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
print(report); print(sp,rp)
