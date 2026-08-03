# 실습 066 생성 하네스 프롬프트
역할: 반도체 PCA 기준 모델 엔지니어.
목표: 초기 400개 정상 샘플로 StandardScaler와 누적 설명분산 95% PCA를 학습한다.
필수 조건:
- StandardScaler 후 PCA를 학습한다.
- n_components=0.95와 svd_solver='full'을 사용한다.
- scaler와 PCA를 joblib 번들로 저장한다.
- 주성분 수와 설명분산을 JSON으로 저장한다.
