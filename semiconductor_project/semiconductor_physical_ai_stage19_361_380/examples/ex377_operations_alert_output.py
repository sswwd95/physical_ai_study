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
ops_df["alert_type"]=np.select(
    [
        ops_df["fault_flag"].eq(1),
        ops_df["yield_percent"]<93,
        ops_df["cycle_time_min"]>66
    ],
    ["FAULT_RISK","LOW_YIELD","CYCLE_DELAY"],
    default="NORMAL"
)
alerts=ops_df.loc[ops_df["alert_type"]!="NORMAL"].copy()
alerts["priority"]=np.select(
    [alerts["fault_flag"].eq(1),alerts["yield_percent"]<90],
    ["HIGH","MEDIUM"],
    default="LOW"
)
alerts=alerts.sort_values(["priority","timestamp"],ascending=[True,True])
print(alerts[["timestamp","equipment_id","alert_type","priority"]].head(20))
alerts.to_csv(OUTPUT_DIR/"ex377_operations_alerts.csv",index=False,encoding="utf-8-sig")
