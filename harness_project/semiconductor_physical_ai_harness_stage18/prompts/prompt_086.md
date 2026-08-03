# 실습 086 생성 하네스 프롬프트
역할: 반도체 불량 예측 모델 엔지니어.
목표: 시간 순서 70/30 분할과 숫자·범주형 전처리를 포함한 로지스틱 회귀 모델을 학습한다.
필수 조건:
- 숫자형은 median imputation과 StandardScaler를 사용한다.
- 범주형은 most_frequent imputation과 OneHotEncoder를 사용한다.
- LogisticRegression(class_weight='balanced')를 사용한다.
- 모델과 메타데이터를 저장한다.
