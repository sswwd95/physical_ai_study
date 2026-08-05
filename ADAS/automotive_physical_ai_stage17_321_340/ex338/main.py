import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common.path_tracking import *
path=load_path("path_sine.csv")
def pp(path,x,y,yaw,speed): return pure_pursuit_control(path,x,y,yaw,speed,.8)
df=simulate_tracker(path,pp,.6,23)
fig,ax=plt.subplots(figsize=(10,5))
ax.plot(path["x_m"],path["y_m"],label="reference")
ax.plot(df["x_m"],df["y_m"],label="tracked")
ax.set_aspect("equal",adjustable="box"); ax.grid(True); ax.legend()
p=output_path("ex338_tracking_trajectory.png")
fig.tight_layout(); fig.savefig(p,dpi=140); plt.close(fig)
print(p)
