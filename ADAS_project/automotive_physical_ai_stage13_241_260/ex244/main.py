import pymc as pm
from common.risk_utils import load_data,sample_model,save_summary
y=load_data()["risk_label"].to_numpy()
with pm.Model() as model:
    p=pm.Beta("p",alpha=2,beta=8)
    pm.Bernoulli("obs",p=p,observed=y)
idata=sample_model(model)
s,pth=save_summary(idata,["p"],"ex244_overall_risk_probability.csv")
print(s); print("saved:",pth)
