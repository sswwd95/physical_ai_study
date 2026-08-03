# 실습 058 생성 하네스 프롬프트
역할: 공정 변화 탐지 성능 분석가.
목표: 합성 작은 평균 이동 구간에서 EWMA와 CUSUM의 첫 경보 시각과 탐지 지연을 계산한다.
필수 조건:
- 이동 시작·종료 시각을 명시한다.
- detected, first_alert_time, detection_delay_sec를 저장한다.
- 탐지하지 못한 경우 None으로 처리한다.
