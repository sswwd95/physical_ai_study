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
score=np.zeros(len(safe_df),dtype=int)
score+=(safe_df["temperature_c"]>75).astype(int)
score+=(safe_df["temperature_c"]>79).astype(int)
score+=(safe_df["pressure_pa"]>19).astype(int)
score+=(safe_df["pressure_pa"]>20.5).astype(int)
score+=(safe_df["vibration_rms_g"]>.12).astype(int)
score+=(safe_df["particle_count"]>15).astype(int)
score+=(safe_df["door_closed"].eq(0)).astype(int)*3
score+=(safe_df["cooling_ok"].eq(0)).astype(int)*2
score+=(safe_df["vacuum_ok"].eq(0)).astype(int)*2
safe_df["calculated_severity"]=np.clip(score,0,5)
print(pd.crosstab(safe_df["severity_level"],safe_df["calculated_severity"]))
