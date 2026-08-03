# 실습 001~005 라인별 해설

## 실습 001 프로젝트 설정 하네스
1. `Path(__file__).resolve().parents[1]`은 실행 위치와 무관하게 프로젝트 루트를 찾습니다.
2. `PATHS`는 데이터·결과·문서 위치를 한곳에서 관리합니다.
3. `mkdir(..., exist_ok=True)`는 폴더가 이미 있어도 안전합니다.
4. `CONFIG`는 재현성에 필요한 시드, 주기, 단위를 기록합니다.
5. JSON 저장은 사람과 프로그램이 모두 읽기 쉽습니다.

## 실습 002 센서 데이터 생성
1. `default_rng(42)`로 같은 교육 데이터를 재현합니다.
2. `date_range(..., freq="s")`로 1초 간격 시계열을 만듭니다.
3. 각 센서는 정상 평균과 작은 변동을 갖습니다.
4. 특정 구간에 드리프트·스파이크·동시 이상을 삽입합니다.
5. DataFrame으로 센서들을 같은 시간축에 정렬합니다.
6. UTF-8 BOM CSV로 저장해 Windows Excel 호환성을 높입니다.

## 실습 003 데이터 계약 검사
1. 필수 열과 물리적 범위를 명세합니다.
2. 시간 문자열을 datetime으로 강제 변환하며 실패값은 결측이 됩니다.
3. 열 누락은 분석 불가능 상태이므로 즉시 예외를 발생시킵니다.
4. 결측과 범위 이탈을 센서별로 집계합니다.
5. 시간 역전은 스트리밍·ROS2 연계에서 심각하므로 별도 검사합니다.
6. 모든 검사를 사람이 이해할 수 있는 메시지로 출력합니다.

## 실습 004 기본 모니터링
1. `parse_dates`로 시간 열을 즉시 변환합니다.
2. 교육용 공정 한계를 사전으로 관리합니다.
3. `between`의 반대로 범위 이탈 경보를 만듭니다.
4. 센서 경보 중 하나라도 참이면 공정 경보입니다.
5. 경보 원인을 문자열로 남겨 추적성을 확보합니다.
6. 전체 결과와 경보 요약을 저장합니다.

## 실습 005 베이지안 온도 추정
1. 이상이 주입되기 전 초기 200개 샘플을 정상 기준으로 사용합니다.
2. `pm.Model()` 안에서 확률 모델을 선언합니다.
3. 평균 `mu`의 사전분포는 65°C 주변이지만 충분히 넓게 둡니다.
4. `sigma`는 음수가 될 수 없어 HalfNormal을 사용합니다.
5. 관측값이 정규분포를 따른다는 단순 모델을 세웁니다.
6. MCMC로 평균·변동의 불확실성을 함께 계산합니다.
7. ArviZ가 평균, HDI, ESS, r_hat을 요약합니다.
8. HDI는 하나의 점이 아니라 가능한 정상 평균 범위를 보여줍니다.

## 실행 순서
```bat
conda env create -f environment.yml
conda activate semi-physical-ai
python examples\example_001_project_config.py
python examples\example_002_generate_sensor_data.py
python examples\example_003_validate_sensor_schema.py
python examples\example_004_basic_monitoring.py
python examples\example_005_bayesian_temperature.py
```
