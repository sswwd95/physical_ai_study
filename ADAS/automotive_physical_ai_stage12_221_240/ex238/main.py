import pandas as pd
from sklearn.model_selection import TimeSeriesSplit
from sklearn.ensemble import RandomForestClassifier
from common.feature_utils import load_data,FEATURES,metrics,output_path
df=load_data(); r=[]
for i,(tr,te) in enumerate(TimeSeriesSplit(n_splits=5).split(df),1):
 m=RandomForestClassifier(n_estimators=100,class_weight='balanced',random_state=42,n_jobs=1).fit(df.iloc[tr][FEATURES],df.iloc[tr].anomaly_label); r.append({'fold':i,**metrics(df.iloc[te].anomaly_label,m.predict(df.iloc[te][FEATURES]))})
o=pd.DataFrame(r); o.to_csv(output_path('ex238_time_series_cv.csv'),index=False); print(o)
