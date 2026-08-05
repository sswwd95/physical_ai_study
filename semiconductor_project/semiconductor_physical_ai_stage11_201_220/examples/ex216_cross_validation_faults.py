from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "equipment_fault_diagnosis.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "data/equipment_fault_diagnosis.csv 파일이 없습니다."
    )

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold,cross_validate
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
sensor_df=pd.read_csv(DATA_FILE)
features=["equipment_id","operation_mode","temperature_c","pressure_pa","vibration_rms_g","vibration_peak_g","motor_current_a","pump_speed_rpm","gas_flow_sccm","particle_count","maintenance_age_hours"]
X=sensor_df[features]; y=sensor_df["fault_type"]
pre=ColumnTransformer([("num","passthrough",features[2:]),("cat",OneHotEncoder(handle_unknown="ignore"),features[:2])])
m=Pipeline([("preprocess",pre),("classifier",RandomForestClassifier(n_estimators=250,class_weight="balanced",random_state=42,n_jobs=-1))])
cv=StratifiedKFold(5,shuffle=True,random_state=42)
s=cross_validate(m,X,y,cv=cv,scoring=["accuracy","f1_macro","f1_weighted"])
out=pd.DataFrame({"fold":range(1,6),"accuracy":s["test_accuracy"],"macro_f1":s["test_f1_macro"],"weighted_f1":s["test_f1_weighted"]})
print(out.round(4)); out.to_csv(OUTPUT_DIR/"ex216_cv_scores.csv",index=False,encoding="utf-8-sig")
