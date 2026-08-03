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
safe_df["action"]=np.select(
    [
        (safe_df["door_closed"]==0)|(safe_df["cooling_ok"]==0)|(safe_df["vacuum_ok"]==0)|(safe_df["severity_level"]>=4),
        safe_df["severity_level"]==3,
        safe_df["severity_level"]==2,
        safe_df["severity_level"]==1
    ],
    ["EMERGENCY_STOP","SLOWDOWN","REINSPECT","MONITOR"],
    default="CONTINUE")
print(safe_df["action"].value_counts())
