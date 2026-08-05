import pymc as pm
from common.bayes_utils import load_data,sample_model,save_summary
y=load_data()["outlier_measurement_mps2"].to_numpy()
with pm.Model() as model:
    bias=pm.Normal("bias",0,.1); sigma=pm.HalfNormal("sigma",.1); nu=pm.Exponential("nu_minus_one",.1)+1; pm.StudentT("obs",nu=nu,mu=bias,sigma=sigma,observed=y)
i=sample_model(model); s,p=save_summary(i,["bias","sigma"],"ex176_student_t.csv"); print(s); print(p)
