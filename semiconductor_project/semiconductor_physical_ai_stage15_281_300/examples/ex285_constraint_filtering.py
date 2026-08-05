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

safe=candidate_df.loc[
    candidate_df["pressure_pa"].between(17.5,18.5)
    & candidate_df["rf_power_w"].between(830,870)
    & candidate_df["gas_flow_sccm"].between(116,124)
].copy()
print("전체 후보:",len(candidate_df))
print("제약 통과:",len(safe))
safe.to_csv(OUTPUT_DIR/"ex285_safe_candidates.csv",index=False,encoding="utf-8-sig")
