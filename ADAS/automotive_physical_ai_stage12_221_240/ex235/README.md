# 예제 235 — ROC 곡선과 AUC

```bat
cd /d C:\work\automotive_physical_ai_stage12_221_240
conda activate auto_physical_ai
python ex235\main.py
```

ROS2 `/odom`, `/imu`, `/scan` 입력에서 특징을 계산하고 이상 확률을 `/diagnostics`로 연결할 수 있습니다. 시간순 분할과 이벤트 단위 평가가 중요합니다.

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import matplotlib` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `matplotlib.use('Agg')` | 현재 특징 엔지니어링 또는 모델 평가 절차를 실행합니다. |
| 3 | `import matplotlib.pyplot as plt` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 4 | `from sklearn.linear_model import LogisticRegression` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 5 | `from sklearn.pipeline import make_pipeline` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 6 | `from sklearn.preprocessing import StandardScaler` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 7 | `from sklearn.metrics import roc_curve,roc_auc_score` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 8 | `from common.feature_utils import load_data,FEATURES,output_path` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 9 | `df=load_data(); s=int(len(df)*.7); m=make_pipeline(StandardScaler(),LogisticRegression(class_weight='balanced',max_iter=1000,random_state=42)).fit(df.iloc[:s][FEATURES],df.iloc[:s].anomaly_label); pr=m.predict_proba(df.iloc[s:][FEATURES])[:,1]; f,t,_=roc_curve(df.iloc[s:].anomaly_label,pr); a=roc_auc_score(df.iloc[s:].anomaly_label,pr); fig,ax=plt.subplots(); ax.plot(f,t,label=f'AUC={a:.3f}'); ax.legend(); ax.grid(True); p=output_path('ex235_roc_curve.png'); fig.savefig(p); plt.close(fig); print(a,p)` | 훈련 데이터로 모델을 학습합니다. |
