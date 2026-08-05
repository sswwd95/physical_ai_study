import json
from common.anomaly_utils import load_data, confusion_counts, output_path
df = load_data()
truth = df["event_label"] != "NORMAL"
pred = (
    (df["accel_mps2"].abs() > 1.8) |
    (df["steering_deg"].abs() > 15) |
    (df["ttc_s"] < 2) |
    (df["motor_current_a"] > 7)
)
c = confusion_counts(truth,pred)
report = {
    "rows": len(df),
    "true_anomaly_samples": int(truth.sum()),
    "predicted_anomaly_samples": int(pred.sum()),
    **c,
    "precision": c["tp"]/max(1,c["tp"]+c["fp"]),
    "recall": c["tp"]/max(1,c["tp"]+c["fn"]),
}
path = output_path("ex219_anomaly_quality_report.json")
path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
print(report)
print("saved:", path)
