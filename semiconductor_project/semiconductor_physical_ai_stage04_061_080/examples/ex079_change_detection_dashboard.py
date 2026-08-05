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

cusum = []
current = 0.0
for value in z:
    current = max(0.0, current + value - 0.5)
    cusum.append(current)

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
sensor_df["ewma_lcl"] = temp_mean - 3 * ewma_std
sensor_df["cusum_upper"] = cusum

baseline_variance = baseline_temp.var(ddof=1)
sensor_df["variance_ratio"] = (
    sensor_df["chamber_temp_c"]
    .rolling(window=40, min_periods=15)
    .var(ddof=1)
    / baseline_variance
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
sensor_df["severity"] = pd.cut(
    score,
    bins=[-np.inf, 4, 8, 12, np.inf],
    labels=["normal", "caution", "warning", "critical"],
    right=False,
)

dashboard_df = sensor_df[
    [
        "timestamp",
        "lot_id",
        "chamber_temp_c",
        "cusum_upper",
        "temp_ewma",
        "ewma_ucl",
        "ewma_lcl",
        "variance_ratio",
        "change_score",
        "severity",
    ]
]

dashboard_df.to_csv(
    OUTPUT_DIR / "ex079_change_detection_dashboard.csv",
    index=False,
    encoding="utf-8-sig",
)
print(dashboard_df.tail(10).round(3))
