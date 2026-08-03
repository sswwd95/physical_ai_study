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
    mean_cycle_time=("cycle_time_min","mean")
)
equipment=ops_df.groupby("equipment_id").agg(
    mean_yield=("yield_percent","mean"),
    fault_rate=("fault_flag","mean"),
    mean_temperature=("temperature_c","mean"),
    mean_vibration=("vibration_rms_g","mean")
)
alerts=ops_df.loc[(ops_df["fault_flag"]==1)|(ops_df["yield_percent"]<93)].copy()
alerts["alert_type"]=np.where(alerts["fault_flag"]==1,"FAULT_RISK","LOW_YIELD")
quality=pd.DataFrame([
    {"check":"missing_values","failed":int(ops_df.isna().sum().sum())},
    {"check":"duplicates","failed":int(ops_df.duplicated().sum())},
    {"check":"yield_out_of_range","failed":int((~ops_df["yield_percent"].between(0,100)).sum())}
])
with pd.ExcelWriter(OUTPUT_DIR/"ex380_operations_report.xlsx",engine="openpyxl") as w:
    daily.to_excel(w,sheet_name="daily_kpi")
    equipment.to_excel(w,sheet_name="equipment_health")
    alerts.to_excel(w,sheet_name="alerts",index=False)
    quality.to_excel(w,sheet_name="data_quality",index=False)
print("보고서 저장 완료")
