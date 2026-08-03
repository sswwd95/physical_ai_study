# 반도체 Physical AI 하네스 엔지니어링 400제

이 압축 파일은 **1단계 실습 001~005**와 전체 400제 로드맵을 포함합니다.

## 학습 목표
- 재현 가능한 반도체 데이터 분석 프로젝트 구조 만들기
- 장비 센서 데이터 모사와 데이터 계약 검사
- 임계값 기반 공정 모니터링
- PyMC를 이용한 정상 온도 평균·변동의 불확실성 추정
- 이후 ROS2 Humble 토픽·노드 구조로 옮길 수 있는 입력/출력 계약 습관 형성

## 폴더
- `examples/`: 그대로 실행 가능한 Python 소스
- `prompts/`: Antigravity 등 코딩 에이전트에 넣을 생성·검증 하네스 프롬프트
- `docs/`: 400제 로드맵과 라인별 해설
- `data/`: 실행 중 생성되는 센서 CSV
- `outputs/`: 설정, 모니터링, 베이지안 결과
- `environment.yml`: 권장 Conda 환경

## 안전 원칙
- 실제 장비 제어, 레시피 변경, 인터록 우회 명령은 포함하지 않습니다.
- 모든 예제는 합성 데이터 또는 읽기 전용 분석을 기본으로 합니다.
- Antigravity 같은 에이전트에는 프로젝트 폴더 밖 파일 삭제·수정 금지 조건을 둡니다.
- 실제 Fab 적용 전에는 공정·설비·안전 담당자의 승인과 검증이 필요합니다.

## 실행
Anaconda Prompt에서 프로젝트 폴더로 이동한 후:

```bat
conda env create -f environment.yml
conda activate semi-physical-ai
python examples\example_001_project_config.py
python examples\example_002_generate_sensor_data.py
python examples\example_003_validate_sensor_schema.py
python examples\example_004_basic_monitoring.py
python examples\example_005_bayesian_temperature.py
```
