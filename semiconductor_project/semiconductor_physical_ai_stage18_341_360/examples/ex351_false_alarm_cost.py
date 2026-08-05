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
actual=safe_df["anomaly_type"].ne("normal")
pred=safe_df["severity_level"].ge(2)
false_alarm=(~actual & pred).sum()
miss=(actual & ~pred).sum()
cost=false_alarm*50+miss*1000
print("오탐:",int(false_alarm))
print("미탐:",int(miss))
print("총 비용:",int(cost))
