from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from common.feature_utils import load_data,FEATURES,metrics,save_json
df=load_data(); s=int(len(df)*.7); m=make_pipeline(StandardScaler(),LogisticRegression(class_weight='balanced',max_iter=1000,random_state=42)); m.fit(df.iloc[:s][FEATURES],df.iloc[:s].anomaly_label); r=metrics(df.iloc[s:].anomaly_label,m.predict(df.iloc[s:][FEATURES])); print(r); print(save_json(r,'ex231_logistic_metrics.json'))
