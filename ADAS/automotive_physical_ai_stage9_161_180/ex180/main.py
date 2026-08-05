import json, numpy as np, pymc as pm, arviz as az
from common.bayes_utils import load_data,sample_model,output_path
d=load_data(); a=d["accel_measurement_mps2"].to_numpy(); g=d["gyro_measurement_rps"].to_numpy()
with pm.Model() as model:
    ab=pm.Normal("accel_bias",0,.1); ass=pm.HalfNormal("accel_sigma",.1); gb=pm.Normal("gyro_bias",0,.05); gs=pm.HalfNormal("gyro_sigma",.03); pm.Normal("a",ab,ass,observed=a); pm.Normal("g",gb,gs,observed=g)
i=sample_model(model); s=az.summary(i,var_names=["accel_bias","accel_sigma","gyro_bias","gyro_sigma"]); sp=output_path("ex180_summary.csv"); s.to_csv(sp)
asamp=i.posterior["accel_bias"].values.reshape(-1); gsamp=i.posterior["gyro_bias"].values.reshape(-1); r={"accel_bias_mean":float(asamp.mean()),"gyro_bias_mean":float(gsamp.mean()),"P_abs_accel_gt_0_04":float(np.mean(np.abs(asamp)>.04)),"max_r_hat":float(s["r_hat"].max())}; rp=output_path("ex180_report.json"); rp.write_text(json.dumps(r,indent=2)); print(r); print(sp,rp)
