# 이상 탐지 핵심 개념

## 이상 유형
- 점 이상: 한 시점이 주변과 크게 다름
- 집단 이상: 여러 시점이 연속적으로 비정상
- 문맥적 이상: 상태·레시피·LOT 조건에서만 비정상

## 평가 지표
- Precision: 모델이 이상이라고 한 것 중 실제 이상 비율
- Recall: 실제 이상 중 모델이 찾은 비율
- Specificity: 실제 정상 중 정상으로 판정한 비율
- F1: Precision과 Recall의 조화평균

## 모델 특성
- Isolation Forest: 격리하기 쉬운 데이터를 이상으로 판단
- LOF: 주변 이웃과 밀도가 다른 데이터를 이상으로 판단
- One-Class SVM: 정상 영역의 경계를 학습
- Robust Covariance: 이상값 영향을 줄인 다변량 거리
- PCA Reconstruction Error: 정상 저차원 구조로 복원되지 않는 정도
