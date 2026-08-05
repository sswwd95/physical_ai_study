import json
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from common.health_utils import load_data,FEATURES,output_path
df=load_data(); split=int(len(df)*.7)
model=RandomForestClassifier(n_estimators=220,class_weight="balanced",random_state=42,n_jobs=1)
model.fit(df.iloc[:split][FEATURES],df.iloc[:split]["failure_label"])
prob=model.predict_proba(df.iloc[split:][FEATURES])[:,1]
pred=(prob>=0.35).astype(int)
report=classification_report(df.iloc[split:]["failure_label"],pred,output_dict=True,zero_division=0)
result=df.iloc[split:][["time_s","health_score","failure_label"]].copy()
result["failure_probability"]=prob; result["predicted_failure"]=pred
csv_path=output_path("ex280_failure_predictions.csv"); result.to_csv(csv_path,index=False,encoding="utf-8-sig")
last=df.iloc[-1]
summary={
"final_health_score":float(last["health_score"]),
"final_motor_temp_c":float(last["motor_temp_c"]),
"final_vibration_g":float(last["bearing_vibration_g"]),
"final_battery_voltage_v":float(last["battery_voltage_v"]),
"failure_samples":int(df["failure_label"].sum()),
"classification_report":report}
json_path=output_path("ex280_integrated_report.json"); json_path.write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding="utf-8")
print(summary)
print(csv_path,json_path)
