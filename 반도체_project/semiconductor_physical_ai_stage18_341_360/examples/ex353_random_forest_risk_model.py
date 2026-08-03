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
from sklearn.metrics import classification_report
safe_df=pd.read_csv(DATA_FILE)
features=["temperature_c","pressure_pa","vibration_rms_g","gas_flow_sccm","particle_count","door_closed","cooling_ok","vacuum_ok"]
X=safe_df[features]; y=safe_df["anomaly_type"].ne("normal").astype(int)
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
model=RandomForestClassifier(n_estimators=350,class_weight="balanced",random_state=42,n_jobs=-1)
model.fit(Xtr,ytr)
pred=model.predict(Xte)
print(classification_report(yte,pred,zero_division=0))
