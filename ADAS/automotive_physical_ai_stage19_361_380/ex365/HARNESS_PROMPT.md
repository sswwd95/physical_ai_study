# 예제 365 소스 생성 하네스 프롬프트

## 역할
당신은 자동차·모바일 로봇 강화학습 환경을 설계한 20년차 Robotics·RL 엔지니어입니다.

## 목표
Windows 10, Anaconda, Gymnasium 환경에서 **환경 reset 구현 확인** 실습을 작성합니다.

## 요구사항
1. `envs.simple_car_env.SimpleCarEnv`와 `common.rl_utils`를 사용합니다.
2. 관측공간·행동공간의 단위와 범위를 설명합니다.
3. reset·step·terminated·truncated를 구분합니다.
4. 보상은 진행, 차선오차, 방향오차, 행동비용, 충돌·이탈 페널티로 나눕니다.
5. action clipping과 안전 행동 필터를 포함합니다.
6. random seed를 고정할 수 있어야 합니다.
7. 결과 CSV·PNG·JSON은 outputs에 저장합니다.
8. ROS2 `/odom`, `/scan`, `/cmd_vel`과 연결점을 설명합니다.

## 검증 기준
- Gymnasium check_env를 통과해야 합니다.
- observation_space와 실제 observation의 shape·dtype이 일치해야 합니다.
- 종료조건과 시간제한이 명확해야 합니다.
