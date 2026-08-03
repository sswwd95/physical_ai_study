# 실습 063 생성 하네스 프롬프트
역할: 다변량 공정 경보 통합 엔지니어.
목표: 센서별 Z-score 경보 개수와 Hotelling T² 경보를 결합한다.
필수 조건:
- timestamp 일치 여부를 먼저 검사한다.
- combined_vote_count를 만든다.
- NORMAL, WATCH, WARNING, CRITICAL 등급을 부여한다.
- 결과를 CSV로 저장한다.
