import pandas as pd
from common.data_utils import load_vehicle_data, output_path

df = load_vehicle_data()
df["voltage_drop_v"] = df["battery_voltage_v"].max() - df["battery_voltage_v"]
summary = df.groupby(pd.cut(df["motor_current_a"], bins=4, duplicates="drop")).agg(
    samples=("battery_voltage_v", "size"),
    mean_current_a=("motor_current_a", "mean"),
    mean_voltage_v=("battery_voltage_v", "mean"),
    mean_drop_v=("voltage_drop_v", "mean"),
)
path = output_path("ex076_voltage_drop_summary.csv")
summary.to_csv(path, encoding="utf-8-sig")
print(summary)
print(f"saved: {path}")
