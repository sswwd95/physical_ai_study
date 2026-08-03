# 실습 061~080 Antigravity 하네스 프롬프트

## 실습 061 — baseline_window_selection
```text
초기 120개 시점을 정상 기준 구간으로 사용하여 온도와 압력의 평균과 표준편차를 계산하라.
기준 구간과 전체 구간 통계를 비교하고 CSV로 저장하라.
```

## 실습 062 — standardized_residuals
```text
초기 120개 온도 데이터를 기준으로 z=(x-mean)/std를 계산하라.
절댓값 2 이상, 3 이상인 행의 개수를 각각 출력하고 결과를 CSV로 저장하라.
```

## 실습 063 — upper_cusum_temperature
```text
초기 120개 온도를 기준으로 상방 CUSUM을 계산하라.
표준화 데이터에 대해 k=0.5, h=5를 사용하고 S+=max(0, 이전S+z-k)로 계산하라.
h를 넘는 행에 alarm 플래그를 만들고 CSV로 저장하라.
```

## 실습 064 — lower_cusum_temperature
```text
초기 120개 온도를 기준으로 하방 CUSUM을 계산하라.
표준화 데이터에 대해 k=0.5, h=5를 사용하고 S-=min(0, 이전S+z+k)로 계산하라.
절댓값이 h 이상이면 경보로 표시하라.
```

## 실습 065 — two_sided_cusum
```text
온도에 대해 상방과 하방 CUSUM을 함께 계산하는 함수를 작성하라.
k=0.5, h=5를 사용하고 어느 한쪽이라도 임계값을 넘으면 two_sided_alarm으로 표시하라.
```

## 실습 066 — cusum_parameter_comparison
```text
온도 상방 CUSUM에서 k=[0.25,0.5,1.0], h=[4,5,8] 조합을 비교하라.
각 조합별 최초 경보 인덱스와 전체 경보 행 수를 표로 만들고 CSV로 저장하라.
```

## 실습 067 — ewma_control_limits
```text
초기 120개 온도를 기준으로 lambda=0.2, L=3인 EWMA를 계산하라.
시간 t에 따른 표준편차 공식 sigma*sqrt(lambda/(2-lambda)*(1-(1-lambda)^(2t)))을 사용하여
EWMA UCL/LCL을 만들고 경보를 저장하라.
```

## 실습 068 — ewma_lambda_comparison
```text
온도 데이터에 lambda 0.05, 0.2, 0.5의 EWMA를 각각 계산하라.
세 컬럼을 한 CSV에 저장하고 마지막 20행을 출력하라.
```

## 실습 069 — rolling_variance_change
```text
온도에 대해 30개 시점 이동분산을 계산하라.
초기 120개 구간 분산의 2배를 초과하면 variance_alarm으로 표시하고 최초 경보 시점을 출력하라.
```

## 실습 070 — variance_ratio_monitor
```text
온도 기준분산은 초기 120개로 계산하라.
최근 40개 이동분산을 기준분산으로 나눈 variance_ratio를 만들고
비율이 2.5 이상이면 경보로 표시하여 CSV로 저장하라.
```

## 실습 071 — mean_shift_scan
```text
온도 시계열에서 후보 인덱스 60부터 len-60까지를 5칸 간격으로 탐색하라.
각 후보에서 앞 구간과 뒤 구간 평균 차이 절댓값을 계산하고 가장 큰 후보 10개를 저장하라.
```

## 실습 072 — window_mean_difference
```text
각 시점 기준 앞 20개와 뒤 20개의 온도 평균 차이를 계산하라.
절댓값이 1.0°C 이상이면 local_change_alarm으로 표시하고 결과를 저장하라.
```

## 실습 073 — multi_sensor_change_score
```text
초기 120개를 기준으로 온도, 압력, 진동의 z-score를 계산하라.
각 절댓값을 합한 change_score를 만들고 8 이상이면 change_alarm으로 표시하라.
고득점 상위 20행을 저장하라.
```

## 실습 074 — pca_distance_monitor
```text
초기 120개 온도, 압력, RF, 가스, 진동을 StandardScaler와 PCA(2)로 학습하라.
전체 데이터를 변환하고 기준 PCA 점수 평균으로부터 유클리드 거리를 계산하라.
기준 거리 99% 분위수를 넘으면 alarm으로 표시하라.
```

## 실습 075 — mahalanobis_distance_monitor
```text
초기 120개의 온도, 압력, RF, 가스, 진동으로 평균과 공분산을 계산하라.
전체 행의 Mahalanobis 거리 제곱을 계산하고 기준 구간 99% 분위수를 넘으면 경보로 표시하라.
```

## 실습 076 — drift_segment_summary
```text
온도 상방 CUSUM 경보를 계산한 뒤 연속된 True 구간마다 segment_id를 부여하라.
각 세그먼트의 시작, 종료, 길이, 평균 온도를 요약하여 CSV로 저장하라.
```

## 실습 077 — alarm_cooldown
```text
change_score가 8 이상인 시점을 원시 경보로 정의하라.
한 번 경보가 발생하면 다음 20개 시점 동안 새 경보를 억제하는 cooldown_alarm을 구현하라.
원시 경보 수와 최종 경보 수를 비교하라.
```

## 실습 078 — alarm_severity_levels
```text
온도, 압력, 진동의 절대 z-score 합으로 change_score를 계산하라.
0~4 normal, 4~8 caution, 8~12 warning, 12 이상 critical로 분류하고 등급별 건수를 출력하라.
```

## 실습 079 — change_detection_dashboard
```text
timestamp별 온도, 상방 CUSUM, EWMA, EWMA UCL/LCL, 분산비,
다중 센서 change_score, severity를 포함하는 대시보드 CSV를 생성하라.
```

## 실습 080 — automated_change_report
```text
온도 상방 CUSUM, EWMA 경보, 분산비 경보, 다중 센서 change_score를 계산하라.
summary, alarm_rows, segments 세 시트의 Excel 보고서와 CSV 요약을 생성하라.
```
