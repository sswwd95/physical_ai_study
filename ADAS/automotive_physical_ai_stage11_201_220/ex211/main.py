from common.anomaly_utils import load_data, output_path
df = load_data()
window = 50
mean = df["motor_current_a"].rolling(window,min_periods=20).mean()
std = df["motor_current_a"].rolling(window,min_periods=20).std()
df["rolling_anomaly"] = df["motor_current_a"] > (mean + 3*std)
path = output_path("ex211_rolling_current_anomalies.csv")
df[df["rolling_anomaly"]].to_csv(path,index=False,encoding="utf-8-sig")
print("detected:", int(df["rolling_anomaly"].sum()))
