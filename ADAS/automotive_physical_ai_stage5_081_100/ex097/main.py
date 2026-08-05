import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common.sync_utils import load_stream, out
df=load_stream("wheel_20hz.csv")
df["measurement"]=(df["wheel_left_mps"]+df["wheel_right_mps"])/2
x=df["measurement"].iloc[0]; p=1.0; q=0.02; r=0.01; est=[]
for z in df["measurement"]:
    p+=q; k=p/(p+r); x=x+k*(z-x); p=(1-k)*p; est.append(x)
fig,ax=plt.subplots(figsize=(10,4))
ax.plot(df["timestamp_s"],df["measurement"],alpha=.35,label="raw")
ax.plot(df["timestamp_s"],est,label="kalman")
ax.legend(); ax.grid(True); ax.set_xlabel("Time (s)"); ax.set_ylabel("Speed (m/s)")
path=out("ex097_kalman_comparison.png")
fig.tight_layout(); fig.savefig(path,dpi=140); plt.close(fig)
print("saved:",path)
