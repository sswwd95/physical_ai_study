import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.stats import norm
from common.bayes_utils import output_path
x=np.linspace(-.15,.15,500); y=norm.pdf(x,0,.05)
fig,ax=plt.subplots(figsize=(8,4)); ax.plot(x,y); ax.grid(True); ax.set_title("Accelerometer Bias Prior")
p=output_path("ex163_accel_bias_prior.png"); fig.tight_layout(); fig.savefig(p,dpi=140); plt.close(fig); print("saved:",p)
