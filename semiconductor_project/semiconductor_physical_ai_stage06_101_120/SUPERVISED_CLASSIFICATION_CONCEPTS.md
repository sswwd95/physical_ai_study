# 지도학습 불량 분류 핵심 개념

## 데이터 분할
- Stratified split: 클래스 비율을 유지
- Group split: 같은 LOT가 학습과 평가에 겹치지 않도록 분리
- Time split: 미래 데이터를 과거 학습에 섞지 않도록 분리

## 주요 지표
- Accuracy: 전체 예측 중 정답 비율
- Precision: 불량 예측 중 실제 불량 비율
- Recall: 실제 불량 중 탐지한 비율
- F1: Precision과 Recall의 조화평균
- ROC-AUC: 전체 임계값에서 클래스 분리 능력
- PR-AUC: 희소한 불량 클래스에 더 집중한 성능

## 모델 특성
- Logistic Regression: 계수 방향을 해석하기 쉬움
- Decision Tree: 규칙을 이해하기 쉬우나 과적합 가능
- Random Forest: 안정적이고 비선형 관계를 잘 표현하지만 해석이 상대적으로 어려움
