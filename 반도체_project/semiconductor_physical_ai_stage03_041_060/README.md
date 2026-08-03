# 반도체 Physical AI 하네스 엔지니어링
## 3단계: 041~060제 — 반도체 공정 변수 모니터링과 기초 SPC

### 단계 목표
- 공정 변수의 중심과 변동을 구분한다.
- 이동평균, EWMA, 3시그마 관리한계를 계산한다.
- I-MR, X-bar, R 관리도의 기본 구조를 이해한다.
- 런·추세·구역 규칙으로 비정상 패턴을 감지한다.
- Cp와 Cpk로 공정능력을 평가한다.
- 여러 경보를 통합한 위험점수와 자동 보고서를 만든다.

### 실행 환경
- Windows 10
- Anaconda 또는 Miniconda
- Python 3.11
- pandas, NumPy, Matplotlib, SciPy, openpyxl

### 설치
```bat
cd semiconductor_physical_ai_stage03_041_060
setup_windows.bat
conda activate semi-physical-ai-stage03
```

### 전체 실행
```bat
run_all_windows.bat
```

## 실습 목록
| 번호 | 핵심 주제 | 학습 목표 | 소스 |
|---:|---|---|---|
| 041 | process_variable_summary | 주요 공정 변수의 평균, 표준편차, 최소, 최대, 중앙값을 한 번에 요약합니다. | `examples/ex041_process_variable_summary.py` |
| 042 | lot_mean_comparison | LOT별 평균 공정 조건을 비교하여 배치 간 차이를 확인합니다. | `examples/ex042_lot_mean_comparison.py` |
| 043 | rolling_mean_std | 이동평균과 이동표준편차로 공정의 국소 추세와 변동성을 계산합니다. | `examples/ex043_rolling_mean_std.py` |
| 044 | ewma_monitoring | EWMA를 이용해 최근 공정 변화에 민감한 추세 지표를 만듭니다. | `examples/ex044_ewma_monitoring.py` |
| 045 | three_sigma_limits | 평균과 표준편차를 이용해 3시그마 관리한계를 계산합니다. | `examples/ex045_three_sigma_limits.py` |
| 046 | individuals_control_chart | 개별값 관리도(I Chart)를 생성하고 관리한계 이탈점을 표시합니다. | `examples/ex046_individuals_control_chart.py` |
| 047 | moving_range_chart | 연속 두 관측값의 차이로 이동범위(MR)를 계산하고 MR 관리도를 작성합니다. | `examples/ex047_moving_range_chart.py` |
| 048 | subgroup_xbar_chart | 5개 관측값을 한 소그룹으로 묶어 X-bar 관리도의 기초를 실습합니다. | `examples/ex048_subgroup_xbar_chart.py` |
| 049 | subgroup_r_chart | 소그룹 범위로 R 관리도의 중심선과 관리한계를 계산합니다. | `examples/ex049_subgroup_r_chart.py` |
| 050 | run_rule_one_side | 중심선 한쪽에 연속으로 나타나는 런 규칙을 탐지합니다. | `examples/ex050_run_rule_one_side.py` |
| 051 | trend_rule_detection | 연속 상승 또는 연속 하락 추세를 감지합니다. | `examples/ex051_trend_rule_detection.py` |
| 052 | zone_rule_detection | 2시그마와 3시그마 구역을 이용한 간단한 Western Electric 규칙을 적용합니다. | `examples/ex052_zone_rule_detection.py` |
| 053 | cp_calculation | 규격폭과 공정 표준편차를 이용해 잠재 공정능력 Cp를 계산합니다. | `examples/ex053_cp_calculation.py` |
| 054 | cpk_calculation | 공정 평균의 치우침까지 반영하는 Cpk를 계산합니다. | `examples/ex054_cpk_calculation.py` |
| 055 | lot_capability_comparison | LOT별 Cp와 Cpk를 계산해 배치 간 공정능력을 비교합니다. | `examples/ex055_lot_capability_comparison.py` |
| 056 | spec_violation_rate | 규격 이탈률을 계산해 실제 불량 후보 비율을 정량화합니다. | `examples/ex056_spec_violation_rate.py` |
| 057 | multi_sensor_alarm_score | 여러 SPC 경보를 점수화해 통합 공정 위험 점수를 만듭니다. | `examples/ex057_multi_sensor_alarm_score.py` |
| 058 | alarm_persistence | 순간 경보와 지속 경보를 구분해 오경보를 줄입니다. | `examples/ex058_alarm_persistence.py` |
| 059 | spc_dashboard_data | 관리도와 KPI에 사용할 통합 대시보드 데이터를 생성합니다. | `examples/ex059_spc_dashboard_data.py` |
| 060 | automated_spc_report | 공정 요약, 관리한계, 공정능력, 경보 건수를 하나의 Excel 보고서로 자동 생성합니다. | `examples/ex060_automated_spc_report.py` |

## 핵심 구분
- **관리한계**: 현재 공정 데이터의 평균과 변동으로 계산한다.
- **규격한계**: 고객, 설계, 품질 기준에서 정한다.
- 관리한계 안에 있어도 규격을 벗어날 수 있다.
- 규격 안에 있어도 비정상 추세나 런 규칙이 나타날 수 있다.

## 폴더 구조
```text
semiconductor_physical_ai_stage03_041_060/
├─ data/
├─ examples/
├─ guides/
├─ outputs/
├─ README.md
├─ CURRICULUM.md
├─ HARNESS_PROMPTS.md
├─ SPC_FORMULAS.md
├─ environment.yml
├─ setup_windows.bat
└─ run_all_windows.bat
```
