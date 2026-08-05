from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "safety_decision_stream.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/safety_decision_stream.csv 파일이 없습니다.")

safe_df=pd.read_csv(DATA_FILE,parse_dates=["timestamp"])
active=safe_df["anomaly_type"].ne("normal")
group=(active!=active.shift()).cumsum()
events=safe_df.loc[active].groupby(group).agg(
    start=("timestamp","min"),end=("timestamp","max"),
    duration_seconds=("timestamp","count"),
    anomaly_type=("anomaly_type","first"),
    max_severity=("severity_level","max"),
    equipment_id=("equipment_id","first"))
events["event_id"]=[f"INC-{i:03d}" for i in range(1,len(events)+1)]
print(events)
events.to_csv(OUTPUT_DIR/"ex357_incident_timeline.csv",encoding="utf-8-sig")
