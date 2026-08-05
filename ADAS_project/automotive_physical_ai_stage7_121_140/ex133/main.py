from pathlib import Path
import pandas as pd
from common.diff_drive import integrate_odometry, path_length
cmd = pd.read_csv(Path(__file__).resolve().parents[1] / "data" / "drive_commands.csv")
commands = [(r.linear_mps, r.angular_rps, r.duration_s, r.mode) for r in cmd.itertuples(index=False)]
df = integrate_odometry(commands, dt=0.05)
print("path length (m):", round(path_length(df), 4))
print("final displacement (m):", round((df.iloc[-1].x_m**2 + df.iloc[-1].y_m**2)**0.5, 4))
