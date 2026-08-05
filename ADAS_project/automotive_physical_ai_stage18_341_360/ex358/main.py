import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common.safety_utils import load_data,output_path
df=load_data()
fig,ax=plt.subplots(figsize=(11,5))
ax.plot(df["time_s"],df["distance_m"],label="distance")
ax.plot(df["time_s"],df["safe_distance_m"],label="safe distance")
ax.fill_between(df["time_s"],0,df["distance_m"],where=df["risk_label"].astype(bool),alpha=.25,label="risk")
ax.grid(True); ax.legend(); ax.set_xlabel("Time (s)"); ax.set_ylabel("Distance (m)")
p=output_path("ex358_collision_risk_timeline.png")
fig.tight_layout(); fig.savefig(p,dpi=140); plt.close(fig)
print(p)
