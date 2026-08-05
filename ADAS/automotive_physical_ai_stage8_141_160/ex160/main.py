import json, numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common.sensor_utils import load_data, rmse, moving_average, output_path
df = load_data()
accel_bias = (df.loc[df["time_s"] < 5,"imu_ax_mps2"] - df.loc[df["time_s"] < 5,"true_accel_mps2"]).mean()
gyro_bias = (df.loc[df["time_s"] < 5,"imu_gyroz_rps"] - df.loc[df["time_s"] < 5,"true_yaw_rate_rps"]).mean()
df["accel_corrected"] = moving_average(df["imu_ax_mps2"] - accel_bias, 21)
df["gyro_corrected"] = df["imu_gyroz_rps"] - gyro_bias
dt = df["time_s"].diff().fillna(0)
df["yaw_corrected"] = np.cumsum(df["gyro_corrected"] * dt)
df["slip_detected"] = (df["encoder_speed_mps"] - df["true_speed_mps"]).abs() > 0.03

csv_path = output_path("ex160_integrated_sensor_analysis.csv")
df[["time_s","true_accel_mps2","accel_corrected","true_yaw_rad","yaw_corrected",
    "true_speed_mps","encoder_speed_mps","slip_flag","slip_detected"]].to_csv(
        csv_path,index=False,encoding="utf-8-sig"
    )

fig, axes = plt.subplots(3,1,figsize=(11,9),sharex=True)
axes[0].plot(df["time_s"],df["true_accel_mps2"],label="true")
axes[0].plot(df["time_s"],df["accel_corrected"],alpha=.7,label="corrected")
axes[0].legend(); axes[0].grid(True); axes[0].set_ylabel("Accel")
axes[1].plot(df["time_s"],df["true_yaw_rad"],label="true")
axes[1].plot(df["time_s"],df["yaw_corrected"],label="integrated")
axes[1].legend(); axes[1].grid(True); axes[1].set_ylabel("Yaw")
axes[2].plot(df["time_s"],df["true_speed_mps"],label="true")
axes[2].plot(df["time_s"],df["encoder_speed_mps"],alpha=.6,label="encoder")
axes[2].legend(); axes[2].grid(True); axes[2].set_ylabel("Speed"); axes[2].set_xlabel("Time (s)")
plot_path = output_path("ex160_integrated_sensor_analysis.png")
fig.tight_layout(); fig.savefig(plot_path,dpi=140); plt.close(fig)

summary = {
    "accel_bias_estimate": float(accel_bias),
    "gyro_bias_estimate": float(gyro_bias),
    "corrected_accel_rmse": rmse(df["accel_corrected"],df["true_accel_mps2"]),
    "corrected_yaw_rmse": rmse(df["yaw_corrected"],df["true_yaw_rad"]),
    "slip_detection_samples": int(df["slip_detected"].sum()),
}
summary_path = output_path("ex160_summary.json")
summary_path.write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding="utf-8")
print(summary)
print("saved:", csv_path, plot_path, summary_path)
