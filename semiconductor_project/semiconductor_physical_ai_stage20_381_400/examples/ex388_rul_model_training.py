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

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error,r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
data=pd.read_csv(DATA_FILE)
features=["recipe","chamber_id","temperature_c","pressure_pa","vibration_rms_g","particle_count","rf_power_w","gas_flow_sccm","cycle_time_min","maintenance_age_hours"]
X=data[features]; y=data["rul_cycles"]
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=42)
pre=ColumnTransformer([("num","passthrough",features[2:]),("cat",OneHotEncoder(handle_unknown="ignore",sparse_output=False),features[:2])])
model=Pipeline([("preprocess",pre),("regressor",GradientBoostingRegressor(n_estimators=250,learning_rate=.05,random_state=42))])
model.fit(Xtr,ytr); pred=model.predict(Xte)
print({"mae":mean_absolute_error(yte,pred),"r2":r2_score(yte,pred)})
