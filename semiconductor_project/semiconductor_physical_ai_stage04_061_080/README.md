# 반도체 Physical AI 하네스 엔지니어링
## 4단계: 061~080제 — CUSUM·EWMA 고급 모니터링과 공정 변화 감지

### 단계 목표
- 정상 기준 구간을 설정하고 기준선 오염의 위험을 이해한다.
- CUSUM으로 작은 평균 이동을 누적 감지한다.
- EWMA 관리한계와 lambda 민감도를 비교한다.
- 평균 변화와 분산 변화를 분리해서 감시한다.
- 단변량·다변량 변화 감지 결과를 통합한다.
- 경보 세그먼트, 쿨다운, 심각도 등급을 적용한다.

### 실행 환경
- Windows 10
- Anaconda 또는 Miniconda
- Python 3.11
- NumPy, pandas, Matplotlib, SciPy, scikit-learn, openpyxl

### 설치 및 실행
```bat
cd semiconductor_physical_ai_stage04_061_080
conda env create -f environment.yml
conda activate semi-physical-ai-stage04
run_all_windows.bat
```

## 실습 목록
| 번호 | 핵심 주제 | 학습 목표 | 소스 |
|---:|---|---|---|
| 061 | baseline_window_selection | 초기 정상 구간을 기준선으로 선택하고 평균·표준편차를 계산합니다. | `examples/ex061_baseline_window_selection.py` |
| 062 | standardized_residuals | 기준 구간의 평균과 표준편차로 표준화 잔차를 계산합니다. | `examples/ex062_standardized_residuals.py` |
| 063 | upper_cusum_temperature | 상방 CUSUM으로 작은 온도 평균 상승을 누적 감지합니다. | `examples/ex063_upper_cusum_temperature.py` |
| 064 | lower_cusum_temperature | 하방 CUSUM으로 작은 온도 평균 하락을 감지합니다. | `examples/ex064_lower_cusum_temperature.py` |
| 065 | two_sided_cusum | 상방·하방 CUSUM을 동시에 계산해 양방향 평균 변화를 감지합니다. | `examples/ex065_two_sided_cusum.py` |
| 066 | cusum_parameter_comparison | k와 h 조합에 따른 CUSUM 경보 민감도를 비교합니다. | `examples/ex066_cusum_parameter_comparison.py` |
| 067 | ewma_control_limits | EWMA 중심선과 시간에 따라 변하는 관리한계를 계산합니다. | `examples/ex067_ewma_control_limits.py` |
| 068 | ewma_lambda_comparison | lambda 값에 따른 EWMA 반응 속도를 비교합니다. | `examples/ex068_ewma_lambda_comparison.py` |
| 069 | rolling_variance_change | 이동분산으로 공정 변동성 증가 구간을 감지합니다. | `examples/ex069_rolling_variance_change.py` |
| 070 | variance_ratio_monitor | 최근 구간 분산과 기준 분산의 비율로 변동성 변화를 정량화합니다. | `examples/ex070_variance_ratio_monitor.py` |
| 071 | mean_shift_scan | 분할점 후보마다 앞뒤 평균 차이를 계산해 변화점 후보를 찾습니다. | `examples/ex071_mean_shift_scan.py` |
| 072 | window_mean_difference | 좌우 고정 창의 평균 차이로 국소 변화점을 탐지합니다. | `examples/ex072_window_mean_difference.py` |
| 073 | multi_sensor_change_score | 온도·압력·진동의 표준화 변화량을 합쳐 다중 센서 변화점수를 만듭니다. | `examples/ex073_multi_sensor_change_score.py` |
| 074 | pca_distance_monitor | 주성분 공간에서 기준 공정과의 거리를 계산합니다. | `examples/ex074_pca_distance_monitor.py` |
| 075 | mahalanobis_distance_monitor | 센서 공분산을 반영한 Mahalanobis 거리로 다변량 이상을 감지합니다. | `examples/ex075_mahalanobis_distance_monitor.py` |
| 076 | drift_segment_summary | 경보가 연속된 구간을 하나의 드리프트 세그먼트로 묶습니다. | `examples/ex076_drift_segment_summary.py` |
| 077 | alarm_cooldown | 경보 후 일정 시간 동안 재경보를 억제하는 쿨다운 로직을 구현합니다. | `examples/ex077_alarm_cooldown.py` |
| 078 | alarm_severity_levels | 변화점수에 따라 주의·경고·위험 등급을 부여합니다. | `examples/ex078_alarm_severity_levels.py` |
| 079 | change_detection_dashboard | CUSUM·EWMA·분산비·다중 센서 점수를 한 파일에 통합합니다. | `examples/ex079_change_detection_dashboard.py` |
| 080 | automated_change_report | 여러 변화 감지 지표와 경보 세그먼트를 Excel 보고서로 자동 생성합니다. | `examples/ex080_automated_change_report.py` |

## 데이터 특징
- 총 360개 시점
- 초기 120개는 정상 기준 구간
- 140~219 구간에는 점진적 온도·압력 드리프트
- 260~299 구간에는 온도·압력·진동의 급격한 변화
- 작은 변화와 큰 변화를 모두 실습할 수 있도록 구성

## 실무 원칙
1. 정상 기준 구간은 공정 엔지니어가 승인해야 한다.
2. CUSUM의 k와 h는 탐지하려는 변화 크기에 맞춰야 한다.
3. EWMA의 lambda가 크면 빠르지만 노이즈에 민감하다.
4. 평균 변화와 분산 변화는 별도로 감시해야 한다.
5. 경보는 행 단위가 아니라 사건 단위 세그먼트로 관리하는 것이 좋다.
