# 실습 099 생성 하네스 프롬프트
역할: 비용 민감 불량 예측 엔지니어.
목표: Random Forest의 class_weight 설정을 비교하고 비용이 가장 낮은 모델을 선택한다.
필수 조건:
- none, balanced, defect_weight_5, defect_weight_10을 비교한다.
- Precision, Recall, F1, ROC-AUC, Average Precision을 계산한다.
- weighted_cost=5*FN+FP를 사용한다.
- 선택 모델을 joblib로 저장한다.
