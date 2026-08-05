import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.stats import beta
from common.reliability_utils import output_path
x=np.linspace(.001,.999,500); y=beta.pdf(x,2,18)
fig,ax=plt.subplots(figsize=(8,4)); ax.plot(x,y); ax.set_title("Prior for Failure Probability"); ax.grid(True)
p=output_path("ex283_failure_probability_prior.png")
fig.tight_layout(); fig.savefig(p,dpi=140); plt.close(fig)
print(p)
