# 실습 076 생성 하네스 프롬프트
역할: 반도체 공정 분포 검증 엔지니어.
목표: Shapiro-Wilk와 D'Agostino K² 검정으로 정규성을 평가한다.
필수 조건:
- 왜도와 초과첨도를 함께 계산한다.
- 두 검정의 statistic과 p-value를 저장한다.
- p<0.05이면 normality_rejected_at_0_05=True로 기록한다.
- 결과를 CSV로 저장한다.
