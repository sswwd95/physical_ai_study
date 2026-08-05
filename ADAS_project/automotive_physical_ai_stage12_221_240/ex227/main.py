from sklearn.preprocessing import StandardScaler
import pandas as pd
from common.feature_utils import load_data,FEATURES,output_path
df=load_data(); x=StandardScaler().fit_transform(df[FEATURES]); o=pd.DataFrame(x,columns=[c+'_z' for c in FEATURES]); o['anomaly_label']=df['anomaly_label']; o.to_csv(output_path('ex227_scaled_features.csv'),index=False); print(o.describe().loc[['mean','std']])
