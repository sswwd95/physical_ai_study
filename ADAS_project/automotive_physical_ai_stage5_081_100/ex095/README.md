# 예제 095 — 상보 필터 속도 융합

## 학습 목표
서로 다른 주기의 자동차 센서 데이터를 시간축에 맞추고 필요한 경우 융합하는 방법을 익힙니다.

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage5_081_100
conda activate auto_physical_ai
python ex095\main.py
```

## 실무 연결
ROS2의 `/imu`, `/odom`, `/scan`, GPS 토픽은 발행 주기와 지연이 서로 다릅니다. 이 예제는 rosbag 분석과 센서 융합 노드 설계 전에 필요한 오프라인 기초입니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `from common.sync_utils import load_stream, nearest_merge, out` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `imu = load_stream("imu_50hz.csv")` | 지정한 센서 CSV를 DataFrame으로 읽습니다. |
| 3 | `wheel = load_stream("wheel_20hz.csv")` | 지정한 센서 CSV를 DataFrame으로 읽습니다. |
| 4 | `wheel["wheel_speed_mps"]=(wheel["wheel_left_mps"]+wheel["wheel_right_mps"])/2` | 동기화, 보간, 융합 또는 통계 계산에 필요한 값을 만듭니다. |
| 5 | `m = nearest_merge(imu, wheel, tolerance=0.03).dropna().copy()` | 가장 가까운 타임스탬프끼리 센서 데이터를 결합합니다. |
| 6 | `estimate = []` | 동기화, 보간, 융합 또는 통계 계산에 필요한 값을 만듭니다. |
| 7 | `v = float(m["wheel_speed_mps"].iloc[0])` | 동기화, 보간, 융합 또는 통계 계산에 필요한 값을 만듭니다. |
| 8 | `prev_t = float(m["timestamp_s"].iloc[0])` | 동기화, 보간, 융합 또는 통계 계산에 필요한 값을 만듭니다. |
| 9 | `for _, r in m.iterrows():` | 현재 분석 절차를 실행합니다. |
| 10 | `    dt = float(r["timestamp_s"]-prev_t)` | 동기화, 보간, 융합 또는 통계 계산에 필요한 값을 만듭니다. |
| 11 | `    predicted = v + float(r["imu_ax_mps2"])*dt` | 동기화, 보간, 융합 또는 통계 계산에 필요한 값을 만듭니다. |
| 12 | `    v = 0.9*predicted + 0.1*float(r["wheel_speed_mps"])` | 동기화, 보간, 융합 또는 통계 계산에 필요한 값을 만듭니다. |
| 13 | `    estimate.append(v)` | 현재 분석 절차를 실행합니다. |
| 14 | `    prev_t=float(r["timestamp_s"])` | 동기화, 보간, 융합 또는 통계 계산에 필요한 값을 만듭니다. |
| 15 | `m["complementary_speed_mps"]=estimate` | 동기화, 보간, 융합 또는 통계 계산에 필요한 값을 만듭니다. |
| 16 | `path=out("ex095_complementary_filter.csv")` | 동기화, 보간, 융합 또는 통계 계산에 필요한 값을 만듭니다. |
| 17 | `m.to_csv(path,index=False)` | 분석 결과를 outputs 폴더에 저장합니다. |
| 18 | `print(m[["timestamp_s","wheel_speed_mps","complementary_speed_mps"]].head())` | 핵심 결과를 콘솔에 출력합니다. |

## 확인 문제
1. 허용 오차가 너무 크면 어떤 잘못된 결합이 생기는가?
2. 선형 보간이 적합하지 않은 센서는 무엇인가?
3. 실차에서는 센서 시간과 PC 수신 시간 중 무엇을 기준으로 삼아야 하는가?
