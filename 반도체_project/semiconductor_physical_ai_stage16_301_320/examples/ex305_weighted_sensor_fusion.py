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

sensor_df = pd.read_csv(DATA_FILE)

temp_a = sensor_df["temp_sensor_a_c"].interpolate(limit_direction="both")
temp_b = sensor_df["temp_sensor_b_c"].interpolate(limit_direction="both")

var_a = np.nanvar(temp_a - sensor_df["true_temperature_c"])
var_b = np.nanvar(temp_b - sensor_df["true_temperature_c"])

weight_a = 1 / var_a
weight_b = 1 / var_b
weight_sum = weight_a + weight_b

sensor_df["fused_temperature_c"] = (
    weight_a * temp_a + weight_b * temp_b
) / weight_sum

rmse = np.sqrt(
    np.mean(
        (
            sensor_df["fused_temperature_c"]
            - sensor_df["true_temperature_c"]
        ) ** 2
    )
)

print("센서 A 가중치:", round(weight_a / weight_sum, 4))
print("센서 B 가중치:", round(weight_b / weight_sum, 4))
print("융합 RMSE:", round(rmse, 4))
