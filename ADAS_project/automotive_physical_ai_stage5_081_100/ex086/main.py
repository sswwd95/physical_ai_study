from common.sync_utils import load_stream, nearest_merge, out
wheel = load_stream("wheel_20hz.csv")
imu = load_stream("imu_50hz.csv")
merged = nearest_merge(wheel, imu, tolerance=0.03)
path = out("ex086_wheel_imu_nearest.csv")
merged.to_csv(path,index=False)
print(merged.head())
print("missing:", merged.isna().sum().to_dict())
