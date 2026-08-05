from common.anomaly_utils import load_data, output_path
df = load_data()
df["risk_score"] = (
    (df["accel_mps2"].abs() > 1.8).astype(int)*2 +
    (df["steering_deg"].abs() > 15).astype(int)*2 +
    (df["ttc_s"] < 2).astype(int)*3 +
    (df["motor_current_a"] > 7).astype(int)*2
)
df["risk_level"] = df["risk_score"].map(
    lambda x: "HIGH" if x >= 4 else ("MEDIUM" if x >= 2 else "LOW")
)
path = output_path("ex212_risk_score.csv")
df.to_csv(path,index=False,encoding="utf-8-sig")
print(df["risk_level"].value_counts())
