# 실습 082 생성 하네스 프롬프트
역할: 반도체 센서 구간별 불량률 분석가.
목표: 5개 센서를 4분위 구간으로 나누고 구간별 표본 수·불량 수·불량률을 계산한다.
필수 조건:
- pandas qcut을 사용한다.
- feature, bin, sample_count, defect_count, defect_rate_percent를 저장한다.
- 구간 표본이 너무 적으면 해석에 주의한다고 설명한다.
