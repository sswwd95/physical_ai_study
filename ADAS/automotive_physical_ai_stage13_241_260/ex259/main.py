import pymc as pm, arviz as az
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common.risk_utils import load_data,standardize,sample_model,output_path
df=load_data(); x1=standardize(df["ttc_s"]).to_numpy(); x2=standardize(df["slip_ratio"]).to_numpy(); y=df["risk_label"].to_numpy()
with pm.Model() as model:
    a=pm.Normal("intercept",0,2); b1=pm.Normal("b_ttc",0,2); b2=pm.Normal("b_slip",0,2)
    p=pm.math.sigmoid(a+b1*x1+b2*x2); pm.Bernoulli("obs",p=p,observed=y)
idata=sample_model(model)
az.plot_posterior(idata,var_names=["b_ttc","b_slip"],hdi_prob=.95)
pth=output_path("ex259_posterior_plot.png"); plt.tight_layout(); plt.savefig(pth,dpi=140); plt.close("all")
print(pth)
