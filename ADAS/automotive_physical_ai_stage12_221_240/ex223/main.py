from common.feature_utils import load_data,add_window_features,output_path
df=add_window_features(load_data(),10); c=['time_s','accel_mps2_mean_w','steering_deg_mean_w','motor_current_a_mean_w','anomaly_label']; df[c].to_csv(output_path('ex223_window_mean_features.csv'),index=False); print(df[c].head())
