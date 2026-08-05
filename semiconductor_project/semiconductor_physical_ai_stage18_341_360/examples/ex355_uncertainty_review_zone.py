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
safe_df=pd.read_csv(DATA_FILE)
features=["temperature_c","pressure_pa","vibration_rms_g","gas_flow_sccm","particle_count","door_closed","cooling_ok","vacuum_ok"]
X=safe_df[features]; y=safe_df["anomaly_type"].ne("normal").astype(int)
m=RandomForestClassifier(n_estimators=350,class_weight="balanced",random_state=42,n_jobs=-1)
m.fit(X,y); prob=m.predict_proba(X)[:,1]
safe_df["risk_probability"]=prob
safe_df["review_required"]=safe_df["risk_probability"].between(.35,.75)
print("재검사 대상:",int(safe_df["review_required"].sum()))
