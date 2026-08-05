from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from common.diff_drive import integrate_odometry, output_path
cmd = pd.read_csv(Path(__file__).resolve().parents[1] / "data" / "drive_commands.csv")
commands = [(r.linear_mps, r.angular_rps, r.duration_s, r.mode) for r in cmd.itertuples(index=False)]
df = integrate_odometry(commands, dt=0.05)
fig, ax = plt.subplots(figsize=(6,6))
ax.plot(df["x_m"], df["y_m"])
ax.set_aspect("equal", adjustable="box")
ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")
ax.set_title("Differential Drive Trajectory")
ax.grid(True)
path = output_path("ex132_xy_trajectory.png")
fig.tight_layout()
fig.savefig(path, dpi=140)
plt.close(fig)
print("saved:", path)
