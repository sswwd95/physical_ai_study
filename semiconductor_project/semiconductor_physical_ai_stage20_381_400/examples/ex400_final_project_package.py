from pathlib import Path
import json
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "final_project_data.csv"
CONFIG_FILE = ROOT / "config" / "project_config.json"
OUTPUT_DIR = ROOT / "outputs"
MODEL_DIR = ROOT / "models"
REPORT_DIR = ROOT / "reports"
PORTFOLIO_DIR = ROOT / "portfolio"

for directory in [OUTPUT_DIR, MODEL_DIR, REPORT_DIR, PORTFOLIO_DIR]:
    directory.mkdir(exist_ok=True)

data=pd.read_csv(DATA_FILE,parse_dates=["timestamp"])
daily=data.assign(date=data["timestamp"].dt.date).groupby("date").agg(
    mean_yield=("yield_percent","mean"),
    fault_count=("fault_flag","sum"),
    mean_rul=("rul_cycles","mean"),
    mean_cycle_time=("cycle_time_min","mean")
)
equipment=data.groupby("equipment_id").agg(
    mean_yield=("yield_percent","mean"),
    fault_rate=("fault_flag","mean"),
    mean_rul=("rul_cycles","mean"),
    mean_temperature=("temperature_c","mean"),
    mean_vibration=("vibration_rms_g","mean")
)
risk=data.loc[(data["fault_flag"]==1)|(data["yield_percent"]<93)|(data["rul_cycles"]<30)].copy()
risk["recommended_action"]=np.select(
    [risk["fault_flag"]==1,risk["rul_cycles"]<15,risk["yield_percent"]<90],
    ["INSPECT_NOW","MAINTENANCE_SOON","PROCESS_HOLD"],
    default="MONITOR")
quality=pd.DataFrame([
    {"check":"missing","failed":int(data.isna().sum().sum())},
    {"check":"duplicates","failed":int(data.duplicated().sum())},
    {"check":"yield_range","failed":int((~data["yield_percent"].between(0,100)).sum())}
])
excel=REPORT_DIR/"final_project_report.xlsx"
with pd.ExcelWriter(excel,engine="openpyxl") as w:
    daily.to_excel(w,sheet_name="daily_kpi")
    equipment.to_excel(w,sheet_name="equipment_summary")
    risk.to_excel(w,sheet_name="risk_actions",index=False)
    quality.to_excel(w,sheet_name="data_quality",index=False)

manifest={
    "project":"Semiconductor Physical AI Final Project",
    "examples":20,
    "data_rows":len(data),
    "report_file":excel.name,
    "portfolio_files":[p.name for p in PORTFOLIO_DIR.glob("*")],
    "generated_outputs":[p.name for p in OUTPUT_DIR.glob("*")]
}
manifest_file=REPORT_DIR/"final_project_manifest.json"
manifest_file.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding="utf-8")
print("최종 보고서:",excel)
print("Manifest:",manifest_file)
