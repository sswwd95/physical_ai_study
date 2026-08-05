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
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
sensor_df=pd.read_csv(DATA_FILE)
features=["equipment_id","operation_mode","temperature_c","pressure_pa","vibration_rms_g","vibration_peak_g","motor_current_a","pump_speed_rpm","gas_flow_sccm","particle_count","maintenance_age_hours"]
X=sensor_df[features]; y=(sensor_df["fault_type"]!="normal").astype(int)
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
pre=ColumnTransformer([("num","passthrough",features[2:]),("cat",OneHotEncoder(handle_unknown="ignore"),features[:2])])
m=Pipeline([("preprocess",pre),("classifier",RandomForestClassifier(n_estimators=300,class_weight="balanced",random_state=42,n_jobs=-1))])
m.fit(Xtr,ytr); prob=m.predict_proba(Xte)[:,1]
rows=[]
for t in [.3,.4,.5,.6,.7]:
    pred=(prob>=t).astype(int)
    rows.append({"threshold":t,"predicted_faults":int(pred.sum()),"review_count":int(((prob>=t-.1)&(prob<t)).sum())})
out=pd.DataFrame(rows); print(out); out.to_csv(OUTPUT_DIR/"ex212_threshold_policy.csv",index=False,encoding="utf-8-sig")
