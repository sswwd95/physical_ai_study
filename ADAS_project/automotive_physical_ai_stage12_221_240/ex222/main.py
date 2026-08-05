from common.feature_utils import load_data,output_path
df=load_data(); s=df.groupby('anomaly_label')[['jerk_mps3','steering_rate_dps']].agg(['mean','std','max','min']); p=output_path('ex222_derived_feature_summary.csv'); s.to_csv(p); print(s)
