# 예제 238 — 시간순 교차검증

```bat
cd /d C:\work\automotive_physical_ai_stage12_221_240
conda activate auto_physical_ai
python ex238\main.py
```

ROS2 `/odom`, `/imu`, `/scan` 입력에서 특징을 계산하고 이상 확률을 `/diagnostics`로 연결할 수 있습니다. 시간순 분할과 이벤트 단위 평가가 중요합니다.

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import pandas as pd` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `from sklearn.model_selection import TimeSeriesSplit` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 3 | `from sklearn.ensemble import RandomForestClassifier` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 4 | `from common.feature_utils import load_data,FEATURES,metrics,output_path` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 5 | `df=load_data(); r=[]` | 특징, 데이터 분할, 모델 또는 평가 지표를 계산합니다. |
| 6 | `for i,(tr,te) in enumerate(TimeSeriesSplit(n_splits=5).split(df),1):` | 특징, 데이터 분할, 모델 또는 평가 지표를 계산합니다. |
| 7 | ` m=RandomForestClassifier(n_estimators=100,class_weight='balanced',random_state=42,n_jobs=1).fit(df.iloc[tr][FEATURES],df.iloc[tr].anomaly_label); r.append({'fold':i,**metrics(df.iloc[te].anomaly_label,m.predict(df.iloc[te][FEATURES]))})` | 훈련 데이터로 모델을 학습합니다. |
| 8 | `o=pd.DataFrame(r); o.to_csv(output_path('ex238_time_series_cv.csv'),index=False); print(o)` | 결과를 outputs 폴더에 저장합니다. |
