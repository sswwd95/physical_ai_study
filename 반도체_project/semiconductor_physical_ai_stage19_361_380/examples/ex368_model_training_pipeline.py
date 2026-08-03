from pathlib import Path
import json
import logging
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "operations_stream.csv"
CONFIG_FILE = ROOT / "config" / "app_config.json"
OUTPUT_DIR = ROOT / "outputs"
LOG_DIR = ROOT / "logs"
MODEL_DIR = ROOT / "models"

OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)
MODEL_DIR.mkdir(exist_ok=True)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
ops_df=pd.read_csv(DATA_FILE)
features=["temperature_c","pressure_pa","vibration_rms_g","particle_count","cycle_time_min","yield_percent"]
X=ops_df[features]; y=ops_df["fault_flag"]
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
model=RandomForestClassifier(n_estimators=300,class_weight="balanced",random_state=42,n_jobs=-1)
model.fit(Xtr,ytr)
pred=model.predict(Xte)
print(classification_report(yte,pred,zero_division=0))
