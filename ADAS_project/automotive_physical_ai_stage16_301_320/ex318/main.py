import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common.control_utils import PID, simulate_first_order, output_path
df=simulate_first_order(PID(1.5,.7,.1,2.0,2.0),1.0)
fig,ax=plt.subplots(figsize=(9,4))
ax.plot(df["time_s"],df["target"],label="target")
ax.plot(df["time_s"],df["measurement"],label="measurement")
ax.plot(df["time_s"],df["control"],label="control",alpha=.7)
ax.grid(True); ax.legend(); ax.set_xlabel("Time (s)")
p=output_path("ex318_pid_response.png")
fig.tight_layout(); fig.savefig(p,dpi=140); plt.close(fig)
print(p)
