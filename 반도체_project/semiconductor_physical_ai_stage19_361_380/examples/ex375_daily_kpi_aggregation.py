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

ops_df=pd.read_csv(DATA_FILE,parse_dates=["timestamp"])
ops_df["date"]=ops_df["timestamp"].dt.date
daily=ops_df.groupby("date").agg(
    mean_yield=("yield_percent","mean"),
    fault_count=("fault_flag","sum"),
    mean_cycle_time=("cycle_time_min","mean"),
    running_ratio=("process_status",lambda s:(s=="RUNNING").mean())
)
print(daily.round(4))
daily.to_csv(OUTPUT_DIR/"ex375_daily_kpi.csv",encoding="utf-8-sig")
