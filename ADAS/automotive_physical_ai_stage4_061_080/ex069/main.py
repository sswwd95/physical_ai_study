from common.data_utils import load_vehicle_data, output_path

df = load_vehicle_data()
events = df[df["accel_mps2"] >= 1.5][
    ["timestamp", "time_s", "speed_mps", "accel_mps2", "throttle_pct"]
].copy()
path = output_path("ex069_hard_acceleration.csv")
events.to_csv(path, index=False, encoding="utf-8-sig")
print(f"hard acceleration samples: {len(events)}")
print(events.head(10))
print(f"saved: {path}")
