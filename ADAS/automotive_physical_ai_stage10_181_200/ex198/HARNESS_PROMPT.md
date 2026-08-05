# 예제 198 소스 생성 하네스 프롬프트

## 역할
당신은 자동차·모바일 로봇 휠 슬립과 오도메트리 불확실성을 분석하는 20년차 Robotics 엔지니어입니다.

## 목표
Windows 10, Anaconda, PyMC, ArviZ 환경에서 **사후분포 R-hat·ESS 진단** 실습을 작성합니다.

## 입력 데이터
- `data/wheel_slip_odometry.csv`
- 노면: dry, wet, tile, gravel
- 슬립률, 명령 속도, 주행시간
- 실제·오도메트리 이동거리
- 실제·오도메트리 회전각
- IMU 변동, 좌우 휠 속도차, 모터 전류
- 위험 레이블

## 요구사항
1. `common.bayes_slip_utils`를 사용합니다.
2. draws=500, tune=500, chains=2, cores=1, random_seed=42를 적용합니다.
3. 사전분포를 선택한 이유를 설명합니다.
4. 사후평균·95% 신용구간·R-hat·ESS 또는 기준 초과 확률을 출력합니다.
5. CSV·PNG·JSON은 `outputs`에 저장합니다.
6. 실차 적용 시 노면, 타이어, 하중, 마찰, 시간 지연을 추가 고려합니다.
7. ROS2 `/odom`, `/imu`, `/joint_states`, 진단 토픽과 연결점을 설명합니다.

## 검증 기준
- 원본 CSV를 변경하지 않습니다.
- 같은 random seed에서 결과가 재현되어야 합니다.
- 임계값과 위험 판정 규칙이 코드에 명확해야 합니다.
