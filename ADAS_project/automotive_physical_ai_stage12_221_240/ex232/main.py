from sklearn.ensemble import RandomForestClassifier
from common.feature_utils import load_data,FEATURES,metrics,save_json
df=load_data(); s=int(len(df)*.7); m=RandomForestClassifier(n_estimators=150,class_weight='balanced',random_state=42,n_jobs=1); m.fit(df.iloc[:s][FEATURES],df.iloc[:s].anomaly_label); r=metrics(df.iloc[s:].anomaly_label,m.predict(df.iloc[s:][FEATURES])); print(r); print(save_json(r,'ex232_random_forest_metrics.json'))
