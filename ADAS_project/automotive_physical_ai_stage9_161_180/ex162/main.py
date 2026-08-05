from common.bayes_utils import load_data
df=load_data(); x=df["accel_measurement_mps2"]
print(x.describe()); print("mean:",x.mean(),"std:",x.std())
