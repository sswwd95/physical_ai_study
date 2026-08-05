from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data_stage04.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_sensor_data_stage04.csv 파일이 없습니다.")

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

baseline_temp = sensor_df["chamber_temp_c"].iloc[:120]
temp_mean = baseline_temp.mean()
temp_std = baseline_temp.std(ddof=1)

z = (
    sensor_df["chamber_temp_c"] - temp_mean
) / temp_std

cusum_values = []
current = 0.0
for value in z:
    current = max(0.0, current + value - 0.5)
    cusum_values.append(current)

sensor_df["cusum_upper"] = cusum_values
sensor_df["cusum_alarm"] = (
    sensor_df["cusum_upper"] >= 5.0
)

lambda_value = 0.2
sensor_df["temp_ewma"] = (
    sensor_df["chamber_temp_c"]
    .ewm(alpha=lambda_value, adjust=False)
    .mean()
)

t = np.arange(1, len(sensor_df) + 1)
ewma_std = temp_std * np.sqrt(
    lambda_value / (2 - lambda_value)
    * (1 - (1 - lambda_value) ** (2 * t))
)
sensor_df["ewma_ucl"] = temp_mean + 3 * ewma_std
sensor_df["ewma_alarm"] = (
    sensor_df["temp_ewma"] > sensor_df["ewma_ucl"]
)

baseline_variance = baseline_temp.var(ddof=1)
sensor_df["variance_ratio"] = (
    sensor_df["chamber_temp_c"]
    .rolling(window=40, min_periods=15)
    .var(ddof=1)
    / baseline_variance
)
sensor_df["variance_alarm"] = (
    sensor_df["variance_ratio"] >= 2.5
)

score = np.zeros(len(sensor_df))
for column in [
    "chamber_temp_c",
    "chamber_pressure_pa",
    "vibration_g",
]:
    baseline = sensor_df[column].iloc[:120]
    score += (
        (sensor_df[column] - baseline.mean())
        / baseline.std(ddof=1)
    ).abs()

sensor_df["change_score"] = score
sensor_df["multi_sensor_alarm"] = (
    sensor_df["change_score"] >= 8.0
)

sensor_df["any_alarm"] = (
    sensor_df["cusum_alarm"]
    | sensor_df["ewma_alarm"]
    | sensor_df["variance_alarm"]
    | sensor_df["multi_sensor_alarm"]
)

start_flag = (
    sensor_df["any_alarm"]
    & ~sensor_df["any_alarm"].shift(1, fill_value=False)
)
sensor_df["segment_id"] = start_flag.cumsum()
sensor_df.loc[
    ~sensor_df["any_alarm"],
    "segment_id",
] = 0

segments_df = (
    sensor_df.loc[sensor_df["segment_id"] > 0]
    .groupby("segment_id")
    .agg(
        start_time=("timestamp", "min"),
        end_time=("timestamp", "max"),
        length=("timestamp", "size"),
        max_change_score=("change_score", "max"),
    )
    .reset_index()
)

summary_df = pd.DataFrame([{
    "row_count": len(sensor_df),
    "cusum_alarm_count": int(sensor_df["cusum_alarm"].sum()),
    "ewma_alarm_count": int(sensor_df["ewma_alarm"].sum()),
    "variance_alarm_count": int(sensor_df["variance_alarm"].sum()),
    "multi_sensor_alarm_count": int(sensor_df["multi_sensor_alarm"].sum()),
    "combined_alarm_count": int(sensor_df["any_alarm"].sum()),
    "segment_count": len(segments_df),
}])

alarm_df = sensor_df.loc[sensor_df["any_alarm"]]

excel_file = OUTPUT_DIR / "ex080_change_detection_report.xlsx"
with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
    summary_df.to_excel(writer, sheet_name="summary", index=False)
    alarm_df.to_excel(writer, sheet_name="alarm_rows", index=False)
    segments_df.to_excel(writer, sheet_name="segments", index=False)

summary_df.to_csv(
    OUTPUT_DIR / "ex080_change_detection_summary.csv",
    index=False,
    encoding="utf-8-sig",
)

print(summary_df)
print("보고서 저장:", excel_file)
