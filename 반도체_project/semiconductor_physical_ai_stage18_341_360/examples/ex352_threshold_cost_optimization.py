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
actual=safe_df["anomaly_type"].ne("normal")
rows=[]
for threshold in range(1,6):
    pred=safe_df["severity_level"].ge(threshold)
    fa=int((~actual & pred).sum())
    miss=int((actual & ~pred).sum())
    rows.append({"threshold":threshold,"false_alarm":fa,"miss":miss,"expected_cost":fa*50+miss*1000})
out=pd.DataFrame(rows).sort_values("expected_cost")
print(out)
out.to_csv(OUTPUT_DIR/"ex352_threshold_cost.csv",index=False,encoding="utf-8-sig")
