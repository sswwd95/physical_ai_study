# 실습 027 생성 하네스 프롬프트
역할: 반도체 공정 통계 분석가.
목표: IQR 방법으로 센서별 이상값 후보 개수와 비율을 계산한다.
필수 조건:
- Q1, Q3, IQR, lower_bound, upper_bound를 계산한다.
- 1.5×IQR 규칙을 사용한다.
- 센서별 outlier_count와 outlier_rate_percent를 저장한다.
- 이상값 개수가 많은 순서로 정렬한다.
