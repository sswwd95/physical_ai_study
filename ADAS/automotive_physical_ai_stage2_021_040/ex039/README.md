# 실습 039 | 센서 데이터 시각화

## 핵심 주제
속도와 전방 거리 그래프를 각각 저장한다.

## 실행 방법
프로젝트 루트에서 Anaconda Prompt를 열고 다음을 실행합니다.

```bat
conda activate auto_physical_ai
cd /d C:\work\automotive_physical_ai_stage2_021_040
python ex039\main.py
```

## 기대 결과
코드가 오류 없이 실행되고, 계산 결과 또는 생성 파일 경로가 출력되어야 합니다.

## 실무 연결
이 예제는 ROS2 토픽 또는 MuJoCo 센서 배열을 받기 전에 Python 자료구조와 데이터 처리 흐름을 연습하는 단계입니다. 실제 차량 프로젝트에서는 단위, 시간축, 임계값, 결측값을 항상 함께 확인해야 합니다.

## 라인별 해설
- **01행** `import matplotlib.pyplot as plt` — 필요한 라이브러리 또는 공통 함수를 불러옵니다.
- **02행** `from common.load_data import load_vehicle_log` — 필요한 라이브러리 또는 공통 함수를 불러옵니다.
- **03행** `from common.paths import OUTPUT_DIR` — 필요한 라이브러리 또는 공통 함수를 불러옵니다.
- **05행** `df = load_vehicle_log()` — 센서 값, 조건식 또는 계산 결과를 변수에 저장합니다.
- **06행** `plt.figure(figsize=(9, 4))` — 센서 값, 조건식 또는 계산 결과를 변수에 저장합니다.
- **07행** `plt.plot(df["time_s"], df["speed_mps"])` — 그래프의 데이터, 축, 제목 또는 저장 옵션을 설정합니다.
- **08행** `plt.xlabel("Time (s)")` — 그래프의 데이터, 축, 제목 또는 저장 옵션을 설정합니다.
- **09행** `plt.ylabel("Speed (m/s)")` — 그래프의 데이터, 축, 제목 또는 저장 옵션을 설정합니다.
- **10행** `plt.title("Vehicle Speed")` — 그래프의 데이터, 축, 제목 또는 저장 옵션을 설정합니다.
- **11행** `plt.tight_layout()` — 그래프의 데이터, 축, 제목 또는 저장 옵션을 설정합니다.
- **12행** `path1 = OUTPUT_DIR / "ex039_speed.png"` — 센서 값, 조건식 또는 계산 결과를 변수에 저장합니다.
- **13행** `plt.savefig(path1, dpi=140)` — 센서 값, 조건식 또는 계산 결과를 변수에 저장합니다.
- **14행** `plt.close()` — 그래프의 데이터, 축, 제목 또는 저장 옵션을 설정합니다.
- **16행** `plt.figure(figsize=(9, 4))` — 센서 값, 조건식 또는 계산 결과를 변수에 저장합니다.
- **17행** `plt.plot(df["time_s"], df["front_distance_m"])` — 그래프의 데이터, 축, 제목 또는 저장 옵션을 설정합니다.
- **18행** `plt.xlabel("Time (s)")` — 그래프의 데이터, 축, 제목 또는 저장 옵션을 설정합니다.
- **19행** `plt.ylabel("Front distance (m)")` — 그래프의 데이터, 축, 제목 또는 저장 옵션을 설정합니다.
- **20행** `plt.title("Front Distance")` — 그래프의 데이터, 축, 제목 또는 저장 옵션을 설정합니다.
- **21행** `plt.tight_layout()` — 그래프의 데이터, 축, 제목 또는 저장 옵션을 설정합니다.
- **22행** `path2 = OUTPUT_DIR / "ex039_distance.png"` — 센서 값, 조건식 또는 계산 결과를 변수에 저장합니다.
- **23행** `plt.savefig(path2, dpi=140)` — 센서 값, 조건식 또는 계산 결과를 변수에 저장합니다.
- **24행** `plt.close()` — 그래프의 데이터, 축, 제목 또는 저장 옵션을 설정합니다.
- **25행** `print(path1)` — 계산 결과나 상태를 화면에 출력해 확인합니다.
- **26행** `print(path2)` — 계산 결과나 상태를 화면에 출력해 확인합니다.

## 확인 문제
1. 입력 단위가 바뀌면 어느 부분을 수정해야 합니까?
2. 임계값을 너무 낮게 설정하면 어떤 오경보가 발생할 수 있습니까?
3. 이 결과를 ROS2 메시지로 전달하려면 어떤 필드가 필요합니까?
