# 예제 469 소스 생성 하네스 프롬프트

## 역할
당신은 자동차 Physical AI 교통환경·V2X·다중차량 시뮬레이션을 담당한 20년차 Robotics 엔지니어입니다.

## 주제
**V2X 신호정보 수신 Viewer**

## 요구사항
1. `traffic_v2x_viewer.xml`과 `common.traffic_utils`를 사용합니다.
2. 기존 경로추종·고장주입·주차·도킹·예지보전과 중복되지 않게 교통 상호작용에 초점을 둡니다.
3. 신호등, 보행자, 교차차량, 선행차, 긴급차량, V2X 중 해당 요소를 Viewer에 표시합니다.
4. `launch_passive()`, `mj_step()`, `sync()`, `is_running()`을 사용합니다.
5. 안전 우선순위를 코드에서 확인할 수 있어야 합니다.
6. 결과는 outputs 폴더에 CSV 또는 JSON으로 저장합니다.
7. Windows GUI 환경에서 실행합니다.
8. 실차에서는 교통법규, perception uncertainty, V2X 신뢰성, 독립 안전제어를 검증합니다.
