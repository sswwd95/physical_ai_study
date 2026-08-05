import pymc as pm
from common.bayes_utils import load_data,sample_model
x=load_data()["accel_measurement_mps2"].to_numpy()
for ps in [.02,.1,.5]:
    with pm.Model() as model:
        bias=pm.Normal("bias",0,ps); sigma=pm.HalfNormal("sigma",.1); pm.Normal("obs",bias,sigma,observed=x)
    print(ps,float(sample_model(model).posterior["bias"].mean()))
