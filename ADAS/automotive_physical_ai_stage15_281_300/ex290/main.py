import numpy as np, pymc as pm
from common.reliability_utils import load_lifetime,sample_model
y=load_lifetime().query("failure_event==1")["observed_time_h"].to_numpy()
with pm.Model() as model:
    a=pm.HalfNormal("alpha",5); b=pm.HalfNormal("beta",2000)
    pm.Weibull("obs",alpha=a,beta=b,observed=y)
idata=sample_model(model)
aa=idata.posterior["alpha"].values.reshape(-1); bb=idata.posterior["beta"].values.reshape(-1)
median_life=bb*(np.log(2)**(1/aa))
print("posterior median life mean:",median_life.mean())
print("95% interval:",np.quantile(median_life,[.025,.975]))
