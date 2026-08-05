# 자동차 Physical AI 하네스 엔지니어링
## 26단계 | 501~520제 | ROBOTIS MuJoCo Menagerie TurtleBot3 Burger Viewer

### 공식 모델
이 패키지는 `ROBOTIS-GIT/robotis_mujoco_menagerie`의 다음 파일을 직접 사용합니다.

- `robotis_tb3/scene_turtlebot3_burger.xml`
- `robotis_tb3/turtlebot3_burger.xml`
- `robotis_tb3/assets/`

공식 Burger 모델의 휠 조인트·액추에이터 이름은 `wheel_left`, `wheel_right`입니다.
본 패키지는 공식 mesh와 XML을 재배포하지 않고 설치 스크립트로 저장소를 clone합니다.

### 실습 주제
- 공식 모델 경로·파일 검증
- scene Viewer 실행
- body·joint·actuator 검사
- passive Viewer
- 직진·회전·곡선 주행
- 미션 명령 시퀀스
- Tracking Camera
- base 자유관절 상태
- 휠 속도·오도메트리
- ctrlrange 포화
- 접촉점·접촉력
- 마찰 변화
- 키보드 텔레오퍼레이션
- 장애물·센서 scene 확장
- 상태 초기화
- 통합 Viewer 리포트

### 설치
```bat
conda env create -f environment.yml
conda activate robotis_tb3_burger_viewer
scripts\01_clone_robotis_menagerie.bat
00_check_environment.bat
```

### 실행
```bat
00_run_example_menu.bat
```

### 키보드
예제 516:
- W: 전진
- A: 좌회전
- D: 우회전
- S: 정지
