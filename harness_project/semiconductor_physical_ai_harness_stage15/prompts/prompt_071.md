# 실습 071 생성 하네스 프롬프트
역할: 반도체 공정 능력 분석가.
목표: 부분군 내부 표준편차로 단기 변동을 추정해 Cp, Cpu, Cpl, Cpk를 계산한다.
필수 조건:
- 규격 JSON에서 LSL, USL, subgroup_size를 읽는다.
- 부분군 크기 5를 사용한다.
- within_sigma, process_mean, Cp, Cpu, Cpl, Cpk를 JSON으로 저장한다.
- Cpk는 Cpu와 Cpl 중 작은 값으로 계산한다.
