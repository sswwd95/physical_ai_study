from pathlib import Path
import numpy as np
import pandas as pd
import pymc as pm
import arviz as az

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "bayesian_sensor_fusion.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

sensor_df = pd.read_csv(DATA_FILE)

temp_res=(sensor_df["temp_sensor_a_c"]-sensor_df["true_temperature_c"]).dropna().to_numpy()
pressure_res=(sensor_df["pressure_sensor_a_pa"]-sensor_df["true_pressure_pa"]).dropna().to_numpy()

with pm.Model() as temp_model:
    temp_mu=pm.Normal("temp_mu",0,2); temp_sigma=pm.HalfNormal("temp_sigma",1)
    pm.Normal("temp_r",temp_mu,temp_sigma,observed=temp_res)
    temp_idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)

with pm.Model() as pressure_model:
    pressure_mu=pm.Normal("pressure_mu",0,1); pressure_sigma=pm.HalfNormal("pressure_sigma",.5)
    pm.Normal("pressure_r",pressure_mu,pressure_sigma,observed=pressure_res)
    pressure_idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)

temp_summary=az.summary(temp_idata,var_names=["temp_mu","temp_sigma"],hdi_prob=.94)
pressure_summary=az.summary(pressure_idata,var_names=["pressure_mu","pressure_sigma"],hdi_prob=.94)

stream=sensor_df[["timestamp","process_phase"]].copy()
temp_b_res=(sensor_df["temp_sensor_b_c"]-sensor_df["true_temperature_c"])
pressure_b_res=(sensor_df["pressure_sensor_b_pa"]-sensor_df["true_pressure_pa"])
stream["temp_anomaly_score"]=np.abs(temp_b_res)/(temp_b_res.dropna().std()+1e-9)
stream["pressure_anomaly_score"]=np.abs(pressure_b_res)/(pressure_b_res.dropna().std()+1e-9)
stream["review_required"]=(stream["temp_anomaly_score"]>3)|(stream["pressure_anomaly_score"]>3)

phase_summary=stream.groupby("process_phase")[["temp_anomaly_score","pressure_anomaly_score","review_required"]].mean()

with pd.ExcelWriter(OUTPUT_DIR/"ex340_bayesian_twin_report.xlsx",engine="openpyxl") as w:
    temp_summary.to_excel(w,sheet_name="temperature_posterior")
    pressure_summary.to_excel(w,sheet_name="pressure_posterior")
    phase_summary.to_excel(w,sheet_name="phase_summary")
    stream.to_excel(w,sheet_name="anomaly_stream",index=False)

print("보고서 저장 완료")
