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
temp=((safe_df["temperature_c"]-74)/6).clip(lower=0)
pressure=((safe_df["pressure_pa"]-18.5)/3).clip(lower=0)
vibration=((safe_df["vibration_rms_g"]-.10)/.10).clip(lower=0)
particle=((safe_df["particle_count"]-10)/25).clip(lower=0)
interlock=(1-safe_df[["door_closed","cooling_ok","vacuum_ok"]]).max(axis=1)
safe_df["risk_score"]=(.25*temp+.20*pressure+.20*vibration+.15*particle+.20*interlock).clip(0,1)
print(safe_df["risk_score"].describe().round(4))
