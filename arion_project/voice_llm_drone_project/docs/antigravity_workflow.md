# Antigravity 하네스 워크플로

## 생성 단계

1. Mission JSON Schema 생성
2. 정상·모호·위험·프롬프트 주입 명령 테스트 생성
3. Safety Supervisor 경계값 테스트 생성
4. MuJoCo 회귀 시나리오 생성
5. 로그 필드 누락 검사
6. PyMC 분석 재현성 검사

## 검토 체크리스트

- LLM과 actuator가 직접 연결되어 있지 않은가
- 좌표계와 단위가 명시되어 있는가
- timeout과 emergency_stop이 존재하는가
- 스키마 오류 시 fail-safe인가
- 안전 수정과 거부 이유가 로그에 남는가
- 동일 입력 반복 실행 결과를 비교할 수 있는가
