# 설계 기준

Pure Pursuit:
- 최근접점에서 lookahead 거리만큼 앞의 목표점을 선택
- 목표점 방향 오차로 곡률 계산
- yaw_rate = speed × curvature

Stanley:
- 경로 진행방향 오차
- 부호 있는 횡방향 오차
- 속도 소프트닝 항

실차 적용 전 조향각 제한, 조향속도 제한, 경로 종점 정지,
센서 지연, localization jump, fail-safe를 별도로 검증해야 합니다.
