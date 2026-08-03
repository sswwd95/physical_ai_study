from pathlib import Path
import json
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "final_project_data.csv"
CONFIG_FILE = ROOT / "config" / "project_config.json"
OUTPUT_DIR = ROOT / "outputs"
MODEL_DIR = ROOT / "models"
REPORT_DIR = ROOT / "reports"
PORTFOLIO_DIR = ROOT / "portfolio"

for directory in [OUTPUT_DIR, MODEL_DIR, REPORT_DIR, PORTFOLIO_DIR]:
    directory.mkdir(exist_ok=True)

data=pd.read_csv(DATA_FILE)
tests=[
    ("row_count",len(data)==1800),
    ("no_missing",data.isna().sum().sum()==0),
    ("yield_range",data["yield_percent"].between(0,100).all()),
    ("fault_binary",data["fault_flag"].isin([0,1]).all()),
    ("rul_nonnegative",(data["rul_cycles"]>=0).all()),
    ("equipment_count",data["equipment_id"].nunique()==4),
]
test_df=pd.DataFrame(tests,columns=["test","passed"])
print(test_df)
test_df.to_csv(REPORT_DIR/"integration_tests.csv",index=False,encoding="utf-8-sig")
if not test_df["passed"].all():
    raise AssertionError("통합 테스트 실패")
