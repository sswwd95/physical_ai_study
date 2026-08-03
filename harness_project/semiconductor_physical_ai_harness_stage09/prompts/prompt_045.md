# 실습 045 생성 하네스 프롬프트
역할: 반도체 ML 전처리 하네스 엔지니어.
목표: 파생 변수 생성, 중앙값 결측 대체, Robust Scaling을 하나의 재현 가능한 파이프라인으로 통합한다.
필수 조건:
- sklearn Pipeline과 ColumnTransformer를 사용한다.
- 입력 특징 목록과 처리 단계를 메타데이터 JSON으로 저장한다.
- 출력에 timestamp, lot_id, recipe_id를 유지한다.
- 처리 후 결측값이 0인지 검증한다.
