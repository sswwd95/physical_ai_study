from common.diff_drive import integrate_odometry, output_path
df = integrate_odometry([(0.15, 0.50, 6.0, "arc")], dt=0.05)
path = output_path("ex130_arc_odometry.csv")
df.to_csv(path, index=False, encoding="utf-8-sig")
print(df.tail())
print("saved:", path)
