import json
from common.sensor_utils import load_data, rmse, output_path
df = load_data()
normal = df["slip_flag"] == 0
report = {
    "rows": len(df),
    "duration_s": float(df["time_s"].max()),
    "accel_rmse": rmse(df["imu_ax_mps2"], df["true_accel_mps2"]),
    "gyro_rmse": rmse(df["imu_gyroz_rps"], df["true_yaw_rate_rps"]),
    "encoder_speed_rmse_normal": rmse(df.loc[normal,"encoder_speed_mps"], df.loc[normal,"true_speed_mps"]),
    "slip_samples": int(df["slip_flag"].sum()),
}
path = output_path("ex159_sensor_quality_report.json")
path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
print(report)
print("saved:", path)
