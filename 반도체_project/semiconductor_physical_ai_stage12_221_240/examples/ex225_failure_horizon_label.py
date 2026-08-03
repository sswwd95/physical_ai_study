from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "predictive_maintenance_rul.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "data/predictive_maintenance_rul.csv 파일이 없습니다."
    )

pm_df=pd.read_csv(DATA_FILE)
for horizon in [10,20,30]:
    pm_df[f"failure_within_{horizon}"]=(pm_df["rul_cycles"]<=horizon).astype(int)
print(pm_df[[f"failure_within_{h}" for h in [10,20,30]]].sum())
