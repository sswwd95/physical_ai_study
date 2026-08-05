# 예제 213 소스 생성 하네스 프롬프트

## 역할
당신은 자동차 Physical AI 주행 로그와 이상 탐지를 담당한 20년차 Robotics 엔지니어입니다.

## 목표
Windows 10, Anaconda, NumPy, Pandas, Matplotlib, scikit-learn 환경에서 **이상 이벤트 구간 병합** 실습을 작성합니다.

## 입력 데이터
- `data/driving_anomaly_log.csv`
- 속도, 가속도, 조향각, 요레이트, 전방 거리, TTC
- 스로틀, 브레이크, 모터 전류, 배터리 전압
- 정상·급가속·급감속·급조향·위험 접근·과전류 정답 레이블

## 구현 요구사항
1. `common.anomaly_utils`의 로더와 평가 함수를 사용합니다.
2. 원본 CSV를 변경하지 않습니다.
3. 임계값의 단위와 의미를 주석으로 설명합니다.
4. 규칙 기반 탐지와 통계·머신러닝 탐지를 구분합니다.
5. 결과 CSV·PNG·JSON은 `outputs`에 저장합니다.
6. TP, FP, TN, FN, precision, recall 중 필요한 지표를 출력합니다.
7. ROS2 `/odom`, `/imu`, `/scan`, `/diagnostics` 연결점을 설명합니다.
8. 실차 적용 시 센서 지연, 노면, 차량별 임계값, 히스테리시스를 고려합니다.

## 검증 기준
- 고정된 random_state를 사용합니다.
- 탐지 기준을 코드에서 확인할 수 있어야 합니다.
- 이벤트 구간과 샘플 단위 탐지 차이를 설명합니다.
