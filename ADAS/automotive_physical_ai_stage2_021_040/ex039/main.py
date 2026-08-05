import matplotlib.pyplot as plt
from common.load_data import load_vehicle_log
from common.paths import OUTPUT_DIR

df = load_vehicle_log()
plt.figure(figsize=(9, 4))
plt.plot(df["time_s"], df["speed_mps"])
plt.xlabel("Time (s)")
plt.ylabel("Speed (m/s)")
plt.title("Vehicle Speed")
plt.tight_layout()
path1 = OUTPUT_DIR / "ex039_speed.png"
plt.savefig(path1, dpi=140)
plt.close()

plt.figure(figsize=(9, 4))
plt.plot(df["time_s"], df["front_distance_m"])
plt.xlabel("Time (s)")
plt.ylabel("Front distance (m)")
plt.title("Front Distance")
plt.tight_layout()
path2 = OUTPUT_DIR / "ex039_distance.png"
plt.savefig(path2, dpi=140)
plt.close()
print(path1)
print(path2)
