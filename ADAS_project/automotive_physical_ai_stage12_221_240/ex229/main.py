import pandas as pd
from common.feature_utils import load_data,metrics,output_path
df=load_data(); r=[]
for a in [1.4,1.8,2.2]:
 for s in [12,15,18]:
  p=(df.accel_mps2.abs()>a)|(df.steering_deg.abs()>s)|(df.ttc_s<2)|(df.motor_current_a>7); r.append({'accel_th':a,'steer_th':s,**metrics(df.anomaly_label,p)})
o=pd.DataFrame(r).sort_values('f1',ascending=False); o.to_csv(output_path('ex229_threshold_grid.csv'),index=False); print(o.head())
