# 반도체 Physical AI 하네스 엔지니어링 — 2단계

실습 006~010은 분석 알고리즘을 만들기 전에 필요한 실행·검증·안전 기반을 다룹니다.

## 포함 내용
- YAML 기반 설정 분리
- 콘솔·파일 구조화 로그
- Python 실행 파이프라인
- 사전 환경 점검
- Antigravity 안전 작업 정책
- pytest 자동 검증

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

## 안전 주의
이 예제는 합성 데이터와 로컬 파일 작업만 수행합니다. 실제 반도체 장비 제어, 레시피 변경, 인터록 우회는 포함하지 않습니다.
