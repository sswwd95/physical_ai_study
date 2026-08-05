from common.feature_utils import load_data,metrics,save_json
df=load_data(); best=None
for a in [1.2,1.4,1.6,1.8,2.0,2.2]:
 for s in [10,12,14,16,18]:
  p=(df.accel_mps2.abs()>a)|(df.steering_deg.abs()>s)|(df.ttc_s<2)|(df.motor_current_a>7); c={'accel_th':a,'steer_th':s,**metrics(df.anomaly_label,p)}; best=c if best is None or c['f1']>best['f1'] else best
print(best); print(save_json(best,'ex230_best_rule_threshold.json'))
