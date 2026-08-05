from sklearn.ensemble import GradientBoostingClassifier
from common.feature_utils import load_data,FEATURES,metrics,save_json
df=load_data(); s=int(len(df)*.7); m=GradientBoostingClassifier(random_state=42); m.fit(df.iloc[:s][FEATURES],df.iloc[:s].anomaly_label); r=metrics(df.iloc[s:].anomaly_label,m.predict(df.iloc[s:][FEATURES])); print(r); print(save_json(r,'ex233_gradient_boosting_metrics.json'))
