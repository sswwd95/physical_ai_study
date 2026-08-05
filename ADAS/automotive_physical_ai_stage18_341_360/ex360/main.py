import json,numpy as np
from common.safety_utils import load_data,hysteresis_alarm,confusion_counts,output_path
df=load_data()
df["warning"]=hysteresis_alarm(df["ttc_s"],2.0,3.0)
df["emergency_stop"]=(df["ttc_s"]<1.0)|(df["distance_m"]<2.5)
ratio=np.clip(df["distance_m"]/df["safe_distance_m"],0,1.2)
df["target_speed_mps"]=df["ego_speed_mps"]*np.clip(ratio,0,1)
df["decel_cmd_mps2"]=np.clip(df["target_speed_mps"]-df["ego_speed_mps"],-4.0,0.0)
df["avoidance_yaw_rate_rps"]=np.where(
    (df["warning"]) & (~df["emergency_stop"]),
    np.clip(-0.05*df["obstacle_angle_deg"],-1.0,1.0),
    0.0
)
pred=df["warning"]|df["emergency_stop"]
counts=confusion_counts(df["risk_label"],pred)
csv_path=output_path("ex360_integrated_safety_control.csv")
df.to_csv(csv_path,index=False,encoding="utf-8-sig")
report={
    "rows":len(df),
    "warning_samples":int(df["warning"].sum()),
    "emergency_stop_samples":int(df["emergency_stop"].sum()),
    "max_deceleration_mps2":float(df["decel_cmd_mps2"].min()),
    "max_abs_avoidance_yaw_rate_rps":float(df["avoidance_yaw_rate_rps"].abs().max()),
    "confusion":counts,
    "precision":counts["tp"]/max(1,counts["tp"]+counts["fp"]),
    "recall":counts["tp"]/max(1,counts["tp"]+counts["fn"])
}
json_path=output_path("ex360_integrated_report.json")
json_path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
print(report)
print(csv_path,json_path)
