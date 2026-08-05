from common.sync_utils import load_stream, out
imu = load_stream("imu_50hz.csv")
offset = imu["timestamp_s"].min()
imu["timestamp_aligned_s"] = imu["timestamp_s"] - offset
path = out("ex088_imu_time_aligned.csv")
imu.to_csv(path,index=False)
print("offset:", offset, "saved:", path)
