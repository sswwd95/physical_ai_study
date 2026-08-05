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
latest["recommended_action"]=np.select(
    [latest["rul_cycles"]<=10,latest["rul_cycles"]<=20,latest["rul_cycles"]<=40],
    ["immediate_maintenance","schedule_within_week","inspection_required"],
    default="continue_monitoring")
latest["recommended_due_cycle"]=latest["cycle"]+latest["rul_cycles"].clip(lower=0)
out=latest[["equipment_id","cycle","health_index","rul_cycles","recommended_action","recommended_due_cycle"]].sort_values("rul_cycles")
print(out)
out.to_csv(OUTPUT_DIR/"ex239_maintenance_schedule.csv",index=False,encoding="utf-8-sig")
