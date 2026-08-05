import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from common.feature_utils import load_data,FEATURES,output_path
df=load_data(); m=RandomForestClassifier(n_estimators=150,class_weight='balanced',random_state=42,n_jobs=1).fit(df[FEATURES],df.anomaly_label); o=pd.DataFrame({'feature':FEATURES,'importance':m.feature_importances_}).sort_values('importance',ascending=False); o.to_csv(output_path('ex234_feature_importance.csv'),index=False); print(o)
