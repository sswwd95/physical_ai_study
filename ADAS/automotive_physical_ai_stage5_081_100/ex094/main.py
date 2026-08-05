import numpy as np
from common.sync_utils import load_stream, out
imu = load_stream("imu_50hz.csv")
bias = imu.loc[imu["timestamp_s"] < 2, "imu_ax_mps2"].mean()
dt = imu["timestamp_s"].diff().fillna(0)
imu["imu_ax_corrected"] = imu["imu_ax_mps2"] - bias
imu["speed_est_mps"] = np.cumsum(imu["imu_ax_corrected"]*dt)
path = out("ex094_bias_corrected_integration.csv")
imu.to_csv(path,index=False)
print("estimated bias:", round(bias,4))
