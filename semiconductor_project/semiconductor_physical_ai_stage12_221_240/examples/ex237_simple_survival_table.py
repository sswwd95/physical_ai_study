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
life=pm_df.groupby("equipment_id")["cycle"].max().add(1)
rows=[]
for t in range(0,int(life.max())+1,10):
    rows.append({"cycle":t,"survival_probability":float((life>t).mean()),"equipment_at_risk":int((life>t).sum())})
out=pd.DataFrame(rows)
print(out)
out.to_csv(OUTPUT_DIR/"ex237_survival_table.csv",index=False,encoding="utf-8-sig")
