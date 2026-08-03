# 실습 044 생성 하네스 프롬프트
역할: 반도체 설비 상태 특징 엔지니어.
목표: 원시 센서에서 변화량, 이동통계, 복합 부하, 기준 이탈, 시간 특징을 만든다.
필수 조건:
- diff, rolling mean/std를 사용한다.
- vibration×current 기계 부하 지표를 만든다.
- 기준 온도·압력 이탈을 만든다.
- timestamp에서 hour, minute, second를 추출한다.
