# 예제 231 — Logistic Regression 기준 모델

```bat
cd /d C:\work\automotive_physical_ai_stage12_221_240
conda activate auto_physical_ai
python ex231\main.py
```

ROS2 `/odom`, `/imu`, `/scan` 입력에서 특징을 계산하고 이상 확률을 `/diagnostics`로 연결할 수 있습니다. 시간순 분할과 이벤트 단위 평가가 중요합니다.

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `from sklearn.linear_model import LogisticRegression` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `from sklearn.pipeline import make_pipeline` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 3 | `from sklearn.preprocessing import StandardScaler` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 4 | `from common.feature_utils import load_data,FEATURES,metrics,save_json` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 5 | `df=load_data(); s=int(len(df)*.7); m=make_pipeline(StandardScaler(),LogisticRegression(class_weight='balanced',max_iter=1000,random_state=42)); m.fit(df.iloc[:s][FEATURES],df.iloc[:s].anomaly_label); r=metrics(df.iloc[s:].anomaly_label,m.predict(df.iloc[s:][FEATURES])); print(r); print(save_json(r,'ex231_logistic_metrics.json'))` | 훈련 데이터로 모델을 학습합니다. |
