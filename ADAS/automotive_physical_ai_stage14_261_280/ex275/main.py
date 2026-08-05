import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from common.health_utils import load_data,FEATURES,output_path
df=load_data()
model=RandomForestClassifier(n_estimators=180,class_weight="balanced",random_state=42,n_jobs=1)
model.fit(df[FEATURES],df["failure_label"])
imp=pd.DataFrame({"feature":FEATURES,"importance":model.feature_importances_}).sort_values("importance",ascending=False)
p=output_path("ex275_feature_importance.csv"); imp.to_csv(p,index=False,encoding="utf-8-sig")
print(imp)
