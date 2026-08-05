# 예제 236 — Precision-Recall 곡선과 AP

```bat
cd /d C:\work\automotive_physical_ai_stage12_221_240
conda activate auto_physical_ai
python ex236\main.py
```

ROS2 `/odom`, `/imu`, `/scan` 입력에서 특징을 계산하고 이상 확률을 `/diagnostics`로 연결할 수 있습니다. 시간순 분할과 이벤트 단위 평가가 중요합니다.

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import matplotlib` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `matplotlib.use('Agg')` | 현재 특징 엔지니어링 또는 모델 평가 절차를 실행합니다. |
| 3 | `import matplotlib.pyplot as plt` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 4 | `from sklearn.ensemble import RandomForestClassifier` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 5 | `from sklearn.metrics import precision_recall_curve,average_precision_score` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 6 | `from common.feature_utils import load_data,FEATURES,output_path` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 7 | `df=load_data(); s=int(len(df)*.7); m=RandomForestClassifier(n_estimators=150,class_weight='balanced',random_state=42,n_jobs=1).fit(df.iloc[:s][FEATURES],df.iloc[:s].anomaly_label); p=m.predict_proba(df.iloc[s:][FEATURES])[:,1]; pr,rc,_=precision_recall_curve(df.iloc[s:].anomaly_label,p); ap=average_precision_score(df.iloc[s:].anomaly_label,p); fig,ax=plt.subplots(); ax.plot(rc,pr,label=f'AP={ap:.3f}'); ax.legend(); ax.grid(True); q=output_path('ex236_pr_curve.png'); fig.savefig(q); plt.close(fig); print(ap,q)` | 훈련 데이터로 모델을 학습합니다. |
