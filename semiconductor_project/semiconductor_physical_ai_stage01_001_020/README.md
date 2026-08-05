# 반도체 Physical AI 하네스 엔지니어링
## 1단계: 001~020제 — 반도체 센서 데이터와 Python 기초

### 교육 대상
- ROS2 Humble 학습 전의 전공·비전공 혼합 취업 준비생
- Python, pandas, 센서 데이터, 베이즈 통계를 처음 접하는 학습자

### 권장 환경
- Windows 10
- Anaconda 또는 Miniconda
- Python 3.11
- pandas / NumPy / Matplotlib / SciPy / PyMC / ArviZ
- Antigravity: 프롬프트 기반 코드 생성·검토·수정 워크플로에 활용

### 설치
```bat
cd semiconductor_physical_ai_stage01_001_020
setup_windows.bat
conda activate semi-physical-ai
```

### 개별 실행
```bat
python examples\ex001_generate_sensor_data.py
python examples\ex002_load_and_inspect.py
```

### 전체 실행
```bat
run_all_windows.bat
```

> 실습 002~020은 실습 001이 생성한 CSV를 사용합니다.

## 실습 목록
| 번호 | 핵심 주제 | 학습 목표 | 소스 |
|---:|---|---|---|
| 001 | generate_sensor_data | 반도체 식각 장비를 모사한 온도·압력·RF 전력·가스 유량 센서 데이터를 생성하고 CSV 구조를 이해합니다. | `examples/ex001_generate_sensor_data.py` |
| 002 | load_and_inspect | CSV를 읽고 행·열 개수, 컬럼명, 자료형, 앞부분 데이터를 확인합니다. | `examples/ex002_load_and_inspect.py` |
| 003 | select_sensor_columns | 필요한 센서 컬럼만 선택하고 컬럼 선택 문법을 익힙니다. | `examples/ex003_select_sensor_columns.py` |
| 004 | basic_statistics | 평균·표준편차·최솟값·최댓값으로 센서의 기본 상태를 요약합니다. | `examples/ex004_basic_statistics.py` |
| 005 | filter_temperature | 조건식으로 고온 구간을 찾고 Boolean 필터링을 익힙니다. | `examples/ex005_filter_temperature.py` |
| 006 | create_derived_feature | 센서 두 개를 조합해 간단한 공정 부하 지표를 만듭니다. | `examples/ex006_create_derived_feature.py` |
| 007 | group_by_lot | LOT별 센서 평균과 변동성을 계산해 배치 간 차이를 확인합니다. | `examples/ex007_group_by_lot.py` |
| 008 | group_by_process_state | 공정 상태별 센서 특성을 비교합니다. | `examples/ex008_group_by_process_state.py` |
| 009 | handle_missing_values | 결측값을 탐지하고 중앙값으로 보정하는 기본 절차를 익힙니다. | `examples/ex009_handle_missing_values.py` |
| 010 | detect_duplicate_rows | 중복 행을 찾아 제거하고 데이터 품질 점검 절차를 익힙니다. | `examples/ex010_detect_duplicate_rows.py` |
| 011 | sort_by_particle_count | 입자 수가 높은 순서로 정렬하여 오염 위험 시점을 찾습니다. | `examples/ex011_sort_by_particle_count.py` |
| 012 | time_range_filter | 특정 시간 범위의 데이터만 선택하는 시계열 필터링을 익힙니다. | `examples/ex012_time_range_filter.py` |
| 013 | rolling_average | 이동평균으로 순간 잡음을 줄이고 추세를 확인합니다. | `examples/ex013_rolling_average.py` |
| 014 | simple_threshold_alarm | 다중 센서 임계값으로 기초 경보 규칙을 구현합니다. | `examples/ex014_simple_threshold_alarm.py` |
| 015 | zscore_temperature | Z-score를 계산해 평균에서 멀리 떨어진 온도값을 탐지합니다. | `examples/ex015_zscore_temperature.py` |
| 016 | sensor_correlation | 센서 간 선형 상관관계를 계산하고 해석의 기초를 익힙니다. | `examples/ex016_sensor_correlation.py` |
| 017 | plot_temperature_trend | Matplotlib으로 시간에 따른 온도 추세를 시각화하고 파일로 저장합니다. | `examples/ex017_plot_temperature_trend.py` |
| 018 | plot_sensor_histogram | 히스토그램으로 센서값의 분포 모양을 확인합니다. | `examples/ex018_plot_sensor_histogram.py` |
| 019 | bayesian_temperature_mean | PyMC로 챔버 평균 온도의 사후분포를 추정하는 첫 베이즈 실습을 수행합니다. | `examples/ex019_bayesian_temperature_mean.py` |
| 020 | bayesian_alarm_probability | 베타-이항 모형으로 공정 경보 확률을 추정합니다. | `examples/ex020_bayesian_alarm_probability.py` |

## 폴더 구조
```text
semiconductor_physical_ai_stage01_001_020/
├─ data/             # 실습 001이 생성하는 센서 CSV
├─ examples/         # 001~020 Python 소스
├─ guides/           # 예제별 프롬프트·절차·라인별 해설
├─ outputs/          # 실행 결과 CSV와 PNG
├─ environment.yml
├─ requirements.txt
├─ setup_windows.bat
└─ run_all_windows.bat
```

## 하네스 엔지니어링 공통 절차
1. 요구사항을 센서, 입력, 처리, 출력, 검증 조건으로 분해합니다.
2. Antigravity에 예제별 하네스 프롬프트를 입력합니다.
3. 생성 코드가 파일 경로, 컬럼명, 단위, 예외 처리를 지키는지 검토합니다.
4. 작은 샘플 데이터로 먼저 실행합니다.
5. 결과 건수, 범위, 결측값, 그래프를 확인합니다.
6. 수정 지시를 구체적으로 작성하고 다시 생성합니다.
7. 최종 코드를 버전 관리하고 재현 가능한 환경 파일과 함께 보관합니다.

## 학습 완료 기준
- DataFrame 읽기, 선택, 필터, 그룹화, 정렬을 설명할 수 있다.
- 결측·중복 데이터의 기본 처리 방법을 적용할 수 있다.
- 이동평균, 임계값, Z-score의 의미를 설명할 수 있다.
- 센서 추세와 분포를 그래프로 저장할 수 있다.
- PyMC의 사전분포, 우도, 사후분포를 기초 수준에서 구분할 수 있다.
