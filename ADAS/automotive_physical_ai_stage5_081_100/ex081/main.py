from common.sync_utils import load_stream
for name in ["imu_50hz.csv","wheel_20hz.csv","range_10hz.csv","gps_2hz.csv"]:
    df = load_stream(name)
    dt = df["timestamp_s"].diff().dropna()
    print(name, "samples=", len(df), "mean_dt=", round(dt.mean(),4), "hz=", round(1/dt.mean(),2))
