from common.diff_drive import integrate_odometry, output_path
df = integrate_odometry([(0.0, 1.0, 3.14159, "spin")], dt=0.05)
path = output_path("ex129_spin_odometry.csv")
df.to_csv(path, index=False, encoding="utf-8-sig")
print(df.tail())
print("saved:", path)
