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
X=sensor_df[features]; y=sensor_df["fault_type"]
idx=np.arange(len(sensor_df)); tr,te=train_test_split(idx,test_size=.25,random_state=42,stratify=y)
pre=ColumnTransformer([("num","passthrough",features[2:]),("cat",OneHotEncoder(handle_unknown="ignore"),features[:2])])
m=Pipeline([("preprocess",pre),("classifier",RandomForestClassifier(n_estimators=350,class_weight="balanced",random_state=42,n_jobs=-1))])
m.fit(X.iloc[tr],y.iloc[tr]); prob=m.predict_proba(X.iloc[te]); pred=m.predict(X.iloc[te])
out=sensor_df.iloc[te][["timestamp","equipment_id","fault_type"]].copy(); out["predicted_fault"]=pred; out["max_probability"]=prob.max(1); out["review_required"]=out["max_probability"]<.65
print("재검사:",int(out["review_required"].sum())); out.to_csv(OUTPUT_DIR/"ex218_low_confidence.csv",index=False,encoding="utf-8-sig")
