import numpy as np, pymc as pm
from common.risk_utils import load_data,sample_model
y=load_data()["risk_label"].to_numpy()
with pm.Model() as model:
    p=pm.Beta("p",2,8)
    pm.Bernoulli("obs",p=p,observed=y)
samples=sample_model(model).posterior["p"].values.reshape(-1)
prob=float(np.mean(samples>.20))
print("P(overall risk rate > 0.20):",prob)
print("decision:","REVIEW" if prob>.95 else "ACCEPT")
