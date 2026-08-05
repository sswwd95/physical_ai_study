# 설계 기준

- TTC = distance / closing_speed
- braking_distance = speed² / (2 g μ)
- safe_distance = reaction_distance + braking_distance + margin

안전 제어 단계:
1. 정상 주행
2. 주의
3. 감속
4. 긴급정지
5. 회피 가능 시 제한된 yaw rate 명령

실차에서는 센서 지연, 오검출, 제동 응답, 타이어 상태,
노면 마찰, 차량 질량과 법규를 별도로 검증해야 합니다.
