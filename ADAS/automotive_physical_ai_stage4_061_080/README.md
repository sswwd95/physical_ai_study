# 자동차 Physical AI 하네스 엔지니어링
## 4단계 | 061~080제 | 센서 시각화·상관관계·주행 구간 분석

### 학습 환경
- Windows 10
- Anaconda
- Python 3.11
- NumPy / Pandas / Matplotlib
- MuJoCo 3.6.0
- PyMC / ArviZ
- ROBOTIS `robotis_mujoco_menagerie/robotis_tb3` Burger 연계 준비

### 예제 목록
- 061 속도 시계열
- 062 다중 센서 시계열
- 063 가속도 분포
- 064 속도-전류 산점도
- 065 상관계수 행렬
- 066 상관관계 히트맵
- 067 이동평균 추세
- 068 정차 구간
- 069 급가속 구간
- 070 급감속 구간
- 071 회전 구간
- 072 위험 접근 거리
- 073 TTC
- 074 좌우 바퀴 속도 차이
- 075 조향각-요레이트
- 076 배터리 전압 강하
- 077 주행 상태 분류
- 078 상태 타임라인
- 079 구간별 통계
- 080 통합 대시보드

### 설치
```bat
conda env create -f environment.yml
conda activate auto_physical_ai
```

### 개별 실행
```bat
python ex061\main.py
```

### 전체 실행
```bat
00_run_all_examples.bat
```

### ROS2 연결 포인트
이 단계의 분석 결과는 다음 단계에서 ROS2 토픽 형태의 센서 메시지와 연결할 수 있습니다.
- 속도: `/odom`
- IMU: `/imu`
- 거리 센서: `/scan` 또는 사용자 정의 거리 토픽
- 모터 상태: 사용자 정의 진단 토픽
