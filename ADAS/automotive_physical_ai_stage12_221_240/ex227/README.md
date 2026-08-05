# 예제 227 — 표준화 전후 특징 비교

```bat
cd /d C:\work\automotive_physical_ai_stage12_221_240
conda activate auto_physical_ai
python ex227\main.py
```

ROS2 `/odom`, `/imu`, `/scan` 입력에서 특징을 계산하고 이상 확률을 `/diagnostics`로 연결할 수 있습니다. 시간순 분할과 이벤트 단위 평가가 중요합니다.

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `from sklearn.preprocessing import StandardScaler` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `import pandas as pd` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 3 | `from common.feature_utils import load_data,FEATURES,output_path` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 4 | `df=load_data(); x=StandardScaler().fit_transform(df[FEATURES]); o=pd.DataFrame(x,columns=[c+'_z' for c in FEATURES]); o['anomaly_label']=df['anomaly_label']; o.to_csv(output_path('ex227_scaled_features.csv'),index=False); print(o.describe().loc[['mean','std']])` | 결과를 outputs 폴더에 저장합니다. |
