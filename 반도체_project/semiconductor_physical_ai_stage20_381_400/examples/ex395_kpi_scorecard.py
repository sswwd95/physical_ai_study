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

from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor
from sklearn.metrics import mean_absolute_error,recall_score,r2_score
from sklearn.model_selection import train_test_split
data=pd.read_csv(DATA_FILE)
features=["temperature_c","pressure_pa","vibration_rms_g","particle_count","rf_power_w","gas_flow_sccm","cycle_time_min","maintenance_age_hours"]
X=data[features]
tr,te=train_test_split(np.arange(len(data)),test_size=.25,random_state=42,stratify=data["fault_flag"])
yield_model=RandomForestRegressor(n_estimators=250,random_state=42,n_jobs=-1).fit(X.iloc[tr],data["yield_percent"].iloc[tr])
fault_model=RandomForestClassifier(n_estimators=250,class_weight="balanced",random_state=42,n_jobs=-1).fit(X.iloc[tr],data["fault_flag"].iloc[tr])
rul_model=RandomForestRegressor(n_estimators=250,random_state=42,n_jobs=-1).fit(X.iloc[tr],data["rul_cycles"].iloc[tr])
yp=yield_model.predict(X.iloc[te]); fp=fault_model.predict(X.iloc[te]); rp=rul_model.predict(X.iloc[te])
scorecard=pd.DataFrame([
    {"kpi":"yield_mae","value":mean_absolute_error(data["yield_percent"].iloc[te],yp),"target":1.5},
    {"kpi":"yield_r2","value":r2_score(data["yield_percent"].iloc[te],yp),"target":.7},
    {"kpi":"fault_recall","value":recall_score(data["fault_flag"].iloc[te],fp,zero_division=0),"target":.8},
    {"kpi":"rul_mae","value":mean_absolute_error(data["rul_cycles"].iloc[te],rp),"target":20.0},
])
scorecard["passed"]=np.where(scorecard["kpi"].str.contains("mae"),scorecard["value"]<=scorecard["target"],scorecard["value"]>=scorecard["target"])
print(scorecard.round(4))
scorecard.to_csv(REPORT_DIR/"kpi_scorecard.csv",index=False,encoding="utf-8-sig")
