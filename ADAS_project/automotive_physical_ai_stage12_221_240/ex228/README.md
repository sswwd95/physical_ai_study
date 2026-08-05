# 예제 228 — 클래스 불균형 가중치 계산

```bat
cd /d C:\work\automotive_physical_ai_stage12_221_240
conda activate auto_physical_ai
python ex228\main.py
```

ROS2 `/odom`, `/imu`, `/scan` 입력에서 특징을 계산하고 이상 확률을 `/diagnostics`로 연결할 수 있습니다. 시간순 분할과 이벤트 단위 평가가 중요합니다.

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import numpy as np` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `from sklearn.utils.class_weight import compute_class_weight` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 3 | `from common.feature_utils import load_data` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 4 | `df=load_data(); c=np.array([0,1]); w=compute_class_weight('balanced',classes=c,y=df['anomaly_label']); print(dict(zip(c,w)))` | 핵심 결과를 출력합니다. |
