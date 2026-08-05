from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from common.health_utils import load_data,FEATURES,output_path
df=load_data(); split=int(len(df)*.7)
model=RandomForestClassifier(n_estimators=180,class_weight="balanced",random_state=42,n_jobs=1)
model.fit(df.iloc[:split][FEATURES],df.iloc[:split]["failure_label"])
pred=model.predict(df.iloc[split:][FEATURES])
report=classification_report(df.iloc[split:]["failure_label"],pred,output_dict=True,zero_division=0)
p=output_path("ex274_random_forest_failure_report.json")
p.write_text(__import__("json").dumps(report,indent=2),encoding="utf-8")
print(report)
