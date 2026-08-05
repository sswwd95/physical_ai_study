from sklearn.ensemble import IsolationForest
from common.anomaly_utils import load_data, confusion_counts
df = load_data()
truth = df["event_label"] != "NORMAL"
rule = (
    (df["accel_mps2"].abs() > 1.8) |
    (df["steering_deg"].abs() > 15) |
    (df["ttc_s"] < 2) |
    (df["motor_current_a"] > 7)
)
features = df[["speed_mps","accel_mps2","steering_deg","ttc_s","motor_current_a"]]
iso = IsolationForest(contamination=0.10, random_state=42).fit_predict(features) == -1
print("rule:", confusion_counts(truth,rule))
print("isolation_forest:", confusion_counts(truth,iso))
