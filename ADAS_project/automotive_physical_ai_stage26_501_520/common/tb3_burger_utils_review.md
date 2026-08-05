# adas_tb3_utils.py

## 개요

`adas_tb3_utils.py`는 TurtleBot3 MuJoCo 예제를 실행하기 위한 공통 유틸리티 모듈이다.

주요 역할은 다음과 같다.

- ROBOTIS MuJoCo 저장소 검색
- TurtleBot3 모델(XML) 로드
- MuJoCo 시뮬레이션 초기화
- 바퀴 속도 제어
- 로봇 위치 및 자세 계산
- 실시간 시뮬레이션 루프 실행
- 결과(JSON) 저장

---

# 전체 실행 흐름

```text
main.py
    │
    ▼
load_tb3()
    │
    ▼
find_repo_root()
    │
    ▼
TurtleBot3 XML 검색
    │
    ▼
MuJoCo Model 생성
    │
    ▼
realtime_loop()
    │
    ├── control()
    ├── mj_step()
    ├── logger()
    └── viewer.sync()
    │
    ▼
save_json()
```

---

# 주요 변수

| 변수 | 설명 |
|------|------|
| ROOT | 프로젝트 최상위 폴더 |
| OUTPUTS | 실행 결과 저장 폴더 |
| REPO_NAME | ROBOTIS 저장소 이름 |
| TB3_DIR_NAME | TurtleBot3 모델 폴더 |
| SCENE_NAME | 기본 Scene XML 파일 |
| MODEL_NAME | TurtleBot3 모델 XML |

---

# 함수 설명

## candidate_repo_roots()

ROBOTIS MuJoCo 저장소를 찾기 위한 후보 경로를 생성한다.

검색 순서는 다음과 같다.

1. 환경 변수
2. 프로젝트 vendor 폴더
3. 프로젝트 상위 폴더
4. 현재 작업 폴더
5. 사용자 홈
6. C:\work

반환값

- 저장소 후보(Path) 리스트

---

## find_repo_root()

후보 경로 중 실제 ROBOTIS 저장소를 찾는다.

`scene_turtlebot3_burger.xml`이 존재하는 폴더를 저장소로 판단한다.

반환값

- ROBOTIS 저장소 경로(Path)

---

## tb3_dir()

TurtleBot3 모델 폴더를 반환한다.

예시

```text
robotis_tb3/
```

---

## scene_path()

기본 Scene XML 경로를 반환한다.

예시

```text
scene_turtlebot3_burger.xml
```

---

## model_path()

TurtleBot3 모델 XML 경로를 반환한다.

예시

```text
turtlebot3_burger.xml
```

---

## output_path(name)

outputs 폴더를 생성한 후 결과 파일 경로를 반환한다.

예시

```python
output_path("result.json")
```

↓

```text
outputs/result.json
```

---

## load_tb3()

MuJoCo 모델을 생성한다.

실행 과정

1. MuJoCo 라이브러리 로드
2. XML 읽기
3. MjModel 생성
4. MjData 생성
5. Body, Joint, Actuator ID 저장

반환값

```python
mujoco
model
data
ids
```

---

## set_wheels()

좌우 바퀴 속도를 설정한다.

```python
set_wheels(data, left_speed, right_speed)
```

속도는 안전 범위인

```text
-6.67 ~ 6.67
```

으로 자동 제한된다.

---

## yaw_from_quat()

Quaternion을 Yaw(회전각)로 변환한다.

반환값

```text
라디안(rad)
```

---

## base_pose()

현재 로봇의 위치와 방향을 반환한다.

반환값

```python
{
    "x_m": ...,
    "y_m": ...,
    "z_m": ...,
    "yaw_rad": ...
}
```

---

## realtime_loop()

실시간 시뮬레이션을 실행한다.

반복 과정

```text
control()

↓

mj_step()

↓

logger()

↓

viewer.sync()

↓

sleep()
```

duration_s 동안 반복 실행된다.

---

## make_extension_scene()

기존 TurtleBot3 모델을 포함한 새로운 Scene XML을 생성한다.

추가 가능한 요소

- 장애물
- 센서
- 액추에이터

생성 위치

```text
extensions/
```

---

## save_json()

Python 객체를 JSON 파일로 저장한다.

예시

```python
save_json(result, "output.json")
```

↓

```text
outputs/output.json
```

---

# 함수 관계

```text
candidate_repo_roots()
        │
        ▼
find_repo_root()
        │
        ▼
tb3_dir()
        │
 ┌──────┴───────┐
 ▼              ▼
scene_path()  model_path()
        │
        ▼
load_tb3()
        │
        ▼
realtime_loop()
        │
 ┌──────┴────────┐
 ▼               ▼
control()     logger()
        │
        ▼
save_json()
```

---

# 핵심 역할 요약

| 함수 | 역할 |
|------|------|
| candidate_repo_roots | 저장소 후보 생성 |
| find_repo_root | 저장소 검색 |
| tb3_dir | TurtleBot3 폴더 반환 |
| scene_path | Scene XML 반환 |
| model_path | Model XML 반환 |
| load_tb3 | MuJoCo 모델 생성 |
| set_wheels | 바퀴 속도 제어 |
| yaw_from_quat | Quaternion → Yaw 변환 |
| base_pose | 현재 위치 반환 |
| realtime_loop | 실시간 시뮬레이션 실행 |
| make_extension_scene | 새로운 Scene 생성 |
| save_json | JSON 저장 |