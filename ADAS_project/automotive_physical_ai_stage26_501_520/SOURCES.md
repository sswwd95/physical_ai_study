# 공식 출처

- ROBOTIS-GIT/robotis_mujoco_menagerie
- robotis_tb3/scene_turtlebot3_burger.xml
- robotis_tb3/turtlebot3_burger.xml
- robotis_tb3/LICENSE

확인된 공식 모델 구조:
- scene은 turtlebot3_burger.xml을 include
- body: base, wheel_left, wheel_right
- free joint: base_joint
- wheel joints: wheel_left, wheel_right
- wheel actuators: wheel_left, wheel_right
- actuator ctrlrange: -6.67 ~ 6.67
- mesh directory: assets/

공식 모델과 assets는 각 모델 디렉터리의 LICENSE 조건을 따릅니다.
