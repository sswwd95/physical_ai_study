# 실습 012 생성 하네스 프롬프트
역할: 반도체 공정 통계 분석가.
목표: 온도, 압력, 가스 유량, 진동, 모터 전류의 기술통계를 계산한다.
필수 조건:
- count, mean, median, std, min, quartile, max를 포함한다.
- 변동계수 CV(%)와 결측 개수를 추가한다.
- 결과를 outputs/sensor_descriptive_statistics.csv로 저장한다.
해석:
- CV가 큰 센서는 상대 변동이 큰 센서 후보로 설명한다.
