# 설계 참고

- MuJoCo Python API: `MjModel.from_xml_path`, `MjData`, `mj_step`, 이름-ID 변환 API
- TurtleBot3 Burger 핵심 구조: 차동구동 좌우 바퀴, 베이스 링크, IMU·오도메트리 연계
- ROS2 연결 대상: `/cmd_vel`, `/odom`, `/imu`, `/joint_states`

교육용 XML은 오프라인에서 모든 예제를 실행하기 위한 최소 모델입니다.
ROBOTIS 공식 모델이 설치된 환경에서는 환경변수 경로를 우선 사용합니다.
공식 모델의 액추에이터 순서가 다르면 예제 111 이후 코드를 모델 이름 기준으로 조정해야 합니다.
