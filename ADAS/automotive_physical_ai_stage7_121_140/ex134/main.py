from pathlib import Path
import pandas as pd
from common.diff_drive import integrate_odometry
cmd = pd.read_csv(Path(__file__).resolve().parents[1] / "data" / "drive_commands.csv")
commands = [(r.linear_mps, r.angular_rps, r.duration_s, r.mode) for r in cmd.itertuples(index=False)]
for dt in [0.20, 0.10, 0.05, 0.01]:
    df = integrate_odometry(commands, dt=dt)
    last = df.iloc[-1]
    print("dt=", dt, "final=", round(last.x_m,4), round(last.y_m,4), round(last.yaw_rad,4))
