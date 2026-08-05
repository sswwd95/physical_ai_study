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

QUALITY_FILE = ROOT / "data" / "sensor_data_with_quality_errors.csv"
if not QUALITY_FILE.exists():
    raise FileNotFoundError("실습 025를 먼저 실행하세요.")

quality_df = pd.read_csv(QUALITY_FILE)

range_violation = (
    ~quality_df["chamber_temp_c"].between(65, 80)
    | ~quality_df["chamber_pressure_pa"].between(15, 22)
    | ~quality_df["rf_power_w"].between(780, 920)
    | ~quality_df["gas_flow_sccm"].between(105, 135)
    | ~quality_df["vibration_g"].between(0, 0.25)
)

summary_df = pd.DataFrame([{
    "row_count": len(quality_df),
    "column_count": len(quality_df.columns),
    "missing_cell_count": int(quality_df.isna().sum().sum()),
    "full_duplicate_count": int(quality_df.duplicated().sum()),
    "invalid_state_count": int(
        (~quality_df["process_state"].isin(["stabilize", "process", "purge"])).sum()
    ),
    "range_violation_row_count": int(range_violation.sum()),
}])

missing_df = (
    quality_df.isna()
    .sum()
    .rename("missing_count")
    .reset_index()
    .rename(columns={"index": "column"})
)
missing_df["missing_ratio"] = missing_df["missing_count"] / len(quality_df)

output_file = OUTPUT_DIR / "ex039_quality_report.xlsx"
with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    summary_df.to_excel(writer, sheet_name="summary", index=False)
    missing_df.to_excel(writer, sheet_name="missing_by_column", index=False)

print(summary_df)
print("Excel 저장:", output_file)
