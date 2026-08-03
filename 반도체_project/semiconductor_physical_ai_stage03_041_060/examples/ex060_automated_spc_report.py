from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_sensor_data.csv 파일이 없습니다.")

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

specs = {
    "chamber_temp_c": {"lsl": 69.0, "usl": 75.0},
    "chamber_pressure_pa": {"lsl": 17.0, "usl": 19.0},
}

summary_rows = []
alarm_masks = []

for column, spec in specs.items():
    mean_value = sensor_df[column].mean()
    std_value = sensor_df[column].std(ddof=1)
    ucl = mean_value + 3 * std_value
    lcl = mean_value - 3 * std_value

    cp = (
        (spec["usl"] - spec["lsl"])
        / (6 * std_value)
    )
    cpu = (
        (spec["usl"] - mean_value)
        / (3 * std_value)
    )
    cpl = (
        (mean_value - spec["lsl"])
        / (3 * std_value)
    )
    cpk = min(cpu, cpl)

    control_mask = (
        (sensor_df[column] > ucl)
        | (sensor_df[column] < lcl)
    )
    spec_mask = ~sensor_df[column].between(
        spec["lsl"],
        spec["usl"],
    )

    summary_rows.append({
        "sensor": column,
        "mean": mean_value,
        "std": std_value,
        "lcl": lcl,
        "ucl": ucl,
        "lsl": spec["lsl"],
        "usl": spec["usl"],
        "cp": cp,
        "cpk": cpk,
        "control_violation_count": int(control_mask.sum()),
        "spec_violation_count": int(spec_mask.sum()),
    })

    alarm_masks.append(control_mask | spec_mask)

summary_df = pd.DataFrame(summary_rows)
combined_alarm = np.logical_or.reduce(alarm_masks)
alarm_df = sensor_df.loc[combined_alarm]

excel_file = OUTPUT_DIR / "ex060_automated_spc_report.xlsx"
with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
    summary_df.to_excel(
        writer,
        sheet_name="summary",
        index=False,
    )
    alarm_df.to_excel(
        writer,
        sheet_name="alarm_rows",
        index=False,
    )

summary_df.to_csv(
    OUTPUT_DIR / "ex060_spc_summary.csv",
    index=False,
    encoding="utf-8-sig",
)

print(summary_df.round(4))
print("Excel 보고서:", excel_file)
