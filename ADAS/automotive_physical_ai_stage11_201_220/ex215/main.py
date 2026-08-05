from sklearn.ensemble import IsolationForest
from common.anomaly_utils import load_data, output_path
df = load_data()
features = df[["speed_mps","accel_mps2","steering_deg","ttc_s","motor_current_a"]]
model = IsolationForest(contamination=0.10, random_state=42)
df["iforest_anomaly"] = model.fit_predict(features) == -1
path = output_path("ex215_isolation_forest.csv")
df[df["iforest_anomaly"]].to_csv(path,index=False,encoding="utf-8-sig")
print("detected:", int(df["iforest_anomaly"].sum()))
