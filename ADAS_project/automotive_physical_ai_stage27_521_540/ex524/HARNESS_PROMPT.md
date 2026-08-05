# 예제 524 하네스 프롬프트
공식 ROBOTIS `robotis_mujoco_menagerie/robotis_tb3/turtlebot3_burger.xml`을 include하여 **LDW 차선 이탈 경고** ADAS Viewer 예제를 작성한다. 원본 모델과 assets는 수정·재배포하지 않는다. wheel_left/wheel_right actuator 제어범위는 -6.67~6.67로 제한한다. 경고와 자동개입을 분리하고 교육용 임계값임을 명시한다.
