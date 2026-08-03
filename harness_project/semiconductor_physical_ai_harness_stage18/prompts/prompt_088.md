# 실습 088 생성 하네스 프롬프트
역할: 불량 경보 임계값 최적화 엔지니어.
목표: 0.10~0.90 임계값에서 precision, recall, F1, FN, FP를 비교한다.
필수 조건:
- false negative 비용 5, false positive 비용 1을 사용한다.
- weighted_cost가 가장 낮은 임계값을 선택한다.
- 동률이면 F1이 높은 값을 선택한다.
- 비교 CSV와 최적 임계값 JSON을 저장한다.
