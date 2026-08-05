import numpy as np

speed_mps = np.array([4.2, 5.1, 5.8, 6.4])
calibration_offset = -0.15
corrected = speed_mps + calibration_offset
speed_kph = corrected * 3.6

print("보정 속도(m/s):", np.round(corrected, 2))
print("변환 속도(km/h):", np.round(speed_kph, 2))
