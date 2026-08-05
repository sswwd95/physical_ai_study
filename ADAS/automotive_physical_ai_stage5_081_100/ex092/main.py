import numpy as np
wheel_var, gps_var = 0.10**2, 0.45**2
wheel_weight = (1/wheel_var) / ((1/wheel_var)+(1/gps_var))
gps_weight = 1-wheel_weight
print("wheel weight:", round(wheel_weight,3))
print("gps weight:", round(gps_weight,3))
