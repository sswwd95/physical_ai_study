import json
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from common.anomaly_utils import load_data, confusion_counts, output_path

df = load_data()
df["driving_state"] = np.select(
    [
        df["speed_mps"] < 0.5,
        df["accel_mps2"] > 1.2,
        df["accel_mps2"] < -1.2,
        df["steering_deg"].abs() > 10,
    ],
    ["STOP","ACCELERATE","DECELERATE","TURN"],
    default="CRUISE"
)
df["rule_anomaly"] = (
    (df["accel_mps2"].abs() > 1.8) |
    (df["steering_deg"].abs() > 15) |
    (df["ttc_s"] < 2) |
    (df["motor_current_a"] > 7)
)
features = df[["speed_mps","accel_mps2","steering_deg","ttc_s","motor_current_a"]]
model = IsolationForest(contamination=0.10,random_state=42)
df["iforest_anomaly"] = model.fit_predict(features) == -1
df["anomaly_score"] = -model.score_samples(features)
df["final_anomaly"] = df["rule_anomaly"] | (
    df["iforest_anomaly"] & (df["anomaly_score"] > df["anomaly_score"].quantile(0.95))
)
csv_path = output_path("ex220_integrated_anomaly_result.csv")
df.to_csv(csv_path,index=False,encoding="utf-8-sig")

truth = df["event_label"] != "NORMAL"
counts = confusion_counts(truth,df["final_anomaly"])
summary = {
    "rows": len(df),
    "state_counts": df["driving_state"].value_counts().to_dict(),
    "rule_anomalies": int(df["rule_anomaly"].sum()),
    "iforest_anomalies": int(df["iforest_anomaly"].sum()),
    "final_anomalies": int(df["final_anomaly"].sum()),
    "confusion": counts,
    "precision": counts["tp"]/max(1,counts["tp"]+counts["fp"]),
    "recall": counts["tp"]/max(1,counts["tp"]+counts["fn"]),
}
json_path = output_path("ex220_integrated_summary.json")
json_path.write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding="utf-8")
print(summary)
print("saved:", csv_path, json_path)
