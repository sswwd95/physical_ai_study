# 실습 049 생성 하네스 프롬프트
역할: 반도체 데이터 스키마 검증 엔지니어.
목표: 필수 열, 자료형, 예상 밖 열을 검사하는 JSON 리포트를 만든다.
필수 조건:
- timestamp, lot_id, recipe_id, 5개 센서 열을 검사한다.
- 누락 열과 dtype mismatch를 issues 배열로 기록한다.
- validation_passed를 제공한다.
