import pymc as pm
from common.bayes_utils import load_data,sample_model,save_summary
x=load_data()["gyro_measurement_rps"].to_numpy()
with pm.Model() as model:
    bias=pm.Normal("bias",0,.05); sigma=pm.HalfNormal("sigma",.03); pm.Normal("obs",bias,sigma,observed=x)
idata=sample_model(model); s,p=save_summary(idata,["bias","sigma"],"ex166_gyro_summary.csv"); print(s); print(p)
