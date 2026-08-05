from pathlib import Path
import json, pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common.diff_drive import integrate_odometry, path_length, output_path, twist_to_wheels
cmd = pd.read_csv(Path(__file__).resolve().parents[1] / "data" / "drive_commands.csv")
commands = [(r.linear_mps, r.angular_rps, r.duration_s, r.mode) for r in cmd.itertuples(index=False)]
df = integrate_odometry(commands, dt=0.05)
wheel_rows = []
for r in cmd.itertuples(index=False):
    left, right = twist_to_wheels(r.linear_mps, r.angular_rps)
    wheel_rows.append([r.mode, r.linear_mps, r.angular_rps, left, right, r.duration_s])
wheel_df = pd.DataFrame(wheel_rows, columns=[
    "mode","linear_mps","angular_rps","left_rad_s","right_rad_s","duration_s"
])
traj_path = output_path("ex140_integrated_trajectory.csv")
wheel_path = output_path("ex140_wheel_commands.csv")
df.to_csv(traj_path,index=False,encoding="utf-8-sig")
wheel_df.to_csv(wheel_path,index=False,encoding="utf-8-sig")
fig, ax = plt.subplots(figsize=(6,6))
for mode, group in df.groupby("mode", sort=False):
    ax.plot(group["x_m"], group["y_m"], label=mode)
ax.set_aspect("equal", adjustable="box")
ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")
ax.set_title("Integrated Differential Drive Analysis")
ax.grid(True)
ax.legend()
plot_path = output_path("ex140_integrated_trajectory.png")
fig.tight_layout()
fig.savefig(plot_path,dpi=140)
plt.close(fig)
last = df.iloc[-1]
summary = {
    "path_length_m": path_length(df),
    "final_pose": [float(last.x_m), float(last.y_m), float(last.yaw_rad)],
    "command_count": len(wheel_df),
    "trajectory_samples": len(df)
}
summary_path = output_path("ex140_summary.json")
summary_path.write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding="utf-8")
print(summary)
print("saved:", traj_path, wheel_path, plot_path, summary_path)
