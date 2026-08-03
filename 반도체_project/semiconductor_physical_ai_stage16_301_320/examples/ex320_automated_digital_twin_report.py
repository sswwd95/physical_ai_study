from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "digital_twin_sensor_stream.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "data/digital_twin_sensor_stream.csv 파일이 없습니다."
    )

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

for column in [
    "temp_sensor_a_c",
    "temp_sensor_b_c",
    "pressure_sensor_a_pa",
    "pressure_sensor_b_pa",
    "rf_sensor_w",
    "gas_sensor_sccm",
]:
    sensor_df[column] = (
        sensor_df[column]
        .interpolate(limit_direction="both")
    )

sensor_df["fused_temperature_c"] = (
    0.7 * sensor_df["temp_sensor_a_c"]
    + 0.3 * sensor_df["temp_sensor_b_c"]
)

sensor_df["fused_pressure_pa"] = (
    0.75 * sensor_df["pressure_sensor_a_pa"]
    + 0.25 * sensor_df["pressure_sensor_b_pa"]
)

sensor_df["temperature_residual"] = (
    sensor_df["fused_temperature_c"]
    - sensor_df["true_temperature_c"]
)

sensor_df["pressure_residual"] = (
    sensor_df["fused_pressure_pa"]
    - sensor_df["true_pressure_pa"]
)

sensor_df["alarm"] = (
    sensor_df["temperature_residual"].abs() > 2.0
) | (
    sensor_df["pressure_residual"].abs() > 0.8
)

phase_summary = (
    sensor_df.groupby("process_phase")[
        [
            "temperature_residual",
            "pressure_residual",
            "rf_sensor_w",
            "gas_sensor_sccm",
        ]
    ]
    .agg(["mean", "std", "max", "min"])
)

alarm_rows = sensor_df.loc[sensor_df["alarm"]].copy()

sensor_quality = pd.DataFrame([
    {
        "sensor": "temp_sensor_a",
        "rmse": np.sqrt(
            np.mean(
                (
                    sensor_df["temp_sensor_a_c"]
                    - sensor_df["true_temperature_c"]
                ) ** 2
            )
        ),
    },
    {
        "sensor": "temp_sensor_b",
        "rmse": np.sqrt(
            np.mean(
                (
                    sensor_df["temp_sensor_b_c"]
                    - sensor_df["true_temperature_c"]
                ) ** 2
            )
        ),
    },
    {
        "sensor": "pressure_sensor_a",
        "rmse": np.sqrt(
            np.mean(
                (
                    sensor_df["pressure_sensor_a_pa"]
                    - sensor_df["true_pressure_pa"]
                ) ** 2
            )
        ),
    },
    {
        "sensor": "pressure_sensor_b",
        "rmse": np.sqrt(
            np.mean(
                (
                    sensor_df["pressure_sensor_b_pa"]
                    - sensor_df["true_pressure_pa"]
                ) ** 2
            )
        ),
    },
])

excel_file = OUTPUT_DIR / "ex320_digital_twin_report.xlsx"

with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
    sensor_quality.to_excel(
        writer,
        sheet_name="sensor_quality",
        index=False,
    )
    phase_summary.to_excel(
        writer,
        sheet_name="phase_summary",
    )
    alarm_rows.to_excel(
        writer,
        sheet_name="alarm_rows",
        index=False,
    )
    sensor_df.to_excel(
        writer,
        sheet_name="twin_stream",
        index=False,
    )

print("보고서 저장:", excel_file)
