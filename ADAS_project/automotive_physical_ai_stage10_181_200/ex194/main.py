import pymc as pm
from common.bayes_slip_utils import load_data, sample_model, save_summary
df = load_data()
x1 = (df["wheel_speed_diff_mps"] - df["wheel_speed_diff_mps"].mean()) / df["wheel_speed_diff_mps"].std()
x2 = (df["imu_accel_std"] - df["imu_accel_std"].mean()) / df["imu_accel_std"].std()
y = df["risk_label"].to_numpy()
with pm.Model() as model:
    intercept = pm.Normal("intercept", 0.0, 2.0)
    b1 = pm.Normal("b_wheel", 0.0, 2.0)
    b2 = pm.Normal("b_imu", 0.0, 2.0)
    p = pm.math.sigmoid(intercept + b1*x1.to_numpy() + b2*x2.to_numpy())
    pm.Bernoulli("obs", p=p, observed=y)
idata = sample_model(model)
summary, path = save_summary(idata, ["intercept","b_wheel","b_imu"], "ex194_slip_risk_logistic.csv")
print(summary)
print("saved:", path)
