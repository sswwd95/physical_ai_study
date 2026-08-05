# 예제 088 — 센서 시작 시각 오프셋 보정

## 학습 목표
서로 다른 주기의 자동차 센서 데이터를 시간축에 맞추고 필요한 경우 융합하는 방법을 익힙니다.

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage5_081_100
conda activate auto_physical_ai
python ex088\main.py
```

## 실무 연결
ROS2의 `/imu`, `/odom`, `/scan`, GPS 토픽은 발행 주기와 지연이 서로 다릅니다. 이 예제는 rosbag 분석과 센서 융합 노드 설계 전에 필요한 오프라인 기초입니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `from common.sync_utils import load_stream, out` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `imu = load_stream("imu_50hz.csv")` | 지정한 센서 CSV를 DataFrame으로 읽습니다. |
| 3 | `offset = imu["timestamp_s"].min()` | 동기화, 보간, 융합 또는 통계 계산에 필요한 값을 만듭니다. |
| 4 | `imu["timestamp_aligned_s"] = imu["timestamp_s"] - offset` | 동기화, 보간, 융합 또는 통계 계산에 필요한 값을 만듭니다. |
| 5 | `path = out("ex088_imu_time_aligned.csv")` | 동기화, 보간, 융합 또는 통계 계산에 필요한 값을 만듭니다. |
| 6 | `imu.to_csv(path,index=False)` | 분석 결과를 outputs 폴더에 저장합니다. |
| 7 | `print("offset:", offset, "saved:", path)` | 핵심 결과를 콘솔에 출력합니다. |

## 확인 문제
1. 허용 오차가 너무 크면 어떤 잘못된 결합이 생기는가?
2. 선형 보간이 적합하지 않은 센서는 무엇인가?
3. 실차에서는 센서 시간과 PC 수신 시간 중 무엇을 기준으로 삼아야 하는가?
