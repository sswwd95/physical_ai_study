import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_curve,roc_auc_score
from common.feature_utils import load_data,FEATURES,output_path
df=load_data(); s=int(len(df)*.7); m=make_pipeline(StandardScaler(),LogisticRegression(class_weight='balanced',max_iter=1000,random_state=42)).fit(df.iloc[:s][FEATURES],df.iloc[:s].anomaly_label); pr=m.predict_proba(df.iloc[s:][FEATURES])[:,1]; f,t,_=roc_curve(df.iloc[s:].anomaly_label,pr); a=roc_auc_score(df.iloc[s:].anomaly_label,pr); fig,ax=plt.subplots(); ax.plot(f,t,label=f'AUC={a:.3f}'); ax.legend(); ax.grid(True); p=output_path('ex235_roc_curve.png'); fig.savefig(p); plt.close(fig); print(a,p)
