# 실습 006~010 라인별 해설

## 실습 006 YAML 설정 로더
1. 프로젝트 루트를 코드 실행 위치와 무관하게 계산합니다.
2. `config/project_config.yaml`을 설정의 단일 기준점으로 사용합니다.
3. `yaml.safe_load`는 YAML을 Python 사전으로 안전하게 읽습니다.
4. 상대경로를 프로젝트 루트와 결합해 실제 경로를 만듭니다.
5. 필요한 폴더를 자동 생성해 초기 실행 오류를 줄입니다.
6. 핵심 설정을 출력해 잘못된 환경을 조기에 발견합니다.

## 실습 007 구조화 로그
1. 로그 YAML을 읽고 파일 경로를 절대경로로 변환합니다.
2. `dictConfig`로 콘솔·파일 로깅을 동시에 설정합니다.
3. 이름 있는 로거는 모듈과 기능별 추적을 쉽게 합니다.
4. INFO, WARNING, ERROR 수준을 구분해 운영 가독성을 높입니다.
5. `logger.exception`은 오류 메시지와 호출 스택을 함께 기록합니다.
6. 실제 분석 파이프라인에서는 센서 파일명, 배치 ID, 모델 버전도 로그에 포함합니다.

## 실습 008 실행 파이프라인
1. 실행 순서를 리스트로 명시해 재현성을 확보합니다.
2. `sys.executable`은 현재 활성화된 Conda Python을 그대로 사용합니다.
3. 표준 출력을 수집해 하네스가 실행 결과를 관리합니다.
4. 표준 오류도 숨기지 않고 표시합니다.
5. 종료 코드가 0이 아니면 즉시 중단해 연쇄 오류를 막습니다.
6. `shell=True`를 쓰지 않아 명령 주입 위험을 낮춥니다.

## 실습 009 사전 점검
1. 필요한 파일·폴더 목록을 먼저 정의합니다.
2. 필요한 패키지를 명시합니다.
3. Python 버전과 운영체제를 확인합니다.
4. 경로가 없으면 문제 목록에 추가합니다.
5. import 가능 여부로 실제 설치 상태를 확인합니다.
6. YAML의 필수 섹션을 검사합니다.
7. 모든 문제를 모아 한 번에 보여주고 실패 코드를 반환합니다.

## 실습 010 Antigravity 안전 작업 정책
1. 에이전트가 수정할 수 있는 작업 영역을 선언합니다.
2. 프로젝트 밖 수정, 실제 장비 제어, 인터록 우회 등을 금지합니다.
3. 변경 전 파일 목록, 자동 테스트, 롤백 가능한 로그를 요구합니다.
4. 허용 경로가 프로젝트 내부인지 코드로 다시 검사합니다.
5. JSON 정책 파일은 사람과 프로그램이 모두 읽을 수 있습니다.
6. 이 정책은 실제 플랫폼 권한 설정과 함께 사용해야 하며 문서만으로 보안을 보장하지는 않습니다.

## 실행 순서

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_006_yaml_config_loader.py
python examples\example_007_structured_logging.py
python examples\example_008_pipeline_runner.py
python examples\example_009_preflight_check.py
python examples\example_010_safe_agent_workspace.py

pytest -q
```
