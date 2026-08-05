import numpy as np

samples = np.array([7.1, 7.4, 7.2, 7.8, 8.0, 7.5, 7.3])

print("mean:", round(float(np.mean(samples)), 3))
print("std :", round(float(np.std(samples, ddof=1)), 3))
print("p25 :", round(float(np.percentile(samples, 25)), 3))
print("p75 :", round(float(np.percentile(samples, 75)), 3))
