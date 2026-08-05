from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "safety_decision_stream.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/safety_decision_stream.csv 파일이 없습니다.")

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
safe_df=pd.read_csv(DATA_FILE)
features=["temperature_c","pressure_pa","vibration_rms_g","gas_flow_sccm","particle_count","door_closed","cooling_ok","vacuum_ok"]
X=safe_df[features]; y=safe_df["anomaly_type"].ne("normal").astype(int)
idx=np.arange(len(safe_df))
tr,te=train_test_split(idx,test_size=.25,random_state=42,stratify=y)
m=RandomForestClassifier(n_estimators=350,class_weight="balanced",random_state=42,n_jobs=-1)
m.fit(X.iloc[tr],y.iloc[tr]); prob=m.predict_proba(X.iloc[te])[:,1]
out=safe_df.iloc[te][["timestamp","equipment_id","anomaly_type"]].copy()
out["risk_probability"]=prob
out["action"]=np.select([prob>=.9,prob>=.7,prob>=.4],["STOP","SLOWDOWN","REINSPECT"],default="CONTINUE")
print(out["action"].value_counts())
