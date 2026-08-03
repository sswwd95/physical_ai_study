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
safe_df["action"]=np.select(
    [
        (safe_df[["door_closed","cooling_ok","vacuum_ok"]]==0).any(axis=1)|(safe_df["severity_level"]>=4),
        safe_df["severity_level"]==3,
        safe_df["severity_level"]==2
    ],
    ["STOP_AND_INSPECT","SLOWDOWN_AND_CHECK","REMEASURE"],
    default="MONITOR")
handoff=safe_df.loc[safe_df["action"]!="MONITOR",[
    "timestamp","equipment_id","process_phase","anomaly_type","severity_level",
    "temperature_c","pressure_pa","vibration_rms_g","particle_count","action"]]
print(handoff.head(15))
handoff.to_csv(OUTPUT_DIR/"ex359_operator_handoff.csv",index=False,encoding="utf-8-sig")
