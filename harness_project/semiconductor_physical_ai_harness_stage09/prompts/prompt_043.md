# 실습 043 생성 하네스 프롬프트
역할: 강건한 반도체 데이터 전처리 엔지니어.
목표: 중앙값과 IQR을 사용해 센서값을 Robust Scaling한다.
필수 조건:
- RobustScaler와 quantile_range=(25,75)를 사용한다.
- 센서별 median과 IQR scale을 JSON으로 저장한다.
- 이상값 영향에 StandardScaler보다 강건하다고 설명한다.
