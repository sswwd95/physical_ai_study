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
raw=safe_df["severity_level"].ge(2)
persistent=raw.rolling(5,min_periods=5).sum().ge(5)
safe_df["persistent_alarm"]=persistent
print("원시 경보:",int(raw.sum()))
print("5초 지속 경보:",int(persistent.sum()))
