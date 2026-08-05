# 예제 221 — 기본 특징과 레이블 확인

```bat
cd /d C:\work\automotive_physical_ai_stage12_221_240
conda activate auto_physical_ai
python ex221\main.py
```

ROS2 `/odom`, `/imu`, `/scan` 입력에서 특징을 계산하고 이상 확률을 `/diagnostics`로 연결할 수 있습니다. 시간순 분할과 이벤트 단위 평가가 중요합니다.

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `from common.feature_utils import load_data` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `df=load_data(); print(df.head()); print(df['anomaly_label'].value_counts()); print(df['anomaly_label'].mean())` | 핵심 결과를 출력합니다. |
