# 예제 222 — 파생 특징 Jerk·조향속도 분석

```bat
cd /d C:\work\automotive_physical_ai_stage12_221_240
conda activate auto_physical_ai
python ex222\main.py
```

ROS2 `/odom`, `/imu`, `/scan` 입력에서 특징을 계산하고 이상 확률을 `/diagnostics`로 연결할 수 있습니다. 시간순 분할과 이벤트 단위 평가가 중요합니다.

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `from common.feature_utils import load_data,output_path` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `df=load_data(); s=df.groupby('anomaly_label')[['jerk_mps3','steering_rate_dps']].agg(['mean','std','max','min']); p=output_path('ex222_derived_feature_summary.csv'); s.to_csv(p); print(s)` | 결과를 outputs 폴더에 저장합니다. |
