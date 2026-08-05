from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
HISTORY_FILE = ROOT / "data" / "process_optimization_history.csv"
CANDIDATE_FILE = ROOT / "data" / "optimization_candidates.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

history_df = pd.read_csv(HISTORY_FILE)
candidate_df = pd.read_csv(CANDIDATE_FILE)

print("이력 데이터:", history_df.shape)
print("후보 데이터:", candidate_df.shape)
print("레시피:", sorted(history_df["recipe"].unique()))
print("챔버:", sorted(history_df["chamber_id"].unique()))
print(history_df[["uniformity_percent","defect_rate","cycle_time_min"]].describe().round(4))
