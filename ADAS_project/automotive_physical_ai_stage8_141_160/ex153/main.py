from common.sensor_utils import load_data, rmse
df = load_data()
normal = df["slip_flag"] == 0
print("normal-section RMSE:", round(rmse(df.loc[normal,"encoder_speed_mps"], df.loc[normal,"true_speed_mps"]),6))
error = df.loc[normal,"encoder_speed_mps"] - df.loc[normal,"true_speed_mps"]
print("mean error:", round(error.mean(),6))
print("std error:", round(error.std(),6))
