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

import joblib
from datetime import datetime
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor,GradientBoostingRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
data=pd.read_csv(DATA_FILE)
features=["recipe","chamber_id","temperature_c","pressure_pa","vibration_rms_g","particle_count","rf_power_w","gas_flow_sccm","cycle_time_min","maintenance_age_hours"]
pre_sparse=ColumnTransformer([("num","passthrough",features[2:]),("cat",OneHotEncoder(handle_unknown="ignore"),features[:2])])
pre_dense=ColumnTransformer([("num","passthrough",features[2:]),("cat",OneHotEncoder(handle_unknown="ignore",sparse_output=False),features[:2])])
models={
    "yield":Pipeline([("preprocess",pre_sparse),("model",RandomForestRegressor(n_estimators=350,random_state=42,n_jobs=-1))]),
    "fault":Pipeline([("preprocess",pre_sparse),("model",RandomForestClassifier(n_estimators=350,class_weight="balanced",random_state=42,n_jobs=-1))]),
    "rul":Pipeline([("preprocess",pre_dense),("model",GradientBoostingRegressor(n_estimators=250,learning_rate=.05,random_state=42))])
}
targets={"yield":"yield_percent","fault":"fault_flag","rul":"rul_cycles"}
version=datetime.now().strftime("%Y%m%d_%H%M%S")
registry=[]
for name,model in models.items():
    model.fit(data[features],data[targets[name]])
    file=MODEL_DIR/f"{name}_model_{version}.joblib"
    joblib.dump(model,file)
    registry.append({"name":name,"version":version,"file":file.name,"target":targets[name],"features":features})
registry_file=MODEL_DIR/"model_registry.json"
registry_file.write_text(json.dumps(registry,ensure_ascii=False,indent=2),encoding="utf-8")
print(registry_file.read_text(encoding="utf-8"))
