# 예제 097 — 칼만 필터와 원시값 비교 그래프

## 학습 목표
서로 다른 주기의 자동차 센서 데이터를 시간축에 맞추고 필요한 경우 융합하는 방법을 익힙니다.

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage5_081_100
conda activate auto_physical_ai
python ex097\main.py
```

## 실무 연결
ROS2의 `/imu`, `/odom`, `/scan`, GPS 토픽은 발행 주기와 지연이 서로 다릅니다. 이 예제는 rosbag 분석과 센서 융합 노드 설계 전에 필요한 오프라인 기초입니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import matplotlib` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `matplotlib.use("Agg")` | 현재 분석 절차를 실행합니다. |
| 3 | `import matplotlib.pyplot as plt` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 4 | `from common.sync_utils import load_stream, out` | 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 5 | `df=load_stream("wheel_20hz.csv")` | 지정한 센서 CSV를 DataFrame으로 읽습니다. |
| 6 | `df["measurement"]=(df["wheel_left_mps"]+df["wheel_right_mps"])/2` | 동기화, 보간, 융합 또는 통계 계산에 필요한 값을 만듭니다. |
| 7 | `x=df["measurement"].iloc[0]; p=1.0; q=0.02; r=0.01; est=[]` | 동기화, 보간, 융합 또는 통계 계산에 필요한 값을 만듭니다. |
| 8 | `for z in df["measurement"]:` | 현재 분석 절차를 실행합니다. |
| 9 | `    p+=q; k=p/(p+r); x=x+k*(z-x); p=(1-k)*p; est.append(x)` | 동기화, 보간, 융합 또는 통계 계산에 필요한 값을 만듭니다. |
| 10 | `fig,ax=plt.subplots(figsize=(10,4))` | 동기화, 보간, 융합 또는 통계 계산에 필요한 값을 만듭니다. |
| 11 | `ax.plot(df["timestamp_s"],df["measurement"],alpha=.35,label="raw")` | 동기화, 보간, 융합 또는 통계 계산에 필요한 값을 만듭니다. |
| 12 | `ax.plot(df["timestamp_s"],est,label="kalman")` | 동기화, 보간, 융합 또는 통계 계산에 필요한 값을 만듭니다. |
| 13 | `ax.legend(); ax.grid(True); ax.set_xlabel("Time (s)"); ax.set_ylabel("Speed (m/s)")` | 현재 분석 절차를 실행합니다. |
| 14 | `path=out("ex097_kalman_comparison.png")` | 동기화, 보간, 융합 또는 통계 계산에 필요한 값을 만듭니다. |
| 15 | `fig.tight_layout(); fig.savefig(path,dpi=140); plt.close(fig)` | 분석 결과를 outputs 폴더에 저장합니다. |
| 16 | `print("saved:",path)` | 핵심 결과를 콘솔에 출력합니다. |

## 확인 문제
1. 허용 오차가 너무 크면 어떤 잘못된 결합이 생기는가?
2. 선형 보간이 적합하지 않은 센서는 무엇인가?
3. 실차에서는 센서 시간과 PC 수신 시간 중 무엇을 기준으로 삼아야 하는가?
