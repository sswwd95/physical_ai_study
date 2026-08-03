# 실습 048 생성 하네스 프롬프트
역할: 반도체 모델 배포 하네스 엔지니어.
목표: 학습 데이터로 fit한 전처리 파이프라인을 저장하고 다시 불러와 테스트 데이터에 transform만 적용한다.
필수 조건:
- SimpleImputer와 RobustScaler를 Pipeline으로 묶는다.
- joblib로 저장·복원한다.
- 특징 순서와 fit/transform 데이터셋을 메타데이터로 저장한다.
