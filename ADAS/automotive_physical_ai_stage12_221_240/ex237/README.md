# 예제 237 — 확률 임계값 튜닝

```bat
cd /d C:\work\automotive_physical_ai_stage12_221_240
conda activate auto_physical_ai
python ex237\main.py
```

ROS2 `/odom`, `/imu`, `/scan` 입력에서 특징을 계산하고 이상 확률을 `/diagnostics`로 연결할 수 있습니다. 시간순 분할과 이벤트 단위 평가가 중요합니다.

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import pandas as pd` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `from sklearn.ensemble import RandomForestClassifier` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 3 | `from common.feature_utils import load_data,FEATURES,metrics,output_path` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 4 | `df=load_data(); s=int(len(df)*.7); m=RandomForestClassifier(n_estimators=150,class_weight='balanced',random_state=42,n_jobs=1).fit(df.iloc[:s][FEATURES],df.iloc[:s].anomaly_label); p=m.predict_proba(df.iloc[s:][FEATURES])[:,1]; o=pd.DataFrame([{'threshold':th,**metrics(df.iloc[s:].anomaly_label,p>=th)} for th in [.1,.2,.3,.4,.5,.6,.7,.8,.9]]); o.to_csv(output_path('ex237_probability_thresholds.csv'),index=False); print(o.sort_values('f1',ascending=False).head())` | 훈련 데이터로 모델을 학습합니다. |
