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
votes=pd.DataFrame({
    "temperature_vote":safe_df["temperature_c"]>76,
    "pressure_vote":safe_df["pressure_pa"]>19.2,
    "vibration_vote":safe_df["vibration_rms_g"]>.12,
    "particle_vote":safe_df["particle_count"]>15})
safe_df["vote_count"]=votes.sum(axis=1)
safe_df["majority_alarm"]=safe_df["vote_count"]>=2
print(safe_df["vote_count"].value_counts().sort_index())
