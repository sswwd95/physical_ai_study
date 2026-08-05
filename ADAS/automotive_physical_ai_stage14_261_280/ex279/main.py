import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common.health_utils import load_data,output_path
df=load_data()
fig,axes=plt.subplots(4,1,figsize=(11,10),sharex=True)
axes[0].plot(df["time_s"],df["motor_temp_c"]); axes[0].set_ylabel("Temp C"); axes[0].grid(True)
axes[1].plot(df["time_s"],df["bearing_vibration_g"]); axes[1].set_ylabel("Vibration g"); axes[1].grid(True)
axes[2].plot(df["time_s"],df["battery_voltage_v"]); axes[2].set_ylabel("Voltage V"); axes[2].grid(True)
axes[3].plot(df["time_s"],df["health_score"]); axes[3].set_ylabel("Health"); axes[3].set_xlabel("Time s"); axes[3].grid(True)
p=output_path("ex279_component_dashboard.png"); fig.tight_layout(); fig.savefig(p,dpi=140); plt.close(fig)
print(p)
