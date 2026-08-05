# 예제 223 — 윈도우 평균 특징 생성

```bat
cd /d C:\work\automotive_physical_ai_stage12_221_240
conda activate auto_physical_ai
python ex223\main.py
```

ROS2 `/odom`, `/imu`, `/scan` 입력에서 특징을 계산하고 이상 확률을 `/diagnostics`로 연결할 수 있습니다. 시간순 분할과 이벤트 단위 평가가 중요합니다.

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `from common.feature_utils import load_data,add_window_features,output_path` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `df=add_window_features(load_data(),10); c=['time_s','accel_mps2_mean_w','steering_deg_mean_w','motor_current_a_mean_w','anomaly_label']; df[c].to_csv(output_path('ex223_window_mean_features.csv'),index=False); print(df[c].head())` | 결과를 outputs 폴더에 저장합니다. |
