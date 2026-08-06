# 음성 LLM 기반 자연어 드론 Physical AI 프로젝트

## 핵심 주제

마이크 또는 텍스트 자연어 명령을 LLM이 구조화된 임무 JSON으로 변환하고, 안전 감독기가 검증한 뒤 MuJoCo 3.6.0의 Skydio X2 시뮬레이션에서 실행한다. 처리 지연·성공률·안전 개입을 기록하고 PyMC로 불확실성을 분석하며 StableBaselines3 PPO 확장 실습을 제공한다.

## 파이프라인

음성 입력 → STT → LLM Planner → Pydantic Mission Schema → Safety Supervisor → 결정론적 비행 제어기 → MuJoCo Viewer → CSV 로그 → PyMC 분석 → 결과 보고서

## 실무 핵심

- LLM을 actuator에 직접 연결하지 않는다.
- LLM은 목표 임무만 JSON으로 제안한다.
- 허용 동작 목록, 고도, 속도, 지오펜스, 대기 시간 제한을 둔다.
- 불명확한 명령은 추측 실행하지 않고 emergency_stop으로 처리한다.
- 비상 정지는 LLM과 일반 임무보다 높은 우선순위를 갖는다.
- 시뮬레이션 로그에는 원문, LLM backend, 수정·거부 이유, 지연, 결과를 남긴다.

## 설치

```bat
conda env create -f environment.yml
conda activate voice-llm-drone
scripts\setup_menagerie.bat
```

환경 변수 반영을 위해 새 Anaconda Prompt를 연 뒤 실행한다.

```bat
conda activate voice-llm-drone
cd 프로젝트_폴더
scripts\run_scripted_demo.bat
```

텍스트 명령:

```bat
scripts\run_text_demo.bat
```

마이크 명령:

```bat
scripts\run_voice_demo.bat
```

로컬 Ollama LLM 사용:

```bat
set DRONE_LLM_BACKEND=ollama
set DRONE_LLM_MODEL=qwen2.5:3b
python -m src.main --input text --viewer
```

Ollama가 없거나 응답이 실패하면 규칙 기반 안전 파서로 자동 전환된다.

## 명령 예

- 이륙해서 높이 2미터로 올라가
- 앞으로 3미터 이동해
- 오른쪽으로 1미터 이동해
- 왼쪽으로 90도 회전해
- 좌표 x 2, y 1, 높이 2로 이동해
- 제자리에서 5초 동안 대기해
- 착륙해
- 즉시 정지

## 분석과 보고서

```bat
scripts\run_analysis.bat
```

생성 파일:

- results/mission_log.csv
- results/mission_summary.json
- results/pymc_latency.png
- results/pymc_success_rate.png
- results/bayesian_summary.json
- results/final_report.md

## PPO 확장

```bat
python -m src.train_ppo
```

PPO는 자연어를 해석하거나 비행 경로를 직접 생성하지 않는다. 위험 수준에 따른 속도 제한과 안전 반응 강도를 조정하는 보조 실습이다.

## 안전 주의

이 프로젝트는 MuJoCo 교육용 시뮬레이션 전용이다. 실기체 연결 코드는 포함하지 않는다.
