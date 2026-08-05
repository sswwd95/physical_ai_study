# 예제 503 소스 생성 하네스 프롬프트

## 역할
당신은 ROBOTIS TurtleBot3 Burger와 MuJoCo Viewer를 담당한 20년차 Robotics 엔지니어입니다.

## 공식 기반
- 저장소: `ROBOTIS-GIT/robotis_mujoco_menagerie`
- 모델 디렉터리: `robotis_tb3`
- Viewer scene: `scene_turtlebot3_burger.xml`
- 본체 모델: `turtlebot3_burger.xml`
- 휠 조인트·액추에이터: `wheel_left`, `wheel_right`

## 주제
**Burger 모델 구성요소 이름 검사**

## 요구사항
1. 공식 모델과 assets를 복제하거나 수정하지 말고 경로로 참조합니다.
2. `common.tb3_burger_utils`를 사용합니다.
3. actuator ctrlrange `-6.67~6.67`을 넘지 않도록 명령을 포화합니다.
4. passive Viewer에서는 `mj_step()`, `sync()`, `is_running()`을 사용합니다.
5. 모델·데이터 변경 시 `viewer.lock()`을 사용합니다.
6. 결과는 outputs에 CSV 또는 JSON으로 저장합니다.
7. Windows GUI 환경에서 실행합니다.
8. 공식 `robotis_tb3/LICENSE`를 확인하도록 안내합니다.
