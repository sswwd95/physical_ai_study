# 예제 234 — 특징 중요도 분석

```bat
cd /d C:\work\automotive_physical_ai_stage12_221_240
conda activate auto_physical_ai
python ex234\main.py
```

ROS2 `/odom`, `/imu`, `/scan` 입력에서 특징을 계산하고 이상 확률을 `/diagnostics`로 연결할 수 있습니다. 시간순 분할과 이벤트 단위 평가가 중요합니다.

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import pandas as pd` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `from sklearn.ensemble import RandomForestClassifier` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 3 | `from common.feature_utils import load_data,FEATURES,output_path` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 4 | `df=load_data(); m=RandomForestClassifier(n_estimators=150,class_weight='balanced',random_state=42,n_jobs=1).fit(df[FEATURES],df.anomaly_label); o=pd.DataFrame({'feature':FEATURES,'importance':m.feature_importances_}).sort_values('importance',ascending=False); o.to_csv(output_path('ex234_feature_importance.csv'),index=False); print(o)` | 훈련 데이터로 모델을 학습합니다. |
