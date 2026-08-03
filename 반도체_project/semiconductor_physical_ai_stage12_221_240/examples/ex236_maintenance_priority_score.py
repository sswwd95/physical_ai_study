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
latest=pm_df.sort_values("cycle").groupby("equipment_id").tail(1).copy()
latest["priority_score"]=(1-latest["health_index"])*50 + (20-latest["rul_cycles"]).clip(lower=0)*2 + latest["failure_within_20"]*20
latest["priority_level"]=pd.cut(latest["priority_score"],[-np.inf,20,40,60,np.inf],labels=["low","medium","high","critical"])
out=latest[["equipment_id","cycle","health_index","rul_cycles","priority_score","priority_level"]].sort_values("priority_score",ascending=False)
print(out.round(3)); out.to_csv(OUTPUT_DIR/"ex236_maintenance_priority.csv",index=False,encoding="utf-8-sig")
