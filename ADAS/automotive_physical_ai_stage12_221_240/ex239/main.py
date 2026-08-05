import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from common.feature_utils import load_data,FEATURES,metrics,output_path
df=load_data(); s=int(len(df)*.7); ms={'logistic':make_pipeline(StandardScaler(),LogisticRegression(class_weight='balanced',max_iter=1000,random_state=42)),'random_forest':RandomForestClassifier(n_estimators=150,class_weight='balanced',random_state=42,n_jobs=1),'gradient_boosting':GradientBoostingClassifier(random_state=42)}; r=[]
for n,m in ms.items(): m.fit(df.iloc[:s][FEATURES],df.iloc[:s].anomaly_label); r.append({'model':n,**metrics(df.iloc[s:].anomaly_label,m.predict(df.iloc[s:][FEATURES]))})
o=pd.DataFrame(r).sort_values('f1',ascending=False); o.to_csv(output_path('ex239_model_comparison.csv'),index=False); print(o)
