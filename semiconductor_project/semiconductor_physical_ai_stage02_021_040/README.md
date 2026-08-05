# 반도체 Physical AI 하네스 엔지니어링
## 2단계: 021~040제 — pandas 기반 센서 데이터 전처리와 품질 검증

### 단계 목표
- 입력 스키마와 자료형을 검증한다.
- 센서 단위와 허용 범위를 명시한다.
- 결측·중복·시간축·범주 오류를 탐지한다.
- 이상값 처리 전후를 감사 가능한 형태로 남긴다.
- 재사용 가능한 데이터 정제 파이프라인을 완성한다.

### 실행 환경
- Windows 10
- Anaconda 또는 Miniconda
- Python 3.11
- pandas, NumPy, openpyxl

### 설치 및 실행
```bat
cd semiconductor_physical_ai_stage02_021_040
setup_windows.bat
conda activate semi-physical-ai-stage02
python examples\ex021_schema_validation.py
```

### 전체 실행
```bat
run_all_windows.bat
```

> 실습 026~032, 038~040은 실습 025에서 만드는 오류 연습 데이터를 사용합니다.
> 전체 실행 배치 파일은 번호 순으로 실행하므로 자동으로 준비됩니다.

## 실습 목록
| 번호 | 핵심 주제 | 학습 목표 | 소스 |
|---:|---|---|---|
| 021 | schema_validation | 필수 컬럼과 컬럼 순서를 검사하여 입력 스키마 오류를 조기에 발견합니다. | `examples/ex021_schema_validation.py` |
| 022 | dtype_normalization | 문자열·실수·정수·범주형 컬럼의 자료형을 명시적으로 정규화합니다. | `examples/ex022_dtype_normalization.py` |
| 023 | unit_conversion | 센서 단위를 변환하면서 원본 단위 컬럼을 보존하는 방법을 익힙니다. | `examples/ex023_unit_conversion.py` |
| 024 | allowed_range_check | 공정 엔지니어가 정의한 허용 범위 밖의 센서값을 플래그로 표시합니다. | `examples/ex024_allowed_range_check.py` |
| 025 | inject_quality_errors | 후속 품질검사를 위해 결측·중복·역순 시간·잘못된 범주값을 포함한 연습 데이터를 만듭니다. | `examples/ex025_inject_quality_errors.py` |
| 026 | missing_value_profile | 결측값의 개수와 비율을 컬럼별 품질 프로파일로 작성합니다. | `examples/ex026_missing_value_profile.py` |
| 027 | time_interpolation | 시계열 센서 결측값을 시간 기준 선형보간으로 복원합니다. | `examples/ex027_time_interpolation.py` |
| 028 | duplicate_key_check | timestamp와 lot_id 복합키의 중복을 검사하고 원인을 분리해 확인합니다. | `examples/ex028_duplicate_key_check.py` |
| 029 | remove_duplicates_with_audit | 중복 제거 전후의 행 수와 제거 대상을 감사 로그로 남깁니다. | `examples/ex029_remove_duplicates_with_audit.py` |
| 030 | timestamp_monotonicity | 시간축이 증가하는지 검사하고 역순·동일 시각 데이터를 찾습니다. | `examples/ex030_timestamp_monotonicity.py` |
| 031 | sampling_interval_check | 예상 샘플링 주기 1초에서 벗어난 누락·지연·중복 시점을 탐지합니다. | `examples/ex031_sampling_interval_check.py` |
| 032 | category_validation | 허용된 LOT와 공정 상태만 존재하는지 범주형 값을 검증합니다. | `examples/ex032_category_validation.py` |
| 033 | iqr_outlier_flags | IQR 방식으로 연속형 센서의 통계적 이상값 후보를 플래그 처리합니다. | `examples/ex033_iqr_outlier_flags.py` |
| 034 | winsorize_outliers | 이상값을 삭제하지 않고 분위수 경계로 제한하는 Winsorization을 실습합니다. | `examples/ex034_winsorize_outliers.py` |
| 035 | lot_consistency_check | 한 LOT 안에서 공정 상태 순서와 행 개수를 점검하는 기초 일관성 검사를 수행합니다. | `examples/ex035_lot_consistency_check.py` |
| 036 | state_transition_check | 공정 상태 전이가 허용된 순서인지 검사하는 상태머신 기초를 익힙니다. | `examples/ex036_state_transition_check.py` |
| 037 | cross_sensor_rule_check | 센서 간 물리·공정 논리를 이용한 교차 검증 규칙을 구현합니다. | `examples/ex037_cross_sensor_rule_check.py` |
| 038 | quality_score | 행 단위 품질 플래그를 점수로 합산해 데이터 품질 등급을 만듭니다. | `examples/ex038_quality_score.py` |
| 039 | quality_report | 여러 품질 지표를 한 번에 요약하는 자동 리포트를 생성합니다. | `examples/ex039_quality_report.py` |
| 040 | cleaning_pipeline | 스키마 확인부터 정제·검증·저장까지 재사용 가능한 전처리 파이프라인을 완성합니다. | `examples/ex040_cleaning_pipeline.py` |

## 폴더 구조
```text
semiconductor_physical_ai_stage02_021_040/
├─ data/
│  └─ semiconductor_sensor_data.csv
├─ examples/
│  └─ ex021_...py ~ ex040_...py
├─ guides/
│  └─ guide_021.md ~ guide_040.md
├─ outputs/
├─ generate_base_data.py
├─ environment.yml
├─ setup_windows.bat
└─ run_all_windows.bat
```

## 실무 원칙
1. 원본 데이터는 수정하지 않는다.
2. 정제 전후의 행 수와 변경 건수를 기록한다.
3. 컬럼명, 단위, 허용 범위, 범주값을 코드 밖 설정으로 분리할 준비를 한다.
4. 이상값은 무조건 삭제하지 않고 플래그·보정·격리 중 목적에 맞는 방식을 선택한다.
5. 시간순 정렬 전에 중복과 역순 발생 원인을 먼저 확인한다.
6. 정제 결과와 감사 로그를 함께 보관한다.
