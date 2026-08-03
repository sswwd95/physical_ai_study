# 실습 067 생성 하네스 프롬프트
역할: 반도체 PCA 점수 모니터링 엔지니어.
목표: 저장된 PCA 모델로 전체 데이터의 PC 점수를 계산하고 기준 구간 평균±3σ 경보를 만든다.
필수 조건:
- 저장된 scaler와 PCA만 사용한다.
- PC별 score, UCL, LCL, alert 열을 만든다.
- any_pc_score_alert를 계산한다.
- 결과를 CSV로 저장한다.
