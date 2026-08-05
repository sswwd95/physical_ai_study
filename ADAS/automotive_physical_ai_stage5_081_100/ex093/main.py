import numpy as np, pandas as pd
from common.sync_utils import load_stream, out
imu = load_stream("imu_50hz.csv")
dt = imu["timestamp_s"].diff().fillna(0).to_numpy()
imu["imu_speed_est_mps"] = np.cumsum(imu["imu_ax_mps2"].to_numpy()*dt)
path = out("ex093_imu_integrated_speed.csv")
imu.to_csv(path,index=False)
print(imu[["timestamp_s","imu_speed_est_mps"]].head())
