# 예제 239 — 모델 성능 비교 리포트

```bat
cd /d C:\work\automotive_physical_ai_stage12_221_240
conda activate auto_physical_ai
python ex239\main.py
```

ROS2 `/odom`, `/imu`, `/scan` 입력에서 특징을 계산하고 이상 확률을 `/diagnostics`로 연결할 수 있습니다. 시간순 분할과 이벤트 단위 평가가 중요합니다.

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import pandas as pd` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `from sklearn.linear_model import LogisticRegression` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 3 | `from sklearn.pipeline import make_pipeline` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 4 | `from sklearn.preprocessing import StandardScaler` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 5 | `from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 6 | `from common.feature_utils import load_data,FEATURES,metrics,output_path` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 7 | `df=load_data(); s=int(len(df)*.7); ms={'logistic':make_pipeline(StandardScaler(),LogisticRegression(class_weight='balanced',max_iter=1000,random_state=42)),'random_forest':RandomForestClassifier(n_estimators=150,class_weight='balanced',random_state=42,n_jobs=1),'gradient_boosting':GradientBoostingClassifier(random_state=42)}; r=[]` | 특징, 데이터 분할, 모델 또는 평가 지표를 계산합니다. |
| 8 | `for n,m in ms.items(): m.fit(df.iloc[:s][FEATURES],df.iloc[:s].anomaly_label); r.append({'model':n,**metrics(df.iloc[s:].anomaly_label,m.predict(df.iloc[s:][FEATURES]))})` | 훈련 데이터로 모델을 학습합니다. |
| 9 | `o=pd.DataFrame(r).sort_values('f1',ascending=False); o.to_csv(output_path('ex239_model_comparison.csv'),index=False); print(o)` | 결과를 outputs 폴더에 저장합니다. |
