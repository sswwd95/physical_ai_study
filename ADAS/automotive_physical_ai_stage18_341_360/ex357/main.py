from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from common.safety_utils import load_data,output_path
df=load_data(); split=int(len(df)*.7)
features=["ego_speed_mps","lead_speed_mps","relative_speed_mps","distance_m","ttc_s","friction_coeff","obstacle_angle_deg"]
model=RandomForestClassifier(n_estimators=160,class_weight="balanced",random_state=42,n_jobs=1)
model.fit(df.iloc[:split][features],df.iloc[:split]["risk_label"])
pred=model.predict(df.iloc[split:][features])
report=classification_report(df.iloc[split:]["risk_label"],pred,output_dict=True,zero_division=0)
p=output_path("ex357_random_forest_risk_report.json")
p.write_text(__import__("json").dumps(report,indent=2),encoding="utf-8")
print(report)
