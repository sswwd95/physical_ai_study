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
sensor_invalid=(
    safe_df[["temperature_c","pressure_pa","vibration_rms_g","gas_flow_sccm"]].isna().any(axis=1)
)
interlock_invalid=(safe_df[["door_closed","cooling_ok","vacuum_ok"]]==0).any(axis=1)
safe_df["fallback_action"]=np.select(
    [interlock_invalid,sensor_invalid,safe_df["severity_level"]>=3],
    ["SAFE_STOP","HOLD_LAST_SAFE_VALUE","REDUCED_POWER"],
    default="NORMAL_CONTROL")
print(safe_df["fallback_action"].value_counts())
