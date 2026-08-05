import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.stats import beta
from common.bayes_slip_utils import output_path
x = np.linspace(0.001, 0.40, 400)
y = beta.pdf(x/0.4, a=2, b=8) / 0.4
fig, ax = plt.subplots(figsize=(8,4))
ax.plot(x, y)
ax.set_title("Prior Distribution of Slip Ratio")
ax.set_xlabel("Slip ratio")
ax.set_ylabel("Density")
ax.grid(True)
path = output_path("ex183_slip_prior.png")
fig.tight_layout()
fig.savefig(path, dpi=140)
plt.close(fig)
print("saved:", path)
