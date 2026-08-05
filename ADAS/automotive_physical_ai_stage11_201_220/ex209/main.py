from common.anomaly_utils import load_data, zscore, output_path
df = load_data()
features = ["accel_mps2","steering_deg","motor_current_a"]
for col in features:
    df[f"{col}_z"] = zscore(df[col])
df["z_anomaly"] = (
    (df["accel_mps2_z"].abs() > 3) |
    (df["steering_deg_z"].abs() > 3) |
    (df["motor_current_a_z"].abs() > 3)
)
path = output_path("ex209_zscore_anomalies.csv")
df[df["z_anomaly"]].to_csv(path,index=False,encoding="utf-8-sig")
print("detected:", int(df["z_anomaly"].sum()))
