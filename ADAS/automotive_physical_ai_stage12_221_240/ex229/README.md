# 예제 229 — 규칙 임계값 그리드 탐색

```bat
cd /d C:\work\automotive_physical_ai_stage12_221_240
conda activate auto_physical_ai
python ex229\main.py
```

ROS2 `/odom`, `/imu`, `/scan` 입력에서 특징을 계산하고 이상 확률을 `/diagnostics`로 연결할 수 있습니다. 시간순 분할과 이벤트 단위 평가가 중요합니다.

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import pandas as pd` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `from common.feature_utils import load_data,metrics,output_path` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 3 | `df=load_data(); r=[]` | 특징, 데이터 분할, 모델 또는 평가 지표를 계산합니다. |
| 4 | `for a in [1.4,1.8,2.2]:` | 현재 특징 엔지니어링 또는 모델 평가 절차를 실행합니다. |
| 5 | ` for s in [12,15,18]:` | 현재 특징 엔지니어링 또는 모델 평가 절차를 실행합니다. |
| 6 | `  p=(df.accel_mps2.abs()>a)¦(df.steering_deg.abs()>s)¦(df.ttc_s<2)¦(df.motor_current_a>7); r.append({'accel_th':a,'steer_th':s,**metrics(df.anomaly_label,p)})` | 특징, 데이터 분할, 모델 또는 평가 지표를 계산합니다. |
| 7 | `o=pd.DataFrame(r).sort_values('f1',ascending=False); o.to_csv(output_path('ex229_threshold_grid.csv'),index=False); print(o.head())` | 결과를 outputs 폴더에 저장합니다. |
