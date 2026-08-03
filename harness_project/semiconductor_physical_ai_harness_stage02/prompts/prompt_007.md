# 실습 007 생성 하네스 프롬프트
역할: 제조 시스템 관측성 엔지니어.
목표: 콘솔과 파일에 동시에 기록되는 구조화 로그를 만든다.
필수 조건:
- logging.config.dictConfig와 YAML 설정을 사용한다.
- 시각, 로그 수준, 로거 이름, 메시지를 기록한다.
- 예외 발생 시 stack trace를 파일에 남긴다.
- logs/harness.log 이외의 시스템 로그는 수정하지 않는다.
검증:
- INFO, WARNING, ERROR 로그가 모두 파일에 존재하는지 확인한다.
