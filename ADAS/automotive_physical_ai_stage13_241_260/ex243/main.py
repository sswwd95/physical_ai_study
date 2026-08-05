import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.stats import beta
from common.risk_utils import output_path
x=np.linspace(.001,.999,500)
y=beta.pdf(x,2,8)
fig,ax=plt.subplots(figsize=(8,4))
ax.plot(x,y); ax.set_title("Prior for Overall Risk Probability"); ax.set_xlabel("Risk probability"); ax.grid(True)
p=output_path("ex243_risk_prior.png")
fig.tight_layout(); fig.savefig(p,dpi=140); plt.close(fig)
print("saved:",p)
