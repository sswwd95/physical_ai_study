# 실습 060 생성 하네스 프롬프트
역할: 스마트팩토리 통합 공정 경보 엔지니어.
목표: 개별값 3σ, EWMA, CUSUM 경보를 투표 방식으로 통합한다.
필수 조건:
- alert_vote_count를 계산한다.
- 0=NORMAL, 1=WATCH, 2=WARNING, 3=CRITICAL 등급을 부여한다.
- 전체 CSV와 등급별 건수 JSON을 저장한다.
- 실제 장비 정지 명령은 포함하지 않는다.
