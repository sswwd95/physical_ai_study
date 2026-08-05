# 예제 226 — 훈련·검증 데이터 시간순 분할

```bat
cd /d C:\work\automotive_physical_ai_stage12_221_240
conda activate auto_physical_ai
python ex226\main.py
```

ROS2 `/odom`, `/imu`, `/scan` 입력에서 특징을 계산하고 이상 확률을 `/diagnostics`로 연결할 수 있습니다. 시간순 분할과 이벤트 단위 평가가 중요합니다.

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `from common.feature_utils import load_data,output_path` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `df=load_data(); s=int(len(df)*.7); df.iloc[:s].to_csv(output_path('ex226_train.csv'),index=False); df.iloc[s:].to_csv(output_path('ex226_test.csv'),index=False); print(s,len(df)-s)` | 결과를 outputs 폴더에 저장합니다. |
