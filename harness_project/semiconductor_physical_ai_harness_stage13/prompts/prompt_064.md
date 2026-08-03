# 실습 064 생성 하네스 프롬프트
역할: 스마트팩토리 공정 건강도 설계자.
목표: 평균 절대 Z-score와 T² 임계값 비율을 결합해 0~100 상태 점수를 만든다.
필수 조건:
- mean_absolute_zscore와 t2_ratio를 계산한다.
- risk_score 가중치는 0.55와 0.45를 사용한다.
- HEALTHY, WATCH, DEGRADED, CRITICAL 등급을 만든다.
- 교육용 가중치임을 명시한다.
