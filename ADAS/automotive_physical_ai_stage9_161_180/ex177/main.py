import pymc as pm
from common.bayes_utils import load_data,sample_model
y=load_data()["outlier_measurement_mps2"].to_numpy()
with pm.Model() as m1:
    b1=pm.Normal("bias",0,.1); s1=pm.HalfNormal("sigma",.1); pm.Normal("obs",b1,s1,observed=y)
i1=sample_model(m1)
with pm.Model() as m2:
    b2=pm.Normal("bias",0,.1); s2=pm.HalfNormal("sigma",.1); pm.StudentT("obs",nu=4,mu=b2,sigma=s2,observed=y)
i2=sample_model(m2); print(float(i1.posterior["bias"].mean()),float(i2.posterior["bias"].mean()))
