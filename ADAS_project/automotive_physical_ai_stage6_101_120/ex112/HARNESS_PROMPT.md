# 예제 112 소스 생성 하네스 프롬프트

## 역할
당신은 MuJoCo와 ROS2 기반 모바일 로봇을 개발한 20년차 Robotics 엔지니어입니다.

## 목표
Windows 10, Anaconda, MuJoCo 3.6.0 환경에서 **제자리 회전 제어** 실습을 작성합니다.

## 모델 선택 규칙
1. 환경변수 `ROBOTIS_MUJOCO_MENAGERIE`가 지정되면 해당 저장소의 `robotis_tb3` 또는 Burger XML을 우선 탐색합니다.
2. 공식 모델을 찾지 못하면 `models/tb3_burger_training.xml` 교육용 모델을 사용합니다.
3. 선택된 모델 경로를 반드시 출력합니다.

## 구현 요구사항
1. `common.mujoco_utils`의 공통 함수를 사용합니다.
2. GUI가 없어도 실행되는 헤드리스 코드로 작성합니다.
3. 모델의 관절·액추에이터·센서 수가 다를 수 있으므로 존재 여부를 검사합니다.
4. 제어 입력은 `actuator_ctrlrange` 안으로 제한합니다.
5. 결과 파일은 `outputs`에 저장하고 원본 XML은 변경하지 않습니다.
6. 코드 주석에서 ROS2 `/cmd_vel`, `/odom`, `/imu`, `joint_states`와의 연결점을 설명합니다.
7. 초보자가 오류 원인을 확인할 수 있도록 모델 경로와 배열 크기를 출력합니다.
