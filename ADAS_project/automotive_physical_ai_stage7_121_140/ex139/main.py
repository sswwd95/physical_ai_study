from pathlib import Path
import json, pandas as pd
from common.diff_drive import integrate_odometry, path_length, output_path
cmd = pd.read_csv(Path(__file__).resolve().parents[1] / "data" / "drive_commands.csv")
commands = [(r.linear_mps, r.angular_rps, r.duration_s, r.mode) for r in cmd.itertuples(index=False)]
df = integrate_odometry(commands, dt=0.05)
last = df.iloc[-1]
report = {
    "samples": len(df),
    "duration_s": float(df["time_s"].max()),
    "path_length_m": path_length(df),
    "final_x_m": float(last.x_m),
    "final_y_m": float(last.y_m),
    "final_yaw_rad": float(last.yaw_rad),
}
path = output_path("ex139_odometry_report.json")
path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
print(report)
print("saved:", path)
