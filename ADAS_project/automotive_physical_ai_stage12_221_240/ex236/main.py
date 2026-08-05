import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_recall_curve,average_precision_score
from common.feature_utils import load_data,FEATURES,output_path
df=load_data(); s=int(len(df)*.7); m=RandomForestClassifier(n_estimators=150,class_weight='balanced',random_state=42,n_jobs=1).fit(df.iloc[:s][FEATURES],df.iloc[:s].anomaly_label); p=m.predict_proba(df.iloc[s:][FEATURES])[:,1]; pr,rc,_=precision_recall_curve(df.iloc[s:].anomaly_label,p); ap=average_precision_score(df.iloc[s:].anomaly_label,p); fig,ax=plt.subplots(); ax.plot(rc,pr,label=f'AP={ap:.3f}'); ax.legend(); ax.grid(True); q=output_path('ex236_pr_curve.png'); fig.savefig(q); plt.close(fig); print(ap,q)
