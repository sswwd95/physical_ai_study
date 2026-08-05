from common.diff_drive import integrate_odometry
ideal = integrate_odometry([(0.20,0.0,5.0,"ideal")], dt=0.05)
slip = integrate_odometry([(0.17,0.0,5.0,"slip")], dt=0.05)
ideal_x = ideal.iloc[-1].x_m
slip_x = slip.iloc[-1].x_m
print("ideal x:", round(ideal_x,3))
print("actual x with slip:", round(slip_x,3))
print("odometry overestimate:", round(ideal_x-slip_x,3))
