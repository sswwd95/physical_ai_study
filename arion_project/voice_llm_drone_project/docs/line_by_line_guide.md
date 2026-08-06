# 핵심 소스 라인별 해설

## mission_schema.py

- `ActionName`: 허용 가능한 임무 이름을 고정한다.
- `MissionCommand`: LLM의 자유문을 검증 가능한 데이터 구조로 바꾼다.
- `defaults`: 이륙 높이나 호버 시간이 빠졌을 때 안전 기본값을 넣는다.
- `SafetyDecision`: 승인, 수정, 이유, 위험도를 하나의 결과로 보관한다.

## llm_planner.py

- `SYSTEM_PROMPT`: LLM이 JSON만 반환하도록 출력 계약을 정의한다.
- 환경 변수는 수업 중 backend와 모델을 코드 변경 없이 교체하게 한다.
- `_ollama`: 로컬 LLM에 요청하고 반환 JSON을 Pydantic으로 검증한다.
- `_rule`: LLM 서버가 없어도 핵심 실습이 중단되지 않게 한다.
- 해석하지 못한 문장은 `emergency_stop`으로 처리한다.

## safety.py

- `max_altitude`, `max_dist`, `max_speed`: 물리적 안전 한계다.
- `review`: 실행 직전 명령을 다시 검사한다.
- 초과 속도와 대기 시간은 상한으로 수정한다.
- 지오펜스 이탈과 고도 위반 예상 명령은 거부한다.
- 비상 정지는 조건 없이 승인한다.

## scene_builder.py

- 환경 변수와 프로젝트 내부 Menagerie 경로를 모두 검사한다.
- Skydio X2의 `scene.xml`과 `x2.xml`을 차례로 시도한다.
- 로딩 실패 시 최소 quadrotor 모델로 전환하여 수업 흐름을 유지한다.
- fallback 모델은 자연어 임무 계층 실습용이며 정밀 동역학 검증용이 아니다.

## drone_controller.py

- 첫 번째 free joint의 qpos 주소를 찾는다.
- LLM은 목표 위치와 회전만 제시한다.
- `set_command`가 상대 명령을 절대 목표로 바꾼다.
- `step`은 timestep마다 목표 방향으로 제한된 거리만 이동한다.
- 위치 오차와 yaw 오차가 허용 범위 안이면 완료로 판정한다.

## main.py

- 입력 방식은 text, voice, scripted다.
- `perf_counter`로 LLM 계획 지연을 측정한다.
- Safety Supervisor 승인 후에만 제어기를 호출한다.
- Viewer와 simulation timestep을 동기화한다.
- timeout을 두어 명령이 무한 실행되지 않게 한다.
- 각 명령의 결과를 CSV로 기록하고 전체 요약을 JSON으로 저장한다.

## analysis.py

- 처리 지연 평균에는 Normal 사전분포를 사용한다.
- 처리 지연 표준편차에는 HalfNormal을 사용한다.
- 성공률에는 Beta(1,1) 사전분포를 사용한다.
- Bernoulli 관측모델로 성공과 실패를 표현한다.
- 사후평균과 94% HDI를 JSON 및 그래프로 저장한다.

## rl_env.py / train_ppo.py

- 상태는 목표 오차와 위험 수준이다.
- 행동은 속도 제한과 안전 반응 강도다.
- 위험한데 속도가 빠르면 큰 벌점을 준다.
- PPO는 안전 감독기 보조 파라미터를 튜닝하는 제한된 역할이다.
