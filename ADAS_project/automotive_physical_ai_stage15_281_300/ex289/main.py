import numpy as np, pymc as pm
from common.reliability_utils import load_lifetime,sample_model,save_json
y=load_lifetime().query("failure_event==1")["observed_time_h"].to_numpy()
with pm.Model() as model:
    a=pm.HalfNormal("alpha",5); b=pm.HalfNormal("beta",2000)
    pm.Weibull("obs",alpha=a,beta=b,observed=y)
idata=sample_model(model)
aa=idata.posterior["alpha"].values.reshape(-1); bb=idata.posterior["beta"].values.reshape(-1)
times=[500,1000,1500]
survival={str(t):float(np.mean(np.exp(-(t/bb)**aa))) for t in times}
print(survival); print(save_json(survival,"ex289_survival_probability.json"))
