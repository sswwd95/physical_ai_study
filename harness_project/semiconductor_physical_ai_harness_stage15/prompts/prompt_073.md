# 실습 073 생성 하네스 프롬프트
역할: 반도체 규격 이탈 분석가.
목표: LSL 미만과 USL 초과를 구분하고 실제 관측 이탈률과 PPM을 계산한다.
필수 조건:
- below_lsl, above_usl, out_of_spec 열을 만든다.
- 위반 행 CSV와 요약 JSON을 저장한다.
- out_of_spec_rate_percent와 ppm_observed를 계산한다.
