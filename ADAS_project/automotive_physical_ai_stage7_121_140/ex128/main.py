from common.diff_drive import integrate_odometry, output_path
df = integrate_odometry([(0.20, 0.0, 5.0, "forward")], dt=0.05)
path = output_path("ex128_straight_odometry.csv")
df.to_csv(path, index=False, encoding="utf-8-sig")
print(df.tail())
print("saved:", path)
