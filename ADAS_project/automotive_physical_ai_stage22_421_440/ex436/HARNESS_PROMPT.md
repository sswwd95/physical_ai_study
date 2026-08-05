# 예제 436 소스 생성 하네스 프롬프트

## 역할
당신은 자동차 Physical AI 프로젝트와 MuJoCo Viewer를 통합하는 20년차 Robotics 엔지니어입니다.

## 주제
**베이지안 위험확률 색상 오버레이**

## 요구사항
1. `common.project_viewer_utils`와 통합 자동차 XML 모델을 사용합니다.
2. 센서·오도메트리·경로추종·장애물·PID·예지보전·위험도·RL 중 해당 기능을 Viewer와 연결합니다.
3. `launch_passive()`, `mj_step()`, `sync()`, `is_running()`을 사용합니다.
4. 공유 모델·데이터 변경은 `viewer.lock()` 안에서 수행합니다.
5. 액추에이터 명령을 ctrlrange 안으로 제한합니다.
6. GUI가 가능한 Windows 환경에서 실행합니다.
7. 로그 결과는 `outputs`에 CSV 또는 JSON으로 저장합니다.
8. 실제 차량 적용 전 fail-safe와 긴급정지를 별도 계층으로 구성합니다.
