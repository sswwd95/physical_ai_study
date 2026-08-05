# 예제 230 — 최적 규칙 임계값 선택

```bat
cd /d C:\work\automotive_physical_ai_stage12_221_240
conda activate auto_physical_ai
python ex230\main.py
```

ROS2 `/odom`, `/imu`, `/scan` 입력에서 특징을 계산하고 이상 확률을 `/diagnostics`로 연결할 수 있습니다. 시간순 분할과 이벤트 단위 평가가 중요합니다.

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `from common.feature_utils import load_data,metrics,save_json` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `df=load_data(); best=None` | 특징, 데이터 분할, 모델 또는 평가 지표를 계산합니다. |
| 3 | `for a in [1.2,1.4,1.6,1.8,2.0,2.2]:` | 현재 특징 엔지니어링 또는 모델 평가 절차를 실행합니다. |
| 4 | ` for s in [10,12,14,16,18]:` | 현재 특징 엔지니어링 또는 모델 평가 절차를 실행합니다. |
| 5 | `  p=(df.accel_mps2.abs()>a)¦(df.steering_deg.abs()>s)¦(df.ttc_s<2)¦(df.motor_current_a>7); c={'accel_th':a,'steer_th':s,**metrics(df.anomaly_label,p)}; best=c if best is None or c['f1']>best['f1'] else best` | 특징, 데이터 분할, 모델 또는 평가 지표를 계산합니다. |
| 6 | `print(best); print(save_json(best,'ex230_best_rule_threshold.json'))` | 핵심 결과를 출력합니다. |
