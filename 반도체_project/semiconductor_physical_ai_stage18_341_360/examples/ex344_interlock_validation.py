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
safe_df["interlock_violation"]=(
    safe_df["door_closed"].eq(0)
    | safe_df["cooling_ok"].eq(0)
    | safe_df["vacuum_ok"].eq(0))
safe_df["mandatory_stop"]=safe_df["interlock_violation"]
print("인터록 위반:",int(safe_df["interlock_violation"].sum()))
print(safe_df.loc[safe_df["interlock_violation"],["timestamp","door_closed","cooling_ok","vacuum_ok"]].head())
