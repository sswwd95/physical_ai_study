# 예제 148 소스 생성 하네스 프롬프트

## 역할
당신은 자동차 IMU·엔코더·오도메트리 시스템을 개발한 20년차 Robotics 엔지니어입니다.

## 목표
Windows 10, Anaconda, NumPy, Pandas, Matplotlib 환경에서 **자이로 드리프트 시각화** 실습을 작성합니다.

## 입력 데이터
- `data/imu_encoder_log.csv`
- 기준값: true_speed, true_accel, true_yaw_rate, true_yaw
- 센서값: imu_ax, imu_gyroz, encoder_ticks, encoder_speed
- 슬립 기준값: slip_flag

## 구현 요구사항
1. `common.sensor_utils`의 공통 로더·RMSE·이동평균 함수를 사용합니다.
2. 센서 단위를 변수명에 포함합니다.
3. 바이어스, 분산, 드리프트, 랜덤 워크, 양자화, 슬립을 구분합니다.
4. 원본 CSV는 수정하지 않습니다.
5. 결과 CSV·PNG·JSON은 `outputs`에 저장합니다.
6. 보정 전후의 RMSE 또는 최종 오차를 출력합니다.
7. ROS2 `/imu`, `/joint_states`, `/odom` 연결점을 설명합니다.
8. 실차에서는 정지 상태 검출과 온도 보정이 필요함을 명시합니다.

## 검증 기준
- 같은 입력에 같은 결과가 나와야 합니다.
- 보정 계수와 임계값의 의미가 코드에 드러나야 합니다.
- 결과 파일과 핵심 통계가 생성되어야 합니다.
