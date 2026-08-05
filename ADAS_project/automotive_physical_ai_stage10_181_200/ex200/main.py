import json
import numpy as np
import pymc as pm
import arviz as az
from common.bayes_slip_utils import load_data, sample_model, output_path
df = load_data()
with pm.Model() as model:
    slip_mu = pm.Normal("slip_mu", 0.08, 0.08)
    slip_sigma = pm.HalfNormal("slip_sigma", 0.08)
    dist_bias = pm.Normal("dist_bias", 0.0, 0.20)
    dist_sigma = pm.HalfNormal("dist_sigma", 0.20)
    yaw_bias = pm.Normal("yaw_bias", 0.0, 0.20)
    yaw_sigma = pm.HalfNormal("yaw_sigma", 0.20)
    pm.Normal("slip_obs", slip_mu, slip_sigma, observed=df["slip_ratio"].to_numpy())
    pm.Normal("dist_obs", dist_bias, dist_sigma, observed=df["distance_error_m"].to_numpy())
    pm.Normal("yaw_obs", yaw_bias, yaw_sigma, observed=df["yaw_error_rad"].to_numpy())
idata = sample_model(model)
summary = az.summary(
    idata,
    var_names=["slip_mu","slip_sigma","dist_bias","dist_sigma","yaw_bias","yaw_sigma"],
    round_to=6
)
summary_path = output_path("ex200_integrated_summary.csv")
summary.to_csv(summary_path, encoding="utf-8-sig")
slip_samples = idata.posterior["slip_mu"].values.reshape(-1)
dist_samples = idata.posterior["dist_bias"].values.reshape(-1)
yaw_samples = idata.posterior["yaw_bias"].values.reshape(-1)
report = {
    "slip_mean": float(slip_samples.mean()),
    "slip_hdi_95": [float(v) for v in np.quantile(slip_samples,[0.025,0.975])],
    "distance_bias_mean_m": float(dist_samples.mean()),
    "yaw_bias_mean_rad": float(yaw_samples.mean()),
    "prob_mean_slip_gt_0_08": float(np.mean(slip_samples > 0.08)),
    "prob_distance_bias_gt_0_05": float(np.mean(dist_samples > 0.05)),
    "max_r_hat": float(summary["r_hat"].max()),
    "min_ess_bulk": float(summary["ess_bulk"].min()),
}
report_path = output_path("ex200_integrated_report.json")
report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
print(report)
print("saved:", summary_path, report_path)
