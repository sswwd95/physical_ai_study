# 예제 225 — 특징 상관관계와 중복성 점검

```bat
cd /d C:\work\automotive_physical_ai_stage12_221_240
conda activate auto_physical_ai
python ex225\main.py
```

ROS2 `/odom`, `/imu`, `/scan` 입력에서 특징을 계산하고 이상 확률을 `/diagnostics`로 연결할 수 있습니다. 시간순 분할과 이벤트 단위 평가가 중요합니다.

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `from common.feature_utils import load_data,FEATURES,output_path` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `c=load_data()[FEATURES].corr(); c.to_csv(output_path('ex225_feature_correlation.csv')); print(c.round(3))` | 결과를 outputs 폴더에 저장합니다. |
