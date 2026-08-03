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

def clean_sensor_data(input_file, clean_output, audit_output):
    required_columns = [
        "timestamp",
        "lot_id",
        "chamber_temp_c",
        "chamber_pressure_pa",
        "rf_power_w",
        "gas_flow_sccm",
        "vibration_g",
        "particle_count",
        "process_state",
    ]

    sensor_df = pd.read_csv(input_file)
    audit = {"input_rows": len(sensor_df)}

    missing_columns = [
        column for column in required_columns
        if column not in sensor_df.columns
    ]
    if missing_columns:
        raise ValueError(f"필수 컬럼 누락: {missing_columns}")

    sensor_df["timestamp"] = pd.to_datetime(
        sensor_df["timestamp"],
        errors="coerce",
    )
    audit["invalid_timestamp_count"] = int(
        sensor_df["timestamp"].isna().sum()
    )

    sensor_df = sensor_df.sort_values("timestamp").reset_index(drop=True)

    duplicate_count = int(sensor_df.duplicated().sum())
    sensor_df = sensor_df.drop_duplicates().reset_index(drop=True)
    audit["removed_duplicate_count"] = duplicate_count

    numeric_columns = [
        "chamber_temp_c",
        "chamber_pressure_pa",
        "rf_power_w",
        "gas_flow_sccm",
        "vibration_g",
        "particle_count",
    ]
    for column in numeric_columns:
        sensor_df[column] = pd.to_numeric(
            sensor_df[column],
            errors="coerce",
        )

    sensor_df = sensor_df.set_index("timestamp")
    interpolate_columns = ["chamber_pressure_pa", "rf_power_w"]
    before_missing = int(
        sensor_df[interpolate_columns].isna().sum().sum()
    )
    sensor_df[interpolate_columns] = sensor_df[
        interpolate_columns
    ].interpolate(method="time", limit_direction="both")
    after_missing = int(
        sensor_df[interpolate_columns].isna().sum().sum()
    )
    sensor_df = sensor_df.reset_index()

    audit["interpolated_cell_count"] = (
        before_missing - after_missing
    )

    valid_states = ["stabilize", "process", "purge"]
    invalid_state_mask = ~sensor_df["process_state"].isin(valid_states)
    audit["invalid_state_count"] = int(invalid_state_mask.sum())
    sensor_df.loc[invalid_state_mask, "process_state"] = np.nan

    sensor_df["quality_has_missing"] = sensor_df.isna().any(axis=1)
    sensor_df["quality_range_violation"] = (
        ~sensor_df["chamber_temp_c"].between(65, 80)
        | ~sensor_df["chamber_pressure_pa"].between(15, 22)
        | ~sensor_df["rf_power_w"].between(780, 920)
        | ~sensor_df["gas_flow_sccm"].between(105, 135)
        | ~sensor_df["vibration_g"].between(0, 0.25)
    )

    audit["output_rows"] = len(sensor_df)
    audit["remaining_missing_cells"] = int(
        sensor_df.isna().sum().sum()
    )
    audit["range_violation_rows"] = int(
        sensor_df["quality_range_violation"].sum()
    )

    sensor_df.to_csv(
        clean_output,
        index=False,
        encoding="utf-8-sig",
    )
    pd.DataFrame([audit]).to_csv(
        audit_output,
        index=False,
        encoding="utf-8-sig",
    )
    return sensor_df, audit

if not QUALITY_FILE.exists():
    raise FileNotFoundError("실습 025를 먼저 실행하세요.")

clean_df, audit = clean_sensor_data(
    QUALITY_FILE,
    OUTPUT_DIR / "ex040_clean_sensor_data.csv",
    OUTPUT_DIR / "ex040_cleaning_audit.csv",
)

print("정제 결과 행 수:", len(clean_df))
print("감사 요약:")
for key, value in audit.items():
    print(f"- {key}: {value}")
