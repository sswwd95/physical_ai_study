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
safe_df["alarm"]=safe_df["severity_level"]>=2
group_id=(safe_df["alarm"]!=safe_df["alarm"].shift()).cumsum()
events=safe_df.loc[safe_df["alarm"]].groupby(group_id).agg(
    start=("timestamp","min"),end=("timestamp","max"),
    duration_seconds=("timestamp","count"),
    max_severity=("severity_level","max"),
    equipment_id=("equipment_id","first"),
    anomaly_type=("anomaly_type","first"))
events["priority"]=events["max_severity"]*10+np.log1p(events["duration_seconds"])
events=events.sort_values("priority",ascending=False)
print(events.head(15).round(3))
events.to_csv(OUTPUT_DIR/"ex343_alarm_priority.csv",encoding="utf-8-sig")
