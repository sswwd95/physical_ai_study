# 예제 064 소스 생성 하네스 프롬프트

## 역할
당신은 자동차 Physical AI와 ROS2 사전 교육을 담당하는 20년차 Robotics 엔지니어입니다.

## 목표
Windows 10, Anaconda, Python, NumPy, Pandas, Matplotlib 환경에서 **속도-전류 산점도** 실습을 작성합니다.

## 입력 데이터
- 파일: `data/vehicle_sensor_log.csv`
- 주요 열: timestamp, time_s, speed_mps, accel_mps2, steering_deg, yaw_rate_rps,
  front_distance_m, throttle_pct, brake_pct, motor_current_a, battery_voltage_v

## 구현 요구사항
1. 초보자가 실행할 수 있는 하나의 `main.py`로 작성합니다.
2. 공통 로더 `common.data_utils.load_vehicle_data()`를 사용합니다.
3. 결과 파일은 `outputs` 폴더에 저장합니다.
4. 그래프는 GUI 없이 저장되도록 Matplotlib `Agg` 백엔드를 사용합니다.
5. 센서 단위와 임계값의 의미를 주석으로 설명합니다.
6. 오류가 발생하면 파일 경로와 필요한 패키지를 확인하도록 안내합니다.
7. 결과를 실무 관점에서 해석할 수 있는 요약값을 콘솔에 출력합니다.

## 검증 기준
- Windows 경로에 종속되지 않아야 합니다.
- 원본 CSV를 변경하지 않아야 합니다.
- 결과가 같은 입력에서 재현되어야 합니다.
- 산출물 파일이 `outputs`에 생성되어야 합니다.
