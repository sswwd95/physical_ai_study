from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "safety_decision_stream.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/safety_decision_stream.csv 파일이 없습니다.")

safe_df=pd.read_csv(DATA_FILE)
risk=safe_df["severity_level"].to_numpy()
active=False
states=[]
for value in risk:
    if not active and value>=3:
        active=True
    elif active and value<=1:
        active=False
    states.append(active)
safe_df["hysteresis_alarm"]=states
print("히스테리시스 경보 시점:",int(safe_df["hysteresis_alarm"].sum()))
