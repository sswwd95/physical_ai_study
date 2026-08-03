from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "기본 데이터가 없습니다. 프로젝트 루트에서 "
        "python generate_base_data.py를 먼저 실행하세요."
    )

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

rule_process_low_rf = (
    (sensor_df["process_state"] == "process")
    & (sensor_df["rf_power_w"] < 800.0)
)
rule_process_low_gas = (
    (sensor_df["process_state"] == "process")
    & (sensor_df["gas_flow_sccm"] < 110.0)
)
rule_purge_high_rf = (
    (sensor_df["process_state"] == "purge")
    & (sensor_df["rf_power_w"] > 900.0)
)

sensor_df["cross_sensor_violation"] = (
    rule_process_low_rf
    | rule_process_low_gas
    | rule_purge_high_rf
)

print("process 저전력:", int(rule_process_low_rf.sum()))
print("process 저유량:", int(rule_process_low_gas.sum()))
print("purge 고전력:", int(rule_purge_high_rf.sum()))

problem_df = sensor_df.loc[sensor_df["cross_sensor_violation"]]
problem_df.to_csv(
    OUTPUT_DIR / "ex037_cross_sensor_violations.csv",
    index=False,
    encoding="utf-8-sig",
)
