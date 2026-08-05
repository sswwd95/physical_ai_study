# 설계 기준

모델링 대상:
- 슬립률 평균과 표준편차
- 노면별 슬립률 차이
- 오도메트리 거리·회전각 오차
- 슬립률과 센서 특징의 회귀 관계
- 위험 여부의 로지스틱 회귀
- 노면별 계층 모델
- 이상값에 강한 Student-t 모델

ROS2 연결 대상:
- `sensor_msgs/JointState`
- `sensor_msgs/Imu`
- `nav_msgs/Odometry`
- `diagnostic_msgs/DiagnosticArray`

실차에서는 타이어 마모, 하중, 바닥 재질, 속도, 가속도, 온도,
센서 지연과 시간 동기화를 함께 모델링해야 합니다.
