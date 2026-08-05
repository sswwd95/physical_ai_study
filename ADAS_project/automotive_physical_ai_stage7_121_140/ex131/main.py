from pathlib import Path
import pandas as pd
from common.diff_drive import integrate_odometry, output_path
cmd = pd.read_csv(Path(__file__).resolve().parents[1] / "data" / "drive_commands.csv")
commands = [
    (r.linear_mps, r.angular_rps, r.duration_s, r.mode)
    for r in cmd.itertuples(index=False)
]
df = integrate_odometry(commands, dt=0.05)
path = output_path("ex131_composite_odometry.csv")
df.to_csv(path, index=False, encoding="utf-8-sig")
print(df.groupby("mode").size())
print("saved:", path)
