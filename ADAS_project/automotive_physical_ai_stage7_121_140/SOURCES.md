# 설계 참고

이 단계는 차동구동 로봇의 표준 평면 운동학을 기반으로 합니다.

- 선속도: `v = r(ωR + ωL)/2`
- 각속도: `ω = r(ωR - ωL)/L`
- 오도메트리 적분:
  - `x += v cos(yaw) dt`
  - `y += v sin(yaw) dt`
  - `yaw += ω dt`

ROS2 연결 대상:
- `geometry_msgs/Twist`
- `nav_msgs/Odometry`
- `sensor_msgs/JointState`

실제 TurtleBot3 Burger 파라미터를 사용할 때는 설치된 모델의 바퀴 반지름과 차축 간격을 확인해야 합니다.
