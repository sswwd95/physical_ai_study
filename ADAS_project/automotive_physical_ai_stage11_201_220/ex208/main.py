from common.anomaly_utils import load_data, output_path
df = load_data()
threshold = df["motor_current_a"].mean() + 3*df["motor_current_a"].std()
events = df[df["motor_current_a"] > threshold].copy()
path = output_path("ex208_motor_overcurrent.csv")
events.to_csv(path,index=False,encoding="utf-8-sig")
print("threshold:", round(threshold,3))
print("detected:", len(events))
