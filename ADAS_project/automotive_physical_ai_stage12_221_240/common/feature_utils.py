from pathlib import Path
import json, numpy as np, pandas as pd
ROOT=Path(__file__).resolve().parents[1]; DATA_PATH=ROOT/'data'/'driving_feature_log.csv'; OUTPUTS=ROOT/'outputs'
FEATURES=['speed_mps','accel_mps2','jerk_mps3','steering_deg','steering_rate_dps','yaw_rate_rps','front_distance_m','ttc_s','motor_current_a','battery_voltage_v']
def load_data(): return pd.read_csv(DATA_PATH)
def output_path(name): OUTPUTS.mkdir(parents=True,exist_ok=True); return OUTPUTS/name
def add_window_features(df,window=10):
 out=df.copy()
 for c in ['accel_mps2','jerk_mps3','steering_deg','motor_current_a','ttc_s']:
  out[f'{c}_mean_w']=out[c].rolling(window,min_periods=1).mean(); out[f'{c}_std_w']=out[c].rolling(window,min_periods=1).std().fillna(0); out[f'{c}_maxabs_w']=out[c].abs().rolling(window,min_periods=1).max()
 return out
def metrics(y,p):
 y=np.asarray(y).astype(int); p=np.asarray(p).astype(int); tp=int(np.sum((y==1)&(p==1))); fp=int(np.sum((y==0)&(p==1))); tn=int(np.sum((y==0)&(p==0))); fn=int(np.sum((y==1)&(p==0))); pr=tp/max(1,tp+fp); rc=tp/max(1,tp+fn); f1=2*pr*rc/max(1e-12,pr+rc); return {'tp':tp,'fp':fp,'tn':tn,'fn':fn,'precision':pr,'recall':rc,'f1':f1}
def save_json(d,n): p=output_path(n); p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8'); return p
