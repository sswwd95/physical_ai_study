from sklearn.ensemble import IsolationForest
from common.anomaly_utils import load_data, output_path
df = load_data()
features = df[["speed_mps","accel_mps2","steering_deg","ttc_s","motor_current_a"]]
model = IsolationForest(contamination=0.10, random_state=42)
model.fit(features)
df["anomaly_score"] = -model.score_samples(features)
path = output_path("ex216_isolation_scores.csv")
df.sort_values("anomaly_score",ascending=False).head(100).to_csv(path,index=False,encoding="utf-8-sig")
print(df[["time_s","anomaly_score","event_label"]].sort_values("anomaly_score",ascending=False).head())
