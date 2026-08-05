from common.anomaly_utils import load_data, confusion_counts
df = load_data()
truth = df["event_label"] != "NORMAL"
pred = (
    (df["accel_mps2"].abs() > 1.8) |
    (df["steering_deg"].abs() > 15) |
    (df["ttc_s"] < 2) |
    (df["motor_current_a"] > 7)
)
counts = confusion_counts(truth, pred)
precision = counts["tp"] / max(1, counts["tp"]+counts["fp"])
recall = counts["tp"] / max(1, counts["tp"]+counts["fn"])
print(counts)
print("precision:", round(precision,4))
print("recall:", round(recall,4))
