# 실습 093 생성 하네스 프롬프트
역할: 반도체 예측확률 보정 엔지니어.
목표: Random Forest 확률을 isotonic calibration으로 보정한다.
필수 조건:
- CalibratedClassifierCV(method='isotonic', cv=3)를 사용한다.
- 원본·보정 확률의 Brier score와 Log loss를 비교한다.
- 보정 모델과 Wafer별 확률 CSV를 저장한다.
