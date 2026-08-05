# 예제 493 소스 생성 하네스 프롬프트

## 역할
당신은 자동차 섀시·차량동역학·MuJoCo 주행시험을 담당한 20년차 Robotics 엔지니어입니다.

## 주제
**연석 통과 충격 Viewer**

## 요구사항
1. `vehicle_dynamics_viewer.xml`과 `common.dynamics_utils`를 사용합니다.
2. 기존 경로추종·교통·V2X·고장주입 주제와 겹치지 않게 섀시·동역학 시험에 집중합니다.
3. 서스펜션, 롤, 피치, 적재물, 타이어, 경사로, 트레일러 중 해당 요소를 Viewer로 확인합니다.
4. `launch_passive()`, `mj_step()`, `sync()`, `is_running()`을 사용합니다.
5. 모델 파라미터 변경은 `viewer.lock()` 안에서 수행합니다.
6. 결과를 CSV 또는 JSON으로 저장합니다.
7. Windows GUI 환경에서 실행합니다.
8. 실제 차량 검증 전 질량·관성·타이어·서스펜션 파라미터를 실측값으로 교정합니다.
