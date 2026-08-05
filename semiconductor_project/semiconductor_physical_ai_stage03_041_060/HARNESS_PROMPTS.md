# 실습 041~060 Antigravity 하네스 프롬프트

## 실습 041 — process_variable_summary
```text
반도체 장비 센서 CSV에서 온도, 압력, RF 전력, 가스 유량, 진동의
평균, 표준편차, 최솟값, 중앙값, 최댓값을 계산하는 초보자용 pandas 예제를 작성하라.
결과는 CSV로 저장하고 소수 셋째 자리까지 출력하라.
```

## 실습 042 — lot_mean_comparison
```text
lot_id별 온도, 압력, RF 전력, 가스 유량의 평균을 계산하고
전체 평균과의 차이도 함께 계산하는 pandas 예제를 작성하라.
결과를 CSV로 저장하라.
```

## 실습 043 — rolling_mean_std
```text
챔버 온도에 대해 20개 시점 이동평균과 이동표준편차를 계산하라.
min_periods=5를 사용하고 마지막 30행을 출력한 뒤 CSV로 저장하라.
```

## 실습 044 — ewma_monitoring
```text
온도 센서에 대해 span=20인 EWMA를 계산하라.
원본 온도와 EWMA를 CSV로 저장하고 마지막 20행을 출력하라.
```

## 실습 045 — three_sigma_limits
```text
챔버 압력의 평균과 표준편차를 계산하고 중심선 CL, 상한 UCL, 하한 LCL을
평균 ± 3표준편차로 계산하라. 관리한계를 벗어난 행을 출력하고 CSV로 저장하라.
```

## 실습 046 — individuals_control_chart
```text
챔버 온도의 평균과 표준편차로 I 관리도를 작성하라.
원본값, 중심선, UCL, LCL을 표시하고 관리한계 이탈점을 별도 마커로 표시한 뒤
PNG로 저장하라. 화면 없이 저장 가능하게 작성하라.
```

## 실습 047 — moving_range_chart
```text
온도 센서의 절대 1시점 차이를 moving_range로 계산하라.
MR 평균과 UCL=3.267*MR평균을 계산하고 MR 관리도를 PNG로 저장하라.
UCL을 넘는 시점 수를 출력하라.
```

## 실습 048 — subgroup_xbar_chart
```text
온도 데이터를 연속 5개씩 소그룹으로 묶고 subgroup_mean과 subgroup_range를 계산하라.
전체 소그룹 평균과 평균 범위를 사용하여 X-bar 관리한계를
UCL=Xdoublebar+0.577*Rbar, LCL=Xdoublebar-0.577*Rbar로 계산하라.
결과를 CSV로 저장하라.
```

## 실습 049 — subgroup_r_chart
```text
실습 048과 동일하게 5개씩 소그룹을 만들고 범위를 계산하라.
n=5의 D3=0, D4=2.114를 사용하여 R 관리도의 CL, UCL, LCL을 계산하고
관리한계 이탈 소그룹을 출력하라.
```

## 실습 050 — run_rule_one_side
```text
온도 평균을 중심선으로 사용하여 7개 연속 관측값이 모두 중심선 위 또는 아래에 있는
구간을 탐지하라. 각 행에 run_rule_violation 플래그를 추가하고 위반 행을 저장하라.
```

## 실습 051 — trend_rule_detection
```text
온도 데이터에서 6개 연속 관측값이 계속 상승하거나 계속 하락하는 구간을 탐지하라.
diff의 부호를 이용하고 trend_violation 플래그를 추가하여 결과를 CSV로 저장하라.
```

## 실습 052 — zone_rule_detection
```text
압력 평균과 표준편차를 계산하라.
최근 3개 중 2개 이상이 같은 방향으로 평균±2표준편차를 넘으면 zone_rule_violation으로
표시하라. 위쪽과 아래쪽 규칙을 모두 검사하고 위반 행을 저장하라.
```

## 실습 053 — cp_calculation
```text
챔버 온도의 규격하한 LSL=69, 규격상한 USL=75로 두고
Cp=(USL-LSL)/(6*sigma)를 계산하라. Cp가 1.33 이상인지 판정 메시지도 출력하라.
```

## 실습 054 — cpk_calculation
```text
챔버 온도의 LSL=69, USL=75를 사용하라.
CPU=(USL-mean)/(3*sigma), CPL=(mean-LSL)/(3*sigma), Cpk=min(CPU,CPL)를 계산하고
평균이 어느 규격 쪽에 더 가까운지 출력하라.
```

## 실습 055 — lot_capability_comparison
```text
lot_id별 챔버 온도 평균과 표준편차를 계산하고 LSL=69, USL=75를 사용하여
Cp, CPU, CPL, Cpk를 계산하라. Cpk가 낮은 순으로 정렬하고 CSV로 저장하라.
```

## 실습 056 — spec_violation_rate
```text
온도 규격 69~75°C, 압력 규격 17~19Pa를 적용하라.
각 센서별 규격 이탈 건수와 이탈률, 둘 중 하나라도 이탈한 행 비율을 계산하여 출력하고
요약 CSV를 저장하라.
```

## 실습 057 — multi_sensor_alarm_score
```text
온도 3시그마 이탈은 40점, 압력 3시그마 이탈은 30점,
진동 0.15g 이상은 20점, 입자 수 10 이상은 10점을 부여하라.
합계 50점 이상을 high_risk로 표시하고 위험 행을 CSV로 저장하라.
```

## 실습 058 — alarm_persistence
```text
실습 057과 같은 risk_score를 계산하라.
high_risk가 최근 5개 중 3개 이상이면 persistent_alarm으로 표시하라.
지속 경보 시작 시점을 찾아 출력하고 CSV로 저장하라.
```

## 실습 059 — spc_dashboard_data
```text
timestamp별 온도, 압력, EWMA, 온도 UCL/LCL, 압력 UCL/LCL,
규격 이탈 여부, 위험점수를 포함하는 대시보드용 CSV를 생성하라.
모든 기준값은 데이터에서 계산하고 결과의 마지막 10행을 출력하라.
```

## 실습 060 — automated_spc_report
```text
온도와 압력에 대해 평균, 표준편차, UCL, LCL, 규격하한, 규격상한,
Cp, Cpk, 관리한계 이탈 수, 규격 이탈 수를 계산하라.
summary, alarm_rows 두 시트의 Excel 보고서를 생성하고 CSV 요약도 함께 저장하라.
```
