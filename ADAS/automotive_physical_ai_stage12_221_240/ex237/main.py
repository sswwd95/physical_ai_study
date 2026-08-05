import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from common.feature_utils import load_data,FEATURES,metrics,output_path
df=load_data(); s=int(len(df)*.7); m=RandomForestClassifier(n_estimators=150,class_weight='balanced',random_state=42,n_jobs=1).fit(df.iloc[:s][FEATURES],df.iloc[:s].anomaly_label); p=m.predict_proba(df.iloc[s:][FEATURES])[:,1]; o=pd.DataFrame([{'threshold':th,**metrics(df.iloc[s:].anomaly_label,p>=th)} for th in [.1,.2,.3,.4,.5,.6,.7,.8,.9]]); o.to_csv(output_path('ex237_probability_thresholds.csv'),index=False); print(o.sort_values('f1',ascending=False).head())
