import numpy as np
from common.diff_drive import integrate_odometry, output_path
truth = integrate_odometry([(0.18,0.45,6.0,"truth")], dt=0.05)
estimate = integrate_odometry([(0.18,0.40,6.0,"estimate")], dt=0.05)
estimate["position_error_m"] = np.sqrt(
    (truth["x_m"] - estimate["x_m"])**2 +
    (truth["y_m"] - estimate["y_m"])**2
)
path = output_path("ex138_trajectory_error.csv")
estimate.to_csv(path,index=False,encoding="utf-8-sig")
print("final position error:", round(estimate["position_error_m"].iloc[-1],4))
print("RMSE:", round(np.sqrt((estimate["position_error_m"]**2).mean()),4))
