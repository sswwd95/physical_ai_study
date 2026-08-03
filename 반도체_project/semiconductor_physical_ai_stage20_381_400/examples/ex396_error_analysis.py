from pathlib import Path
import json
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "final_project_data.csv"
CONFIG_FILE = ROOT / "config" / "project_config.json"
OUTPUT_DIR = ROOT / "outputs"
MODEL_DIR = ROOT / "models"
REPORT_DIR = ROOT / "reports"
PORTFOLIO_DIR = ROOT / "portfolio"

for directory in [OUTPUT_DIR, MODEL_DIR, REPORT_DIR, PORTFOLIO_DIR]:
    directory.mkdir(exist_ok=True)

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
data=pd.read_csv(DATA_FILE)
features=["temperature_c","pressure_pa","vibration_rms_g","particle_count","rf_power_w","gas_flow_sccm","cycle_time_min","maintenance_age_hours"]
idx=np.arange(len(data))
tr,te=train_test_split(idx,test_size=.25,random_state=42)
ym=RandomForestRegressor(n_estimators=250,random_state=42,n_jobs=-1).fit(data[features].iloc[tr],data["yield_percent"].iloc[tr])
rm=RandomForestRegressor(n_estimators=250,random_state=42,n_jobs=-1).fit(data[features].iloc[tr],data["rul_cycles"].iloc[tr])
out=data.iloc[te][["equipment_id","recipe","chamber_id","yield_percent","rul_cycles"]].copy()
out["yield_prediction"]=ym.predict(data[features].iloc[te])
out["rul_prediction"]=rm.predict(data[features].iloc[te])
out["yield_abs_error"]=(out["yield_percent"]-out["yield_prediction"]).abs()
out["rul_abs_error"]=(out["rul_cycles"]-out["rul_prediction"]).abs()
print(out.sort_values(["yield_abs_error","rul_abs_error"],ascending=False).head(20).round(3))
out.to_csv(REPORT_DIR/"error_analysis.csv",index=False,encoding="utf-8-sig")
