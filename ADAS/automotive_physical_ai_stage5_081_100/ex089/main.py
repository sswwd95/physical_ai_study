import numpy as np
from common.sync_utils import load_stream
imu = load_stream("imu_50hz.csv")
signal = imu["imu_ax_mps2"].to_numpy()
delayed = np.roll(signal, 12)
corr = np.correlate(delayed-delayed.mean(), signal-signal.mean(), mode="full")
lag = np.argmax(corr) - (len(signal)-1)
print("estimated lag samples:", lag)
print("estimated lag seconds:", lag * 0.02)
