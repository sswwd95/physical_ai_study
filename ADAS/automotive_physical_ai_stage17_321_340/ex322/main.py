import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common.path_tracking import load_path, output_path
path=load_path("path_sine.csv")
fig,ax=plt.subplots(figsize=(9,4))
ax.plot(path["x_m"],path["y_m"])
ax.set_aspect("equal",adjustable="box"); ax.grid(True)
ax.set_xlabel("X (m)"); ax.set_ylabel("Y (m)")
p=output_path("ex322_reference_path.png")
fig.tight_layout(); fig.savefig(p,dpi=140); plt.close(fig)
print(p)
