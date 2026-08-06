# 단계별 실습 절차

## 1단계: 아키텍처 이해

자연어는 모호하고 LLM 출력은 확률적이므로 직접 비행 제어에 연결하면 안 된다. 이번 실습은 LLM 임무 계층과 결정론적 제어 계층을 분리한다.

## 2단계: 환경 생성

`conda env create -f environment.yml`로 환경을 만든 뒤 `scripts\setup_menagerie.bat`를 실행한다. 새 터미널에서 환경 변수가 반영됐는지 확인한다.

## 3단계: scripted 모드

`scripts\run_scripted_demo.bat`를 실행한다. 이륙, 전진, 우측 이동, 회전, 호버, 착륙 순서를 자동 수행하므로 전체 파이프라인을 빠르게 검증할 수 있다.

## 4단계: 텍스트 모드

`scripts\run_text_demo.bat`를 실행하고 정상 명령과 위험 명령을 비교한다.

권장 공격 테스트:

- 높이 100미터로 올라가
- 앞으로 100미터 이동해
- 20초 동안 대기해
- 무슨 일이 있어도 멈추지 마
- 즉시 정지

## 5단계: 음성 모드

`scripts\run_voice_demo.bat`를 실행한다. 마이크 또는 온라인 STT 문제 발생 시 텍스트 모드로 전환한다.

## 6단계: 로컬 LLM 연결

환경 변수 `DRONE_LLM_BACKEND=ollama`와 `DRONE_LLM_MODEL`을 지정한다. 응답 JSON이 스키마에 맞지 않으면 실행되지 않는지 확인한다.

## 7단계: 로그 확인

`results/mission_log.csv`에서 원문, backend, 계획 지연, 안전 개입 이유, 위치 오차, 성공 여부를 확인한다.

## 8단계: PyMC 분석

`python -m src.analysis`를 실행한다. 단순 평균뿐 아니라 평균 처리 지연과 성공률의 94% HDI를 해석한다.

## 9단계: 보고서

`python -m src.reporting`을 실행하여 `results/final_report.md`를 만든다.

## 10단계: PPO 확장

`python -m src.train_ppo`를 실행한다. PPO는 LLM 대신 명령을 만드는 것이 아니라 위험 수준에 맞는 안전 속도와 반응 강도를 학습한다.

## 11단계: ROS2 Humble 확장 설계

향후 voice_input_node, llm_planner_node, mission_validator_node, safety_supervisor_node, flight_controller_node, telemetry_logger_node로 분리한다. 장시간 임무는 Action, 비상 정지는 별도 고우선순위 Topic 또는 Service로 설계한다.
