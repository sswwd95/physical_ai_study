from common.data_utils import load_vehicle_data, output_path

df = load_vehicle_data()
events = df[df["accel_mps2"] <= -1.8][
    ["timestamp", "time_s", "speed_mps", "accel_mps2", "brake_pct"]
].copy()
path = output_path("ex070_hard_braking.csv")
events.to_csv(path, index=False, encoding="utf-8-sig")
print(f"hard braking samples: {len(events)}")
print(events.head(10))
print(f"saved: {path}")
