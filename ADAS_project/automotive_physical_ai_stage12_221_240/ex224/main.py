from common.feature_utils import load_data,add_window_features,output_path
df=add_window_features(load_data(),20); c=['time_s','accel_mps2_std_w','jerk_mps3_std_w','steering_deg_std_w','anomaly_label']; df[c].to_csv(output_path('ex224_window_std_features.csv'),index=False); print(df[c].describe())
