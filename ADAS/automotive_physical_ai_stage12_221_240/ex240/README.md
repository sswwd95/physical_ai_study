# 예제 240 — 특징 엔지니어링·성능 개선 통합 파이프라인

```bat
cd /d C:\work\automotive_physical_ai_stage12_221_240
conda activate auto_physical_ai
python ex240\main.py
```

ROS2 `/odom`, `/imu`, `/scan` 입력에서 특징을 계산하고 이상 확률을 `/diagnostics`로 연결할 수 있습니다. 시간순 분할과 이벤트 단위 평가가 중요합니다.

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import json,pandas as pd` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `from sklearn.ensemble import RandomForestClassifier` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 3 | `from sklearn.metrics import roc_auc_score,average_precision_score` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 4 | `from common.feature_utils import load_data,add_window_features,metrics,output_path` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 5 | `df=add_window_features(load_data(),15); b=['speed_mps','accel_mps2','jerk_mps3','steering_deg','steering_rate_dps','yaw_rate_rps','front_distance_m','ttc_s','motor_current_a','battery_voltage_v']; e=[c for c in df if c.endswith('_mean_w') or c.endswith('_std_w') or c.endswith('_maxabs_w')]; f=b+e; s=int(len(df)*.7); m=RandomForestClassifier(n_estimators=250,class_weight='balanced',random_state=42,n_jobs=1,min_samples_leaf=2).fit(df.iloc[:s][f],df.iloc[:s].anomaly_label); p=m.predict_proba(df.iloc[s:][f])[:,1]; th=.35; pred=p>=th; o=df.iloc[s:][['time_s','event_type','anomaly_label']].copy(); o['anomaly_probability']=p; o['predicted_anomaly']=pred.astype(int); cp=output_path('ex240_integrated_predictions.csv'); o.to_csv(cp,index=False); sm={'features_used':len(f),'threshold':th,'roc_auc':float(roc_auc_score(df.iloc[s:].anomaly_label,p)),'average_precision':float(average_precision_score(df.iloc[s:].anomaly_label,p)),**metrics(df.iloc[s:].anomaly_label,pred)}; jp=output_path('ex240_integrated_summary.json'); jp.write_text(json.dumps(sm,indent=2)); ip=output_path('ex240_feature_importance.csv'); pd.DataFrame({'feature':f,'importance':m.feature_importances_}).sort_values('importance',ascending=False).to_csv(ip,index=False); print(sm)` | 훈련 데이터로 모델을 학습합니다. |
